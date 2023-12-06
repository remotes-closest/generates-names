import random

class Prefixes:
    _prefixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

    @staticmethod
    def get_random_prefix():
        return random.choice(Prefixes._prefixes)
