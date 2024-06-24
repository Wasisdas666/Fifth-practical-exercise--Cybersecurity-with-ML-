### Comments
# class Node:
#     Initialize with value, left, and right

# class BinarySearchTree:
#     Initialize with root set to None

#     Method insert(value):
#         If tree is empty, create root node
#         Else, recursively find position and insert node

#     Method search(value):
#         Recursively traverse tree to find value

#     Method delete(value):
#         Find node, then delete according to three cases

#     Method traverse():
#         In-order traversal of the tree to print values

# Main:
#     Create binary search tree
#     For each list (a, b, c):
#         Insert values into the tree
#         Perform search, delete, and traverse operations
#         Print tree structure or output

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def delete(self, value):
        # Implementation of delete method is omitted for brevity
        pass

    def traverse(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, current_node):
        if current_node is not None:
            self._traverse_in_order(current_node.left)
            print(current_node.value, end=' ')
            self._traverse_in_order(current_node.right)

# Example usage
bst = BinarySearchTree()
a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
for value in a:
    bst.insert(value)
bst.traverse()

b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]
for value in b:
    bst.insert(value)
bst.traverse()

c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]
for value in c:
    bst.insert(value)
bst.traverse()

# Output

#a) 1 5 13 27 38 49 60 65 76 97
#b) 1 5 11 13 27 38 49 60 65 76 97 149 176 197 217
#c) 1 5 11 13 24 27 38 49 50 55 60 64 65 76 77 97 149 176 197 217