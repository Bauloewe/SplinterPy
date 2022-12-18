from datetime import datetime
from typing import Dict, List

from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.card.CardAdapter import CardAdapter
from SM_Framework.SMBotFramework.api.card.CardUtil import CardUtil
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_CARDS_COLLECTION, GET_CARDS_DETAILS
from SM_Framework.SMBotFramework.api.data.SplinterlandsData import Collection, CardDetails, CardItem, GeneralSettings, \
    CardDetail
from SM_Framework.SMBotFramework.api.util.UtilApi import UtilApi
from SM_Framework.SMBotFramework.data.Session import Session


class CardApi:
    base_caller: BaseApiCaller
    adapter: CardAdapter
    util: CardUtil
    details: Dict[int, CardDetail] = dict()

    def __init__(self):
        self.base_caller = BaseApiCaller()
        self.adapter = CardAdapter()
        self.util = CardUtil()
        self.__prepare_details_map(self.get_card_details())
        self.settings = UtilApi().get_settings()

    def __prepare_details_map(self, details: CardDetails):
        for card in details:
            self.details[card.id] = card

    def get_card_collection(self, player, session: Session = None):
        url: str = BASE_API2 + GET_CARDS_COLLECTION + "/" + player
        query = self.adapter.build_base_request(session)
        return Collection(self.base_caller.call_get(url, params=query))

    def get_card_details(self,session:Session = None):
        url: str = BASE_API2 + GET_CARDS_DETAILS
        query = self.adapter.build_base_request(session)
        return CardDetails(self.base_caller.call_get(url, query))

    def calc_bcx_param(self, xp: int, card_detail_id: int, edition: int, gold: bool):
        rarity: int = self.details.get(card_detail_id, CardDetails()).rarity
        beta: bool = self.util.is_beta(card_detail_id, edition)
        alpha: bool = self.util.is_alpha(edition)
        xp_table = self.util.determine_xp_table(rarity, alpha, beta, gold)
        xp_base = self.util.determine_base_xp(rarity, xp_table, alpha, beta, gold) if alpha or beta else 1
        add_card: int = 0 if xp_base == 1 or gold else 1
        return (xp / xp_base) + add_card  # +1 because the initial card doesn't get counted in xp

    def calc_bcx(self, card: CardItem):
        return self.calc_bcx_param(card.xp, card.card_detail_id, card.edition, card.gold)

    def is_rental_cooldown(self,card: CardItem, settings_timestamp: int, cooldown_blocks: int):
        cd_blocks = cooldown_blocks * 3000
        delta = settings_timestamp - cd_blocks
        used_and_transferred = card.last_transferred_date and card.last_used_date
        cooldown = False
        if used_and_transferred:
            transfer_date = datetime.strptime(card.last_transferred_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            last_used_date = datetime.strptime(card.last_used_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            cooldown = transfer_date.timestamp() * 1000 >= delta and last_used_date.timestamp() * 1000 >= delta

        return not card.market_id and cooldown





"""CanPlayCard(card)
    {
    if (card.market_id & & card.market_listing_status == 0)
    return false;
    if (
    !card.last_transferred_date | | !card.last_used_date | | (card.delegated_to ? card.delegated_to == card.last_used_player: card.player == card.last_used_player))
    return true;


    var
    cooldown_start = new
    Date(SM.settings.timestamp - SM.settings.transfer_cooldown_blocks * 3e3);
    return new
    Date(card.last_transferred_date) <= cooldown_start | | new
    Date(card.last_used_date) <= cooldown_start
    },
"""
