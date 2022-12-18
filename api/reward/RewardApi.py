import time

from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_EC_API, GET_EC_PLAYERS_CLAIMSPSAIR
from SM_Framework.SMBotFramework.api.reward.RewardAdapter import RewardAdapter
from SM_Framework.SMBotFramework.data.Session import Session


class RewardApi:
    baseCaller: BaseApiCaller
    adapter: RewardAdapter

    def __init__(self):
        self.baseCaller = BaseApiCaller()
        self.adapter = RewardAdapter()

    """
        Claims the SPS Airdrop for the specified platform/address
        session -- current user session object (SMBotFramework.data.Session)
        platform -- the platform where the splinterland assets are located e.g. hive, binance, wax, eth, steem or tron
        address -- address on the specified plattform e.g. hive/steem name
        ts -- a recent timestamp, per default the current timestamp 
    """

    def claim_sps_airdrop(self, session: Session, platform: str, address: str, ts: int = int(time.time() * 1000)):
        url: str = BASE_EC_API + GET_EC_PLAYERS_CLAIMSPSAIR
        request = self.adapter.adapt_claim_sps_airdrop(session, platform, address, ts)
        return self.baseCaller.call_get(url, request)

    """
        Claims stake reward from staked SPS
    """

    def claim_staked_sps(self, session: Session):
        request = {"token": "SPS", "qty": 0}
        session.hive.custom_json("sm_stake_tokens", json_data=request, required_posting_auths=[session.user])

    """
        Stake the given amount of SPS (unchecked)
        qty -- amount of SPS to stake qty = 0 -> claim stake reward
    """

    def stake_sps(self, session: Session, qty: int):
        if qty is not None:
            request = {"token": "SPS", "qty": qty}
            session.hive.custom_json("sm_stake_tokens", json_data=request, required_posting_auths=[session.user])
        else:
            print("Quantity is not set")
