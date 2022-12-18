import json
from typing import List, Union

import requests

from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_PLAYERS_VERIFY, GET_PLAYERS_FAQ, \
    GET_PLAYERS_SKIN, GET_PLAYERS_ITEMDET, GET_PLAYERS_DAILYUPDATES, \
    GET_PLAYERS_DYK, GET_PLAYERS_VERSTATUS, GET_PLAYERS_MARKASREAD, GET_PLAYERS_MESSAGES, GET_PLAYERS_REFRESH_GUILD, \
    GET_PLAYERS_OUTSTANDING_MATCH, GET_PLAYERS_EXISTS, GET_PLAYERS_DETAILS, GET_PLAYERS_SPS, BASE_EC_API, \
    GET_EC_PLAYERS_SPSDATA, POST_TRX, GET_PLAYER_BAL_HISTORY
from SM_Framework.SMBotFramework.api.data.SplinterlandsData import Skins, DetailItems, \
    DailyUpdates, Dyk, VerificationStatus, Messages, PlayerDetails, SPSOverview, SpsGeneralData, BalanceHistory
from SM_Framework.SMBotFramework.api.player.PlayerApiAdapter import PlayerApiAdapter
from SM_Framework.SMBotFramework.api.player.data.VerifyEmailRequest import VerifyEmailRequest
from SM_Framework.SMBotFramework.data.Session import Session
from SM_Framework.SMBotFramework.hive.HiveFactory import HiveFactory


class PlayerApi:
    base_caller: BaseApiCaller
    adapter: PlayerApiAdapter

    def __init__(self):
        self.base_caller = BaseApiCaller()
        self.adapter = PlayerApiAdapter()

    def verify_email(self, request: VerifyEmailRequest):
        url: str = BASE_API2 + GET_PLAYERS_VERIFY
        return self.base_caller.call_get(url, request.__dict__)

    def get_faq(self, locale: str):
        url: str = BASE_API2 + GET_PLAYERS_FAQ + "/" + locale
        return self.base_caller.call_get(url)

    def get_player_skins(self, player: str) -> Skins:
        url: str = BASE_API2 + GET_PLAYERS_SKIN

        return Skins(self.base_caller.call_get(url, {"username": player}))

    def get_item_details(self):
        url: str = BASE_API2 + GET_PLAYERS_ITEMDET
        return DetailItems(self.base_caller.call_get(url))

    def get_daily_updates(self):
        url: str = BASE_API2 + GET_PLAYERS_DAILYUPDATES
        return DailyUpdates(self.base_caller.call_get(url))

    def get_dyk(self, locale: str):
        url: str = BASE_API2 + GET_PLAYERS_DYK + "/" + locale
        return Dyk(self.base_caller.call_get(url))

    def get_verification_status(self, player: str):
        url: str = BASE_API2 + GET_PLAYERS_VERSTATUS
        return VerificationStatus(self.base_caller.call_get(url, {"username": player}))

    def mark_as_read(self, session, message_id: str):
        url: str = BASE_API2 + GET_PLAYERS_MARKASREAD
        request = self.adapter.adapt_mark_as_read(session, message_id)
        return self.base_caller.call_get(url, request)

    """
        Get all splinterland messages
        session -- current user session object (SMBotFramework.data.Session)
        message_type -- type of message - either string or list of strings. All message types if None
        trx_id -- tournament trx_id for messages from tournament
    """

    def get_messages(self, session: Session, message_type: Union[str, List[str]] = None, trx_id: str = None):
        url: str = BASE_API2 + GET_PLAYERS_MESSAGES
        request = self.adapter.adapt_messages(session, message_type, trx_id)
        return Messages(self.base_caller.call_get(url, request))

    def get_refresh_guild(self, session: Session):
        url: str = BASE_API2 + GET_PLAYERS_REFRESH_GUILD
        request = self.adapter.build_base_request(session)
        return self.base_caller.call_get(url, request)

    def get_outstanding_match(self, session: Session):
        url: str = BASE_API2 + GET_PLAYERS_OUTSTANDING_MATCH
        request = self.adapter.adapt_outstanding_match(session)
        return self.base_caller.call_get(url, request)

    """ Check if player exists. 
        session -- Session of the calling user
        player -- Name of player to check existence
        Note: doesn't seem to work with other users ?
    """

    def player_exists(self, session: Session, player: str):
        url: str = BASE_API2 + GET_PLAYERS_EXISTS + "/" + player
        request = self.adapter.build_base_request(session)
        return self.base_caller.call_get(url, request)

    def get_player_details(self, session: Session, name: str, teams: bool = None) -> PlayerDetails:
        url: str = BASE_API2 + GET_PLAYERS_DETAILS
        request = self.adapter.adapt_get_player_details(session, name, teams)
        return PlayerDetails(self.base_caller.call_get(url, request))

    """
        Gets the SPS Overview (total staked sps, airdrop points, assets etc)
    """

    def get_sps(self, session: Session):
        url: str = BASE_API2 + GET_PLAYERS_SPS
        request = self.adapter.build_base_request(session)
        return SPSOverview(self.base_caller.call_get(url, request))

    """
        Loads SPS Data (total supply, current wallet balance"
    """

    def get_ec_sps_data(self, session: Session):
        url: str = BASE_EC_API + GET_EC_PLAYERS_SPSDATA
        request = self.adapter.build_base_request(session)
        return SpsGeneralData(self.base_caller.call_get(url, request))

    def transfer_token(self, recipient: str, token: str, amount: float, session: Session):
        request = {"to": recipient, "token": token, "qty": amount}
        session.hive.custom_json("sm_token_transfer", json_data=request, required_auths=[session.user])

    def transfer_card(self, recipient: str, cards: List[str], session: Session):
        request = {"to": recipient, "cards": cards}
        session.hive.custom_json("sm_gift_cards", json_data=request, required_auths=[session.user])

    def purchase(self, purchase_type: str, qty: int, currency: str, session: Session, on_chain: bool = False):
        hive_id: str = "sm_purchase"
        request = {"type": purchase_type, "qty": qty, "currency": currency}
        hive = session.hive if on_chain else HiveFactory.copy_no_broadcast(session.hive, session.user)

        trx: dict = hive.custom_json(hive_id, json_data=request,
                                     required_posting_auths=[session.user])
        if not on_chain:
            trx: str = json.dumps(trx)
            trx = requests.post(POST_TRX, data={"signed_tx": trx}).json()
            trx_id = trx["id"]
        else:
            trx_id = trx["trx_id"]

        return trx_id

    def combine_cards(self, cards: List[str], session: Session):
        id: str = "sm_combine_cards"
        request = {"cards": cards}
        session.hive.custom_json(id, json_data=request, required_auths=[session.user])

    def get_balance_history(self, username: str, token_type: str, offset: int, limit: int, session: Session = None):
        url: str = BASE_API2 + GET_PLAYER_BAL_HISTORY
        request = self.adapter.adapt_get_balance_history(username, token_type, offset, limit, session)
        return BalanceHistory(self.base_caller.call_get(url, request))
