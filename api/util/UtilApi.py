from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_SETTINGS
from SM_Framework.SMBotFramework.api.data.SplinterlandsData import GeneralSettings


class UtilApi:
    caller: BaseApiCaller()

    def __init__(self):
        self.caller = BaseApiCaller()

    def get_settings(self):
        url: str = BASE_API2 + GET_SETTINGS
        return GeneralSettings(self.caller.call_get(url))
