# Tree class
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
"""Tree class.

This is the recursive implementation of a tree data structure
from Week 7 of the course.

Note the relationship between this class and LinkedListRec;
the only major difference is that self.rest has been replaced
by self.subtrees to handle multiple recursive subparts.

This contains all of the linked list methods from the week:
lecture material, labs, and the exercise.
"""


class EmptyValue:
    """As with linked lists, we'll use this class
    as a dummy class to signify the root of an empty tree.
    """
    pass


class Tree:
    """A recursive tree data structure.

    Attributes:
    - root (object): the item stored at the root of the tree,
                     or EmptyValue if the tree is empty.
    - subtrees (list of Tree): a list of all subtrees of the tree
    """

    def __init__(self, root=EmptyValue):
        """ (Tree, object) -> NoneType

        Create a new tree with given root value.
        If no root value is passed in, the tree is empty
        (this is signified by setting the root value to EmptyValue).
        A new tree always has no subtrees.
        """
        self.root = root
        self.subtrees = []

    def is_empty(self):
        """ (Tree) -> bool
        Return True if self is empty.
        """
        return self.root is EmptyValue

    def add_subtrees(self, new_trees):
        """ (Tree, list of Tree) -> NoneType
        Add the trees in new_tree as subtrees of this tree.
        """
        self.subtrees = self.subtrees + new_trees

    def size(self):
        """ (Tree) -> int
        Return the number of nodes contained in this tree.
        """
        if self.is_empty():
            return 0
        else:
            size = 1
            for subtree in self.subtrees:
                size += subtree.size()
            return size

    def print_tree(self):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees.
        """
        if not self.is_empty():
            # This prints the root item before all of the subtrees.
            print(self.root)
            for subtree in self.subtrees:
                subtree.print_tree()

        # Or alternately, simply call
        # self.print_tree_indent()

    def print_tree_indent(self, depth=0):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees,
        and every value is indented to show its depth.
        """
        if not self.is_empty():
            print(depth * '  ' + str(self.root))
            for subtree in self.subtrees:
                subtree.print_tree_indent(depth + 1)

    # Mutating methods

    def delete_item(self, item):
        """ (Tree, object) -> bool
        Delete *one* occurrence of item from this tree.
        Return True if item was deleted, and False otherwise.
        """
        if self.is_empty():
            return False
        else:
            if self.root == item:
                self.delete_root()
                return True
            else:
                for subtree in self.subtrees:
                    # Try to delete item from current subtree
                    # If it works, return!
                    if subtree.delete_item():
                        return True
                return False

    def delete_root(self):
        """ (Tree) -> NoneType
        Remove the root item of this tree.
        """
        if self.subtrees == []:
            # Base case when empty or just one node
            self.root = EmptyValue
        else:
            # Note: this removes a whole subtree from
            # self.subtrees!
            temp = self.subtrees.pop()
            self.root = temp.root
            self.subtrees = self.subtrees + temp.subtrees

    # ------- Lab 7 methods -------
    def __contains__(self, item):
        """ (Tree, object) -> bool
        Return True if item is in this tree.
        """
           # base case
        if self.is_empty():
            return False
        
        elif item == self.root:
            return True
        
        else:
            for subtree in self.subtrees:
                if subtree.__contains__(item):
                    return True
            
            return False
                       
    def get_branching_factor(self):
        """ (Tree) -> int
        Return the average branching factor of this tree.
        Remember to ignore all 0's coming from leaves in
        this calculation.
        Return 0 if this tree is empty or consists of just
        a single root node.
        """

        if self.is_empty():
            return 0 
        else: 
            (a,b) = tree2.get_branching_factor_helper()
            if self.size ==1: 
                return 0 
            else:
                return a/b
        pass

    def get_branching_factor_helper(self):
        """ (Tree) -> (int, int)
        Return a tuple (x,y) where
        x is the total branching factor of all non-leaf nodes in this tree, and
        y is the total number of non-leaf nodes in this tree.
        """
        if self.subtrees == [] and self.root is EmptyValue:
            x = 0
            y = 0
            return (x,y)
        else:
            x = 1
            y = 1
            for subtree in self.subtrees:
                a = subtree.size() 
                if a > 1:
                    x += subtree.size()
                    y += 1
                    
                
        return (x,y)   
        
        


    # Lab Task 2 - Insertion
    # The following line of code imports the module random
    import random
    # Use the function randint as follows:
    # >>> random.randint(1, 3)
    # 2  # Returns a random number between 1 and 3

    def insert(self, item):
        """ (Tree, object) -> NoneType
        Insert item into this tree using the algorithm from the lab handout.
        """
        if self.is_empty():
            self.root = item
        elif self.root is not EmptyValue and self.subtrees == []:
            a = [Tree(item)]
            self.add_subtrees(a)
        else:
            num = random.randint(1,3)
            if num == 3:
                b = [Tree(item)]
                self.add_subtrees(b)
            else:
                n = 0
                for subtree in self.subtrees:
                    n += 1
                n_random = random.randint(1,n)
                self.subtrees[n_random - 1].insert(item)

    # ------- Exercise 7 -------

    def __eq__(self, other):
        """ (Tree, Tree) -> bool

        Return True if this tree and the other tree are equal trees.
        """
        if self.is_empty() and other.is_empty(): 
            return True 
        else:    
            if self.root == other.root: 
                if self.subtrees == [] and other.subtrees == []: 
                    return True 
    
                else: 
            #if self.root == other.root and self.subtrees == other.subtrees: 
                #return True 
            #else:
                    return self.subtrees.__eq__(other) 
            else:
                return False
