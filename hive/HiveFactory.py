import os

from beem import Hive
from beem.exceptions import MissingKeyError
from dotenv import load_dotenv

from SM_Framework.SMBotFramework.hive.HiveEnv import HiveEnv
from SM_Framework.SMBotFramework.hive.exceptions.HiveConfigException import HiveConfigException
from SM_Framework.SMBotFramework.hive.exceptions.HiveUnlockException import HiveUnlockException


class HiveFactory:

    @classmethod
    def from_private_key(cls, posting: str, active: str = None):
        return cls._create_temp_hive_cred(posting, active)

    @classmethod
    def build_hive(cls):
        load_dotenv()
        user: str = HiveFactory._load_env(HiveEnv.USER.value)
        pw: str = HiveFactory._load_env(HiveEnv.PW.value)
        posting: str = HiveFactory._load_env(HiveEnv.POSTING.value)
        active: str = HiveFactory._load_env(HiveEnv.ACTIVE.value)
        if user and (posting or active):
            return HiveFactory._create_temp_hive_cred(posting, active)
        elif user:
            return HiveFactory._load_hive_beempy_wallet(pw)
        else:
            raise HiveConfigException([user, pw, posting, active])

    @staticmethod
    def _load_hive_beempy_wallet(pw: str = None):
        hive: Hive = Hive()
        locked: bool = hive.wallet.locked()

        if locked and pw:
            hive.wallet.unlock(pw)
        elif locked and not pw:
            raise HiveUnlockException()

        return hive

    @staticmethod
    def copy_no_broadcast(hive: Hive, user: str):
        posting = HiveFactory._get_posting(hive, user)
        active = HiveFactory._get_active(hive, user)
        keys = []

        if posting:
            keys.append(posting)
        if active:
            keys.append(active)

        return Hive(nobroadcast=True,keys=keys)

    @staticmethod
    def _create_temp_hive_cred(posting: str, active: str = None) -> Hive:
        keys: list[str] = []
        if posting:
            keys.append(posting)
        if active:
            keys.append(active)

        no_broadcast: bool = "true" == HiveFactory._load_env("no_broadcast")

        hive: Hive = Hive(no_broadcast=no_broadcast, keys=keys,node="https://anyx.io/")

        return hive

    @staticmethod
    def _load_env(key: str) -> str:
        return os.getenv(key)

    @staticmethod
    def _get_posting(hive: Hive, user: str):
        try:
            return hive.wallet.getPostingKeyForAccount(user)
        except MissingKeyError:
            return None
    @staticmethod
    def _get_active(hive: Hive, user: str):
        try:
            return hive.wallet.getActiveKeyForAccount(user)
        except MissingKeyError:
            return None
