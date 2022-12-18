from SM_Framework.SMBotFramework.api.base.BaseAdapter import BaseAdapter
from SM_Framework.SMBotFramework.data.Session import Session


class BattleAdapter(BaseAdapter):

    def adapt_get_battle(self, session: Session, battle_id: str):
        request: dict = {}
        self._add_session_params(session, request)
        request["id"] = battle_id
        return request

    def adapt_get_battle_history2(self,player: str, session: Session = None):
        request: dict = {}
        self._add_session_params(session, request)
        request["player"] = player
        return request
