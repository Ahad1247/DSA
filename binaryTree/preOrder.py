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

def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

x = build_tree()
preOrder(x)