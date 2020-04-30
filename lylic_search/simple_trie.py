# simple implementation of trie node

class TrieNode:
	""" trie node """
    def __init__(self):
		"""
		cnt : count of children leaf node
		children : dictionary of children node
		leaf : leaf node
		"""
        self.cnt = 0
        self.children = {}
        self.leaf = False
    
class Trie:
	""" Trie tree """
    def __init__(self):
		"""
		root : TrieNode root node
		"""
        self.root = TrieNode()
    
    def insert(self, string):
		"""
		insert string to the Trie tree
		"""
        cur = self.root
        
        for c in string:
			# if c is not in the children then make new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur.cnt += 1
            cur = cur.children[c]
        
        cur.leaf = True
    
    def search(self, string):
		"""
		search string in the Trie tree
		"""
        cur = self.root
        
		# if character is not in the children dictionary the return False
        for c in string:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
		# if current node is leaf then find the key else not find
        if cur.leaf == True:
            return True
        else:
            return False
