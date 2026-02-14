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

def inOrder(root):
    if root is None:
        return
    
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

x = build_tree()
inOrder(x)