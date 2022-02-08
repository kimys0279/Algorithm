from collections import defaultdict

def _trie():
    return defaultdict(_trie)

TERMINAL = None

class WordDictionary(object):
    def __init__(self):
        self.trie = _trie()

    def addWord(self, word):
        trie = self.trie
        for letter in word:
            trie = trie[letter]
        trie[TERMINAL]

    def search(self, word, trie=None):
        if trie is None:
            trie = self.trie
        for i, letter in enumerate(word):
            if letter == '.':
                return any(self.search(word[i+1:], t) for t in trie.itervalues())
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return TERMINAL in trie