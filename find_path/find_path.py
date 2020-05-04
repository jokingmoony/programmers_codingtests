# https://programmers.co.kr/learn/courses/30/lessons/42892


# for remove recursion limit
from sys import setrecursionlimit 
setrecursionlimit(10000000)


class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val, coord):
        if self.root == None:
            self.root = Node(val, *coord)
        else:
            curr = self.root

            while True:
                if curr.x > coord[0]:
                    if curr.left == None:
                        curr.left = Node(val, *coord)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = Node(val, *coord)
                        break
                    else:
                        curr = curr.right

    @staticmethod
    def pre_order(answer, node):
        if node == None:
            return None
        answer.append(node.val)
        Tree.pre_order(answer, node.left)
        Tree.pre_order(answer, node.right)

    @staticmethod
    def post_order(answer, node):
        if node == None:
            return None
        Tree.post_order(answer, node.left)
        Tree.post_order(answer, node.right)
        answer.append(node.val)


def solution(nodeinfo):
    answer = []

    nodes = [(i+1, coord) for i, coord in enumerate(nodeinfo)]
    nodes.sort(key=lambda x : x[1][1], reverse=True)
    b_tree = Tree()
    for node in nodes:
        b_tree.add(node[0], node[1])

    pre_list = []
    post_list = []
    b_tree.pre_order(pre_list, b_tree.root)
    b_tree.post_order(post_list, b_tree.root)
    answer.append(pre_list)
    answer.append(post_list)
    return answer