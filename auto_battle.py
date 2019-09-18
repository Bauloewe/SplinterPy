from Requests import Requests
from time import sleep
import time
from api import Api
import json
import pickle
from SMBotTimer import SMBotTimer
import datetime as dt
from datetime import timezone
import random
import math


bot_set = dict()

with open('settings.json', 'r') as file:
    bot_set = json.loads(file.read())

#Insert your private key here, however you like, plain text, encrypted, wallet etc
r = Requests("PRIVATE POSTING KEY")
player = bot_set["player"]

api = Api()
bot_timer = SMBotTimer(bot_set["default_sleep"],bot_set["start_time"],bot_set["end_time"])

sm_dict = dict()


quest_details = dict()
for x in api.settings()["quests"]:
    quest_details[x["name"]] = x

trx = ""

while True:



    quest_color = None

    try:
        x = api.get_player_quests(player)
        for quest in x:
            if not quest["claim_date"]:
                quest_color = quest_details[quest["name"]]["data"]["color"]

                if quest["completed_items"]/quest["total_items"] >= 1 and not quest["claim_trx_id"]:
                    r.claim_reward(player,quest["id"],"quest")
                    quest_color = None
            else:
                created_date = quest['created_date'].replace('Z', '')
                created_date = dt.datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%f")
                reset_time = created_date + dt.timedelta(hours=23)

                if dt.datetime.now() >= reset_time:
                    r.start_quest(player,"daily")
    except:
        quest_color = None

    print("Searching match")
    r.find_match(player,"Ranked")

    sleep(3)
    trx = r.find_match_transaction(player,trx)

    if trx == "":
        continue

    status = api.get_battle_status(trx)

    if "Error" in status:
        print("Transaction error")
        sleep(120)
        continue

    while not status["opponent_player"]:
        try:
            status = api.get_battle_status(trx)
        except Exception as e:
            print(e)
            print("Error while retrieving battle status")

    print("Challenging "+status["opponent_player"])

    if status["inactive"]:
        inactive = status["inactive"].split(",")
    else:
        inactive = []

    ruleset = status["ruleset"].split("|")

    opponent = status["opponent_player"] if status["opponent_player"] != player else status["player"]
    opponent_teams = dict()

    #TODO create your teams here
    team = ["UID_Summoner","UID_1","UID_2","UID_..","UID_n"]
    r.submit_team(trx,team,player)
    res = api.get_battle_result(trx)
    while type(res) is str:
        sleep(10)
        res = api.get_battle_result(trx)


    print("\nThe winner is "+ json.loads(res["details"])["winner"]+"\n")
    print(api.get_player_details(player)["rating"])

    with open("rank.csv", "a") as myfile:
        myfile.write(str(api.get_player_details(player)["rating"])+",")

    print("sleeping")

    if quest_color:
        sleep(10)
    else:
        sleep(bot_timer.default)

