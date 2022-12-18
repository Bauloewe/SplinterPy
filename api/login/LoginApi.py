from SM_Framework.SMBotFramework.api.login.data.AuthResponse import AuthResponse
from SM_Framework.SMBotFramework.api.login.data.LoginRequest import LoginRequest
from SM_Framework.SMBotFramework.api.login.data.LoginResponse import LoginResponse
from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_PLAYERS_AUTH, GET_PLAYERS_LOGIN


class LoginApi:
    base_caller: BaseApiCaller

    def __init__(self):
        self.base_caller = BaseApiCaller()

    def login(self, request: LoginRequest) -> LoginResponse:
        url: str = BASE_API2 + GET_PLAYERS_LOGIN
        return LoginResponse(self.base_caller.call_get(url, request.__dict__))

    def auth(self, user: str, token: str) -> AuthResponse:
        url: str = BASE_API2 + GET_PLAYERS_AUTH
        request: dict = {"username": user, "token": token}
        return AuthResponse(self.base_caller.call_get(url, request))
