class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = list()
        for word in words:
            letters = [letter for letter in word]
            if sorted(letters) == sorted(self.word):
                matches.append(word)
        return matches
