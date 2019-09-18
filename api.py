import time
import requests


class Api(object):
    """ Access the steemmonsters API
        https://github.com/holgern/steemmonsters
    """
    __url__ = 'https://steemmonsters.com/'

    def get_card_details(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            try:
                response = requests.get(self.__url__ + "cards/get_details")
                if str(response) != '<Response [200]>':
                    time.sleep(2)
                cnt2 += 1
            except:
                pass
        return response.json()

    def get_quests(self,name):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            try:
                response = requests.get(self.__url__ + "players/quests?username="+name)
                if str(response) != '<Response [200]>':
                    time.sleep(2)
                cnt2 += 1
            except:
                pass
        return response.json()

    def get_purchases_stats(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/stats")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def settings(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "settings")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def players_leaderboard(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/leaderboard")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def find_cards(self, card_ids):
        if isinstance(card_ids, list):
            card_ids_str = ','.join(card_ids)
        else:
            card_ids_str = card_ids
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "/cards/find?ids=%s" % card_ids_str)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_upcoming_tournaments(self, player=None, token=None):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            if player is None and token is None:
                response = requests.get(self.__url__ + "tournaments/upcoming")
            elif token is None:
                response = requests.get(self.__url__ + "tournaments/upcoming?username=%s" % player)
            else:
                response = requests.get(self.__url__ + "tournaments/upcoming?token=%s&username=%s" % (token, player))
            cnt2 += 1
        return response.json()

    def get_inprogress_tournaments(self, player=None, token=None):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            if player is None and token is None:
                response = requests.get(self.__url__ + "tournaments/in_progress")
            elif token is None:
                response = requests.get(self.__url__ + "tournaments/in_progress?username=%s" % (player))
            else:
                response = requests.get(self.__url__ + "tournaments/in_progress?token=%s&username=%s" % (token, player))
            cnt2 += 1
        return response.json()

    def get_completed_tournaments(self, player=None, token=None):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            if player is None and token is None:
                response = requests.get(self.__url__ + "tournaments/completed")
            elif token is None:
                response = requests.get(self.__url__ + "tournaments/completed?username=%s" % (player))
            else:
                response = requests.get(self.__url__ + "tournaments/completed?token=%s&username=%s" % (token, player))
            cnt2 += 1
        return response.json()

    def get_tournament(self, player, uid, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "tournaments/find?id=%s&token=%s&username=%s" % (uid, token, player))
            cnt2 += 1
        return response.json()
    def get_tournament_details(self,id):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "tournaments/find?id="+id)

            cnt2 += 1
        return response.json()

    def get_tournament_round_lineup(self,id,rnd):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "tournaments/battles?id="+id+"&round="+str(rnd))

            cnt2 += 1
        return response.json()

    def get_open_all_packs(self, player, edition, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/open_all_packs/%s?player=%s&edition=%d&token=%s&username=%s" % (player, player, edition, token, player))
            cnt2 += 1
        return response.json()

    def get_open_packs(self, uuid, player, edition, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/open_pack/%s?player=%s&edition=%d&token=%s&username=%s" % (uuid, player, edition, token, player))
            cnt2 += 1
        return response.json()

    def get_cards_packs(self, player, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            try:
                response = requests.get(self.__url__ + "cards/packs/%s?token=%s" % (player, token))
            except:
                pass
            cnt2 += 1
        return response.json()

    def get_collection(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            try:
                response = requests.get(self.__url__ + "cards/collection/%s" % player)
            except:
                pass
            cnt2 += 1
        return response.json()

    def get_player_login(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/login?name=%s" % player)
            cnt2 += 1
        return response.json()

    def get_player_details(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            try:
                response = requests.get(self.__url__ + "players/details?name=%s" % player)
            except:
                pass
            cnt2 += 1
        return response.json()
  
    def get_player_quests(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/quests?username=%s" % player)
            cnt2 += 1
        return response.json()

    def get_for_sale(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_purchases_settings(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/settings")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()
    
    def get_purchases_status(self, uuid):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/status?id=%s" % uuid)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_from_block(self, block_num):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "transactions/history?from_block=%d" % block_num)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_transaction(self, trx):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "transactions/lookup?trx_id=%s" % trx)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_cards_stats(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/stats")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_for_sale_by_card(self, card_detail_id, gold, edition):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale_by_card?card_detail_id=%d&gold=%s&edition=%d" % (card_detail_id, gold, edition))
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_for_sale_grouped(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale_grouped")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_status(self, market_id):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/status?id=%s" % market_id)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_battle_history(self, player="%24top"):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            try:
                response = requests.get(self.__url__ + "battle/history?player=%s" % player)
                if str(response) != '<Response [200]>':
                    time.sleep(1)
                cnt2 += 1
            except:
                pass
        return response.json()

    def get_battle_result(self, ids):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            try:
                response = requests.get(self.__url__ + "battle/result?id=%s" % ids)
                if str(response) != '<Response [200]>':
                    time.sleep(1)
                cnt2 += 1
            except:
                pass
        return response.json()

    def get_battle_status(self, ids):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            try:
                response = requests.get(self.__url__ + "battle/status?id=%s" % ids)
                if str(response) != '<Response [200]>':
                    time.sleep(1)
                cnt2 += 1
            except:
                pass
        return response.json()

    def get_player_balances(self,player):
        response = ""
        cnt = 0
        while str(response) != '<Response [200]>' and cnt < 20:
            try:
                response = requests.get(self.__url__ + "players/balances?username=%s" % player)
                if str(response) != '<Response [200]>':
                    time.sleep(1)
                cnt += 1
            except:
                pass
        return response.json()

    def get_dec_rec_rate(self,player, block_num):
        """


        :param player: name of player
        :param block_num: current block number
        :return: dark energy recovery rate in range [0-1]
        """
        balances = self.get_player_balances(player)

        ecr_balance = dict()
        for balance in balances:
            if balance["token"] == "ECR":
                ecr_balance = balance
                break
        settings = self.settings()
        return (((block_num - ecr_balance["last_reward_block"])*settings["dec"]["ecr_regen_rate"])+ecr_balance["balance"])/10000
