class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def findMaximum(self, root):
        while root.right != None:
            root = root.right
        return root

    def findMinimum(self, root):
        while root.left != None:
            root = root.left
        return root

    def inOrderSuccessor(self, root, val):
        successor = None
        while root is not None:
            if root.data > val:
                successor = root.data
                root = root.left
            else:
                root = root.right
        return successor

    def inOrderPredecessor(self, root, val):
        predecessor = None
        while root is not None:
            if root.data < val:
                predecessor = root
                root = root.right
            else:
                root = root.left
            return predecessor
    
    def inOrderTraversal(self, root):
        if root is not None:
            self.inOrderTraversal(root.left)
            print(root.data, end=' ')
            self.inOrderTraversal(root.right)

    def insertIntoBST(self, root, data):
        if not root:
            return Node(data)

        cur = root

        while True:
            if cur.data < data:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = Node(data)
                    break
            else:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = Node(data)
                    break

        return root

    def deleteNode(self,root,key):
        if root is None:
            return None
        if root.data == key:
            return self.helper(root)
        
        dummy = root

        while root is not None:
            if key < root.data:
                if root.left is not None and root.left.data == key:
                    helperReturnedValue = self.helper(root.left)
                    root.left = helperReturnedValue
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.data == key:
                    helperReturnedValue = self.helper(root.right)
                    root.right = helperReturnedValue
                    break
                else:
                    root = root.right
        return dummy
    
    def helper(self,root):
        #case 1 no left child, return right child
        if root.left is None:
            return root.right
        #case 2 no right child, return left child
        elif root.right is None:
            return root.left
        #case 3 node has both children
        #Store the right child
        rightChild = root.right
        #find the rightmost node in the left subtree
        lastRight = self.findLastRight(root.left)
        #attach the right child to the rightmost node of left subtree
        lastRight.right = rightChild

        return root.left
    
    def findLastRight(self,root):
        if root.right is None:
            return root
        return self.findLastRight(root.right)
    
    
    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True

        if key < root.data:
            
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)






# -------- MAIN --------
bst = BST()
root = bst.root

n = int(input("How many values do you want to insert? "))

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    root = BST().insertIntoBST(root, value)

print("All values inserted successfully!")


# deleteValue = int(input("Enter a value to delete: "))
# root = BST().deleteNode(root, deleteValue)


# # SEARCH
# numberOfSearches = int(input("How many values do you want to search: "))
# for i in range(numberOfSearches):
#     value = int(input(f"Enter value to search {i+1}: "))
#     found = BST().search(root, value)
#     if found:
#         print(f"{value} found in the BST.")
#     else:
#         print(f"{value} not found in the BST.")

bst.inOrderTraversal(root)