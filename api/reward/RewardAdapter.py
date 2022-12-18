from SM_Framework.SMBotFramework.api.base.BaseAdapter import BaseAdapter
from SM_Framework.SMBotFramework.data.Session import Session


class RewardAdapter(BaseAdapter):

    def adapt_claim_sps_airdrop(self, session: Session, platform: str, address: str, ts: int):
        request = {}
        self._add_session_params(session, request)
        request["platform"] = platform
        if address and ts and platform:
            request["address"] = address
            request["ts"] = ts
            base_sig = platform + address + str(ts)
            request["sig"] = session.compute_sig(base_sig)

        return request
