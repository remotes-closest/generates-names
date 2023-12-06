import random

class Suffixes:
    _suffixes = ["Corp", "Industries", "Solutions", "Technologies", "Labs"]

    @staticmethod
    def get_random_suffix():
        return random.choice(Suffixes._suffixes)
