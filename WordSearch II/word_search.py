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

class Solution(object):
    
    def build_trie(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        found = []
        words = list(set(words))
        trie = self.build_trie(words)
        node = trie.root
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                for word in words:
                    if word not in found and self.dfs_check(board, node, i, j, word):
                        found.append(word)
        return found
    
    def dfs_check(self, board, node, i, j, word):
        if len(word) == 0:
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]):
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        node = node.children.get(tmp)
        if not node:
            return
        flag = self.dfs_check(board, node, i+1, j, word[1:]) or self.dfs_check(board, node, i-1, j, word[1:],) \
        or self.dfs_check(board, node, i, j+1, word[1:]) or self.dfs_check(board, node, i, j-1, word[1:])
        board[i][j] = tmp
        return flag