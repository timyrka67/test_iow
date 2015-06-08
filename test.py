import json
from random import randint
import sys

with open('input.json', 'r') as f:
    config = json.load(f)

creatives = config["creatives"]


def clean_creatives(creatives):
    clean_creatives_id = []
    clean_creatives = []
    for i in range(0, len(creatives)):
        if creatives[i] not in clean_creatives and creatives[i]["id"] not in clean_creatives_id:
            clean_creatives.append(creatives[i])
            clean_creatives_id.append(creatives[i]["id"])
    return clean_creatives


def find_creative_for_country(creatives, country):
    max_value = []
    for i in range(0, len(creatives)):
        if creatives[i]["country"] == country:
            max_value = creatives[i]
    max_value_winners = max_value
    return max_value_winners


def get_max_value_winners(creatives, country):
    country_for_creatives = find_creative_for_country(creatives, country)
    max_value_winners = [country_for_creatives]
    for i in range(0, len(creatives)):
        if creatives[i]["country"] == country or creatives[i]["country"] == "":
            if max_value_winners[0]["price"] < creatives[i]["price"]:
                max_value_winners = [creatives[i]]
            elif max_value_winners[0]["price"] == creatives[i]["price"]:
                if creatives[i] not in max_value_winners:
                    max_value_winners.append(creatives[i])
    for i in reversed(range(0, len(creatives))):
        if creatives[i]["price"] == max_value_winners[0]["price"]:
            del creatives[i]
    return max_value_winners


def get_equiprobable_choice(winners):
    choice = randint(0, len(winners) - 1)
    return winners[choice]


def get_creatives_from_country(creatives ,country):
    number = 0
    creatives_from = []
    for i in range(0, len(creatives)):
        if creatives[i]["country"] == country:
            number = number + 1
            creatives_from.append(creatives[i])
    return number, creatives_from

def get_winners(creatives, number_of_winners, country):
    winners = []
    creatives = clean_creatives(creatives)
    number_creatives_from, creatives_from = get_creatives_from_country(creatives, country)
    if number_creatives_from > number_of_winners:
        while len(winners) < number_of_winners:
            max_value_winners = get_max_value_winners(creatives, country)
            if number_of_winners - len(winners) <= len(max_value_winners):
                while len(winners) != number_of_winners:
                    winner = get_equiprobable_choice(max_value_winners)
                    winners.append(winner)
                    max_value_winners.remove(winner)
            if number_of_winners - len(winners) > len(max_value_winners):
                while len(max_value_winners) != 0:
                    winner = get_equiprobable_choice(max_value_winners)
                    winners.append(winner)
                    max_value_winners.remove(winner)
        print("Number of winners with unique ad_id", len(winners))
        print("Bellow list:")
        print(winners)
    elif number_creatives_from == number_of_winners:
        print("Number of winners with unique ad_id", len(creatives_from))
        print("Bellow list:")
        print(creatives_from)
    else:
        print("We don't have ", number_of_winners, "unique creatives. We have only: ", number_creatives_from)
        print("Bellow list:")
        print(creatives_from)


if (len(sys.argv) < 3):
    print ("Usage test.py <winners number> <Country>")
else:
    get_winners(creatives, int(sys.argv[1]), sys.argv[2])
