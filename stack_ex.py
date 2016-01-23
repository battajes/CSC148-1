# Exercise 3: More Stack Exercises
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# Naina Singh, 1000689098
#
# ---------------------------------------------
from stack import Stack, EmptyStackError


class SmallStackError(Exception):
    pass


def reverse_top_two(stack):
    """ (Stack) -> NoneType

    Reverse the top two elements on stack.
    Raise a SmallStackError if stack has fewer than two elements.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse_top_two(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    
    temp_stack = stack
    try: 
        first = stack.pop()
        second = stack.pop()      
        
    except EmptyStackError: 
        raise SmallStackError
        
    stack.push(first)
    stack.push(second)     
    
    pass


def reverse(stack):
    """ (Stack) -> NoneType

    Reverse all the elements of stack.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    
    temp_stack = stack

    try:     
        while stack.is_empty() == False:
            temp = stack.pop() 
            temp_stack = stack.push(temp)
                    
    except EmptyStackError: 
        pass
            
    stack = temp_stack
                
        
        
    