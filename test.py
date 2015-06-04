import json
from random import randint, shuffle
import unittest

with open('input.json', 'r') as f:
    config = json.load(f)

creatives = config["creatives"]

def get_winners(creatives):
    shuffle(creatives)
    winners = [creatives[0]]
    winners_id = [creatives[0]["id"]]
    winner_country = creatives[0]["country"]
    for i in range(0, len(creatives)):
        if winners[0]["price"] < creatives[i]["price"]:
            winners = [creatives[i]]
            winners_id = [creatives[i]["id"]]
            winner_country = creatives[i]["country"]
        if winners[0]["price"] == creatives[i]["price"]:
            if creatives[i] not in winners and creatives[i]["id"] not in winners_id and creatives[i]["country"] == winner_country or creatives[i]["country"] == "":
                winners.append(creatives[i])
                winners_id.append(creatives[i]["id"])
    return winners


def get_equiprobable_choice(winners):
    choice = randint(0, len(winners)-1)
    return winners[choice]


winners = get_winners(creatives)
print("List of winners:")
print(winners)
print("")
winner = get_equiprobable_choice(winners)
print("One among of winners has been selected equiprobably:")
print(winner)


