"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Find random words from dictionary file"""
    def __init__(self, file):
        dict_file = open(file)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")


    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
