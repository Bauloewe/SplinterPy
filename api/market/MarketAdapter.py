from SM_Framework.SMBotFramework.api.base.BaseAdapter import BaseAdapter
from SM_Framework.SMBotFramework.data.Session import Session


class MarketAdapter(BaseAdapter):

    def adapt_market_by_card(self, card_id: int, edition: int, gold: bool = False, session: Session = None):
        request: dict = {}
        self._add_session_params(session, request)
        request["card_detail_id"] = card_id
        request["gold"] = str(gold).lower()
        request["edition"] = edition

        return request

    def adapt_grouped_market(self, lvl: str, session: Session = None):
        request: dict = {}
        self._add_session_params(session, request)
        request["level"] = lvl
        return request

    def adapt_active_rentals(self, owner: str, renter: str, limit: int, skip: int, session: Session = None):
        request: dict = {}
        self._add_session_params(session, request)
        if owner:
            request["owner"] = owner
        elif renter:
            request["renter"] = renter

        request["limit"] = limit
        request["skip"] = skip

        return request
