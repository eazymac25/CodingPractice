class Node(object):
    def __init__(self, val, children=[], word=None):
        self.val = val
        self.word = word
        self.children = {}
    def __repr__(self):
        return str(self.val)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                curr.children[letter] = Node(letter)
                curr = curr.children[letter]
        curr.word = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            child = curr.children.get(letter, None)
            if child is not None:
                curr = child
            else:
                return False
        return curr.word == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for letter in prefix:
            child = curr.children.get(letter, None)
            if child is not None:
                curr = child
            else:
                return False
        return True