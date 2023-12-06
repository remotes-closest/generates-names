from prefixes import Prefixes
from suffixes import Suffixes
import random

class NameGenerator:
    def __init__(self):
        random.seed()  # Seed the random number generator

    def generate_name(self):
        # Logic to combine random prefixes and suffixes
        return Prefixes.get_random_prefix() + Suffixes.get_random_suffix()
