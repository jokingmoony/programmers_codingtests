# https://programmers.co.kr/learn/courses/30/lessons/60060
class TrieNode:
    def __init__(self, val, leaf=False):
        self.val = val
        self.children = {}
        self.cnt = 0
        self.leaf = leaf
        
    
class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        
    def insert(self, string):
        cur = self.root
        
        for c in string:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur.cnt += 1
            cur = cur.children[c]
        cur.cnt += 1
        cur.leaf = True
        
    def search(self, prefix):
        ret = 0
        cur = self.root
        
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return 0
            
        node_list = []
        for c in cur.children:
            node_list.append(cur.children[c])
        
        for i in node_list:
            ret += i.cnt
        
        return ret


def solution(words, queries):
    answer = []

    tries = [ Trie() for i in range(10000) ]
    r_tries = [ Trie() for i in range(10000) ]
    
    for w in words:
        tries[len(w)-1].insert(w)
        r_tries[len(w)-1].insert(w[::-1])
        
    for query in queries:
        flag = False
        if query[0] == '?' and query[-1] != '?':
            flag = True
            query = query[::-1]
            
        pre = 0
        for idx, c in enumerate(query):
            if c == '?':
                pre = idx
                break
        
        if flag:
            answer.append(r_tries[len(query)-1].search(query[:pre]))
        else:
            answer.append(tries[len(query)-1].search(query[:pre]))
            
    return answer