"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finds random word from dictionary"""
    def __init__(self, path):
        """Reads dictionary and returns number of items read"""
        word_file = open(path)
        self.words = self.parse(word_file)
        print(f"{len(self.words)} words read")

    def parse(self, word_file):
        """Strips words of extra characters and makes list"""
        return [word.strip() for word in word_file]

    def random(self):
        """Returns random word"""
        return random.choice(self.words)
