# Exercise 1, Task 1: Runtime Errors
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
# <Naina Sitara Singh>,<1000689098>  
#
# ---------------------------------------------
"""Exercise 1, Task 1: Runtime Errors."""


def bad_type():
    """When run, produces a TypeError."""
    return 'high' + 5


def bad_name():
    """When run, produces a NameError."""
    return 'in' in five  


def bad_attribute():
    """When run, produces an AttributeError."""
    dict = { 1:'blue'} 
    return dict.append(2)
    


def bad_index():
    """When run, produces an IndexError."""
    L = [1,2,3] 
    return L[4]


def bad_key():
    """When run, produces a KeyError."""
    dict = { 'yellow': 'blue'}
    dict[2]
    
def bad_zero():
    """When run, produces a ZeroDivisionError."""
    return 11/0

def bad_import():
    """When run, produces an ImportError."""
    import new.py 
    