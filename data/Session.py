import time
from binascii import hexlify
from typing import List

from beem.blockchain import Blockchain
from beem.exceptions import MissingKeyError
from beemgraphenebase.ecdsasig import sign_message
from beem import Hive

from SM_Framework.SMBotFramework.api.data.SplinterlandsData import BalanceItem
from SM_Framework.SMBotFramework.api.login.LoginApi import LoginApi
from SM_Framework.SMBotFramework.api.login.data.LoginRequest import LoginRequest
from SM_Framework.SMBotFramework.api.login.data.LoginResponse import LoginResponse
from SM_Framework.SMBotFramework.hive.HiveFactory import HiveFactory

# sha256 = hashlib.sha256(bytes(sig_base, "utf-8")).hexdigest()
# sig = hmac.new(bytes(posting, "ascii"), bytes(sha256, "utf-8"), digestmod=hashlib.sha256, ).hexdigest()
# print(len(sha256))
# private_key = ec.derive_private_key(int(base58decode(posting), 16), ec.SECP256K1(), default_backend())
# print(hex(private_key.private_numbers().private_value))
# signature = private_key.sign(bytes(sig_base, "utf-8"), ec.ECDSA(hashes.SHA256()))
# print(signature)
# sk = ecdsa.SigningKey.from_string(int(base58decode(posting), 16), curve=ecdsa.SECP256k1)
# sig = sk.sign(bytes(sha256, "ascii"))
# shout out and thank you @bubke, after wasting a whole evening trying to decode a hive private key into
# some format that "normal" ecdsa libraries could comprehend, I finally stumbled upon your solution
# First successfull login startdate 1639177977881. Thanks!
# PS I'll leave this mess for other peoples entertainment

"""
    Creates and handles a session with splinterlands.
    It stores username, hive connection and further session details
"""


class Session:
    user: str
    timestamp: int
    hive: Hive
    blockchain: Blockchain
    token: str
    response: LoginResponse
    balances: dict = {}

    loginApi: LoginApi

    """
        Creates a session with the given private keys
    """

    @classmethod
    def from_priv_key(cls, posting: str, active: str = None):
        session: Session = cls()
        session.hive = HiveFactory.from_private_key(posting, active)
        session.user = session.hive.wallet.getAccountFromPrivateKey(posting)
        session.blockchain = Blockchain(blockchain_instance=session.hive)
        return session

    @classmethod
    def from_priv_key_override_user(cls, posting: str,user: str, active: str = None):
        session: Session = cls()
        session.hive = HiveFactory.from_private_key(posting, active)
        session.user = user
        session.blockchain = Blockchain(blockchain_instance=session.hive)
        return session

    """
        Creates a session from the .env configuration
    """

    @classmethod
    def from_config(cls, user):
        session: Session = cls()
        session.hive = HiveFactory.build_hive()
        session.user = user
        session.blockchain = Blockchain(blockchain_instance=session.hive)
        return session

    def __init__(self):
        self.loginApi = LoginApi()

    def compute_sig(self, base_string: str):
        sig: str = None
        if self.hive:
            key = self._get_sig_key()
            bytestring_signature = sign_message(base_string, key)
            sig = hexlify(bytestring_signature).decode("ascii")

        return sig

    def create(self):
        timestamp = int(time.time() * 1000)
        sig_base = self.user + str(timestamp)

        sig = self.compute_sig(sig_base)

        request = LoginRequest(self.user, timestamp, sig)
        self.response = self.loginApi.login(request)

        if self.response:
            self.token = self.response.token
            self.timestamp = timestamp
            self._prepare_balances(self.response)
            self.loginApi.auth(self.user, self.token)  #just emulating official site behaviour ?

    """
        Primary use for refreshing balances
    """
    def refresh_session(self):
        self.create()

    def _prepare_balances(self, response):
        self.balances = {}
        if response and response.balances:
            for balance in response.balances:
                self.balances[balance.token] = balance

    def get_balance(self, token: str) -> BalanceItem:
        return self.balances.get(token, BalanceItem())

    def _get_sig_key(self):
        posting_key: str = self.get_posting()
        key: str = None
        if posting_key:
            key = posting_key
        else:
            active_key: str = self.get_active()
            if active_key:
                key = active_key

        return key

    def get_posting(self):
        try:
            return self.hive.wallet.getPostingKeyForAccount(self.user)
        except MissingKeyError:
            return None

    def get_active(self):
        try:
            return self.hive.wallet.getActiveKeyForAccount(self.user)
        except MissingKeyError:
            return None

    def has_posting(self):
        try:
            return len(self.hive.wallet.getPostingKeysForAccount(self.user) or []) != 0
        except MissingKeyError:
            return False

    def has_active(self):
        try:
            return len(self.hive.wallet.getActiveKeysForAccount(self.user) or []) != 0
        except MissingKeyError:
            return False


