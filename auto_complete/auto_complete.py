# https://programmers.co.kr/learn/courses/30/lessons/17685

class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
            curr.cnt += 1
    
    def search(self, word):
        curr = self.root
        cnt = 0
        
        for w in word:
            cnt += 1
            if w in curr.children:
                curr = curr.children[w]
            if curr.cnt == 1:
                break
        return cnt

def solution(words):
    
    answer = 0
    trie = Trie()
    
    for word in words:
        trie.add(word)
    
    for word in words:
        answer += trie.search(word)
    
    return answer
