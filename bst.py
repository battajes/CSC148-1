# BinarySearchTree class
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
#
# ---------------------------------------------
"""Binary Search Tree class.

This is the recursive implementation of a binary search tree data structure
from Week 8 of the course.

Note that this class is conceptually similar to a general tree,
but has separate left and right attributes rather than a list of trees.

This contains all of the BST methods from the week:
lecture material, labs, and the exercise.
"""


class EmptyBSTError:
    """Exception class used when deleting an item from an empty BST."""
    pass


class EmptyValue:
    """As usual, use this to represent the root value of an empty BST."""
    pass


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and < all items stored in its right subtree.

    Attributes:
    - root (object): the root value stored in the BST, or EmptyValue
                     if the tree is empty
    - left (BinarySearchTree): the left subtree, or None if the tree is empty
    - right (BinarySearchTree): the right subtree, or None if the tree is empty
    """
    def __init__(self, root=EmptyValue):
        """ (BinarySearchTree, object) -> NoneType

        Create a new binary search tree with a given root value.
        An empty BST has its root attribute set to EmptyValue.
        """
        self.root = root    # root value
        if self.is_empty():
            # Set left and right to nothing,
            # because this is an empty binary tree.
            self.left = None
            self.right = None
        else:
            # Set left and right to be new empty trees.
            # Note that this is different than setting them to None!
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

    def is_empty(self):
        """ (BinarySearchTree) -> bool

        Return True if this tree is empty.
        Empty trees are identified by having root value EmptyValue.
        """
        return self.root is EmptyValue

    def print_tree(self, depth=0):
        """ (BinarySearchTree, int) -> NoneType

        Print all of the items in this tree,
        where the root is printed before its left and right subtrees,
        and every value is indented to show its depth.
        """
        if not self.is_empty():
            print(depth * '  ' + str(self.root))
            self.left.print_tree(depth + 1)
            self.right.print_tree(depth + 1)

    def __contains__(self, item):
        """ (BinarySearchTree, object) -> bool
        Return True if this tree contains item.
        """
        if self.is_empty():
            return False
        elif item == self.root:
            return True
        elif item < self.root:
            return self.left.__contains__(item)
            # Or, return item in self.left
        else:
            return self.right.__contains__(item)

    # LAB 8
    def count_all(self, item):
        """ (BinarySearchTree, object) -> int
        Return the number of times item appears in this tree.
        (Return 0 if this tree is empty.)
        """
       
        if self.is_empty():

            return 0

        elif self.root == item:

            return 1 + self.right.count_all(item)

        elif self.root > item:

            return self.left.count_all(item)

        else:

            return self.right.count_all(item)

    def range(self, low, high):
        """ (BinarySearchTree, object, object) -> int

        Precondition: low and high can be compared with items in this tree.

        Return the number of items in this tree whose value is
        between low and high, inclusive.
        """
        if self.is_empty():
         
            return 0
         
        elif self.root == low:
             
            return 1 + self.right.range(low, high)
        
        elif self.root == high:
            return 1 + self.left.range(low,high)
        elif self.root < low:
             
            return self.right.range(low, high)
 
        elif self.root > high:
             
            return self.left.range(low, high)
         
        elif (low < self.root) and (self.root < high):
 
            return 1 + self.right.range(low, high) + self.left.range(low, high)
        

    # Mutating methods

    def insert(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Insert item into this tree in the correct location.
        Do not change positions of any other nodes.
        """
        if self.is_empty():
            # Make new leaf node.
            # Note that self.left and self.right cannot be None if the
            # tree is non-empty! (This is one of our invariants.)
            self.root = item
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        elif item <= self.root:
            self.left.insert(item)
        else:
            self.right.insert(item)

    def delete(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Remove item from this tree.
        Do nothing is this tree doesn't contain item.
        """
        if not self.is_empty():
            if self.root == item:
                self.delete_root()
            elif item < self.root:
                self.left.delete(item)
            else:
                self.right.delete(item)

    def delete_root(self):
        """ (BinarySearchTree) -> NoneType
        Remove the root node of this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        else:
            self.root = self.left.extract_max()

    def extract_max(self):
        """ (BinarySearchTree) -> object

        Remove and return the maximum item stored in this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        elif self.right.is_empty():
            temp = self.root
            # Copy left subtree to self, because root node is removed.
            # Note that self = self.left does NOT work!
            self.root = self.left.root
            self.right = self.left.right
            self.left = self.left.left
            return temp
        else:
            return self.right.extract_max()

    # LAB 8 - complete extract_min and then fix delete_root
    def extract_min(self):
        """ (BinarySearchTree) -> object
        Remove and return the minimum item stored in this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        pass

    # EXERCISE 8
    def list_range(self, low, high):
        """ (BinarySearchTree, object, object) -> list

        Precondition: low and high can be compared with items in this tree.

        Return a sorted list of the items in this tree whose value is
        between low and high, inclusive.
        Note: the returned list should include any duplicates
        that appear in this tree.
        """
        if self.is_empty(): 
            return [] 
        elif self.root == low or self.root == high:
            a = self.root
            lst = [] 
            lst.append(a)
            b = self.right.list_range(low, high)
            for val in b: 
                lst.append(val)
            return lst
        elif self.root < high and self.root > low: 
            lst = [] 
            b =self.right.list_range(low, high)
            c= self.left.list_range(low,high)
            for val in c: 
                lst.append(val)
            a = self.root
            lst.append(a)
            for val in b: 
                lst.append(val)
            return lst
        elif self.root >high: 
            return self.left.list_range(low, high)
        elif self.root < low: 
            return self.right.list_range(low,high)
       
            
            
            
            
        
        