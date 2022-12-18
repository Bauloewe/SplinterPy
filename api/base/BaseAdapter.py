from SM_Framework.SMBotFramework.data.Session import Session


class BaseAdapter:
    def _add_session_params(self, session: Session, request: dict):
        if session and request is not None:
            request["username"] = session.user
            request["token"] = session.token

    def build_base_request(self, session: Session):
        request = {}
        if session:
            self._add_session_params(session, request)
        return request

