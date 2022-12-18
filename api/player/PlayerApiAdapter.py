from typing import List, Union

from SM_Framework.SMBotFramework.api.base.BaseAdapter import BaseAdapter
from SM_Framework.SMBotFramework.data.Session import Session


class PlayerApiAdapter(BaseAdapter):

    def adapt_mark_as_read(self, session, message_id: str):
        request: dict = {}
        self._add_session_params(session, request)
        request["id"] = message_id
        return request

    def adapt_messages(self, session, message_type: Union[str, List[str]] = None, trx_id: str = None):
        request: dict = {}
        self._add_session_params(session, request)

        if message_type and type(message_type) == List[str]:
            request["types"] = ",".join(message_type)

        if message_type and type(message_type) == str:
            request["type"] = message_type

        if trx_id:
            request["tid"] = trx_id
        return request

    def adapt_outstanding_match(self, session: Session):
        request: dict = {}
        self._add_session_params(session, request)
        request["head_block"] = session.blockchain.get_current_block_num()
        return request

    def adapt_get_player_details(self, session: Session, name: str, teams: bool):
        request: dict = {}
        self._add_session_params(session, request)

        if name:
            request["name"] = name
        if teams is not None:
            request["teams"] = teams

        return request

    def adapt_get_balance_history(self, username: str, token_type: str, offset: int, limit: int,
                                  session: Session = None):
        request: dict = {}
        self._add_session_params(session, request)
        request["username"] = username
        request["token_type"] = token_type
        request["offset"] = offset
        request["limit"] = limit

        return request
