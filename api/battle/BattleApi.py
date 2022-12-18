import hashlib
import json
import string
from secrets import choice
from typing import List

import requests

from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.battle.BattleAdapter import BattleAdapter
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_BATTLE_RESULTS, GET_BATTLE_STATUS, \
    POST_BATTLE_TRX, BASE_BATTLE, GET_BATTLE_HISTORY
from SM_Framework.SMBotFramework.api.data.SplinterlandsData import BattleHistory
from SM_Framework.SMBotFramework.data.Session import Session
from SM_Framework.SMBotFramework.hive.HiveFactory import HiveFactory


class BattleApi:
    baseCaller: BaseApiCaller
    adapter: BattleAdapter

    def __init__(self):
        self.baseCaller = BaseApiCaller()
        self.adapter = BattleAdapter()

    def get_battle_result(self, battle_id: str, session: Session = None):
        url: str = BASE_API2 + GET_BATTLE_RESULTS
        request = self.adapter.adapt_get_battle(session, battle_id)
        return self.baseCaller.call_get(url, request)

    def get_battle_status(self, battle_id: str, session: Session = None):
        url: str = BASE_API2 + GET_BATTLE_STATUS
        request = self.adapter.adapt_get_battle(session, battle_id)
        return self.baseCaller.call_get(url, request)

    def get_battle_history2(self,player: str, session: Session = None):
        url: str = BASE_API2 + GET_BATTLE_HISTORY;
        request = self.adapter.adapt_get_battle_history2(player, session)
        return BattleHistory(self.baseCaller.call_get(url, request))

    def broadcast_find_match(self, session: Session, match_type: str, on_chain: bool):
        hive = session.hive if on_chain else HiveFactory.copy_no_broadcast(session.hive, session.user)

        trx_id = None
        trx: dict = hive.custom_json("sm_find_match", json_data={"match_type": match_type},
                                     required_posting_auths=[session.user])
        if not on_chain:
            trx = self.post_battle_transaction(trx)
            if trx["success"]:
                trx_id = trx["id"]
        else:
            trx_id = trx["trx_id"]
        return trx_id

    def broadcast_submit_team(self, session, trx_id: str, team: List[str], on_chain, secret: str):
        hive = session.hive if on_chain else HiveFactory.copy_no_broadcast(session.hive, session.user)

        hash = self.generate_team_hash(team[0], team[1:], secret)

        request = {"trx_id": trx_id, "team_hash": hash}
        trx: dict = hive.custom_json("sm_submit_team", json_data=request,
                                     required_posting_auths=[session.user])
        trx_id = None
        if not on_chain:
            trx = self.post_battle_transaction(trx)
            if trx["success"]:
                trx_id = trx["id"]
        else:
            trx_id = trx["trx_id"]

        return trx_id, hash

    def broadcast_reveal_team(self, session: Session, team: List[str], secret: str, on_chain: bool, trx_id, hash):
        hive = session.hive if on_chain else HiveFactory.copy_no_broadcast(session.hive, session.user)

        request = {"trx_id": trx_id, "team_hash": hash, "summoner": team[0], "monsters": team[1:],
                   "secret": secret}
        trx: dict = hive.custom_json("sm_team_reveal", json_data=request,
                                     required_posting_auths=[session.user])

        trx_id = None
        if not on_chain:
            trx = self.post_battle_transaction(trx)
            if trx["success"]:
                trx_id = trx["id"]
        else:
            trx_id = trx["trx_id"]

        return trx_id

    def generate_key(self, length=10):
        return ''.join(choice(string.ascii_letters + string.digits) for i in range(length))

    def generate_team_hash(self, summoner, monsters, secret):
        m = hashlib.md5()
        m.update((summoner + ',' + ','.join(monsters) + ',' + secret).encode("utf-8"))
        team_hash = m.hexdigest()
        return team_hash

    def post_battle_transaction(self, trx: dict):
        url: str = BASE_BATTLE + POST_BATTLE_TRX
        trx: str = json.dumps(trx)
        return requests.post(url, data={"signed_tx": trx}).json()
