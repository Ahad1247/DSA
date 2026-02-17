from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    data = int(input("Enter the data: "))

    if data == -1:
        return None

    root = Node(data)

    print("Enter data for inserting in left:")
    root.left = build_tree() 

    print("Enter data for inserting in right:")
    root.right = build_tree()

    return root

def levelOrder(root):
    ans = []
    if root is None:
        return ans
    
    q = deque([root])
 
    while q:
        size = len(q)
        level = []

        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.data)
        ans.append(level)
    return ans

    

x = build_tree()
levels = levelOrder(x)

totalLevels = len(levels)

for level in levels:
    print(level)
    