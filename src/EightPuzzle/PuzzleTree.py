from __init__ import Puzzle

class Node:
    left , right, data = None, None, 0
    def __init__(self, data):
        # initializes the data members
        self.left = None
        self.right = None
        self.data = data
        
class Tree:
    def __init__(self,root):
        self.root = root
    
    