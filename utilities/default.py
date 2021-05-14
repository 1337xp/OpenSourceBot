import random
import json

def config(filename: str = "configuration"):
    """ Get default configuration file """
    try:
        with open(f"{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("Could not find JSON file.")


def random_colour():
    return random.randint(0, 0xffffff)
