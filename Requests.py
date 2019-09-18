import time
import json
from time import sleep
from steem import Steem
from steem.blockchain import Blockchain
from api import Api
import string
import hashlib

from secrets import choice

class Requests:

    def __init__(self,private_posting_key):
        self.s = Steem(keys=[private_posting_key])
        self.b = Blockchain(steemd_instance=self.s)
        self.api = Api()
        self.settings = self.api.settings()

    def get_current_block_num(self):
        return self.b.get_current_block_num()

    def find_match(self,name,type,tournament_id=None,round=0):
        if type == "Ranked:":
            json_data = {"match_type": type}
        elif type == "Tournament":
            json_data = {"match_type": type,"settings":{"tournament_id":tournament_id,"round":round}}
        else:
            json_data = {"match_type": type}

        self.s.custom_json('sm_find_match', json_data, required_posting_auths=[name])

    def find_match_transaction(self,player,old_trx):
            #TODO add break condition, e.g. 5 minutes or validity block
            while True:
                try:
                    block_num = self.b.get_current_block_num()
                    for r in self.api.get_from_block(block_num):
                        if r["type"] == "find_match":
                            if r["id"] != old_trx:
                                if r["player"] == player:
                                    print(r["id"])
                                    return r["id"]

                except:
                    print("Error while trying to get current block")

    def enter_tournament(self, id, name):
        json_data = {"tournament_id": id,"signed_pw":""}

        self.s.custom_json('sm_enter_tournament', json_data, required_posting_auths=[name])

    def tournament_checkin(self, id, name):
        json_data = {"tournament_id": id,"signed_pw":""}

        self.s.custom_json('sm_tournament_checkin', json_data, required_posting_auths=[name])

    def submit_team(self, trx_id, team, name):
        """
        Submits a Steem Monsters team for the given match search transaction
        :param trx_id: search transaction id
        :param team: list of UID's corresponding to Monsters (Summoner at index 0, Remaining team 1-n
        :param name: player name
        """
        secret = self.generate_key()
        hash = self.generate_team_hash(team[0],team[1:],secret)

        json_data = {"trx_id": trx_id,"team_hash":hash, "summoner": team[0], "monsters": team[1:], "secret": secret}

        self.s.custom_json('sm_submit_team', json_data, required_posting_auths=[name])

    def generate_key(self,length=10):
        return ''.join(choice(string.ascii_letters + string.digits) for i in range(length))


    def generate_team_hash(self,summoner, monsters, secret):
        m = hashlib.md5()
        m.update((summoner + ',' + ','.join(monsters) + ',' + secret).encode("utf-8"))
        team_hash = m.hexdigest()
        return team_hash

    def open_card_pack(self,player, edition):
        """
        Opens a card pack and prints the transaction details

        Parameters:
        player (String): Name of the player
        edition (int): open pack of edition n, e.g. 1 for beta
        """

        self.s.custom_json("sm_open_pack",{ "edition": edition},required_posting_auths=[player])
        while True:
            for r in self.api.get_from_block(self.b.get_current_block_num()):

                if r["type"] == "open_pack":

                    if r["player"] == player:
                        print(r)
                        return r["id"]

    def claim_reward(self,name,quest_id,type):

        json_data = {"type": type ,"quest_id":quest_id}

        self.s.custom_json('sm_claim_reward', json_data, required_posting_auths=[name])

    def start_quest(self,name,type):

        json_data = {"type": type}

        self.s.custom_json('sm_start_quest', json_data, required_posting_auths=[name])
