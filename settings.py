import configparser
import os

def get_starting_money():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    starting_money = float(os.getenv("MY_MONEY", config.get("Game", "starting_money")))
    return starting_money