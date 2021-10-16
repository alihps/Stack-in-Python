# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 00:27:09 2021

"""

import numpy as np

# Python program to demonstrate stack implementation using a array.

class stack_array(np.ndarray):
    top = 0
    MAX = 0

     # Initializing a stack.
    def __init__(self,n):

        self.MAX = n
        self = np.asarray([None]*n)
      
    # Get the current size of the stack
    def getSize(self):
      return self.top
  
   # Check if the stack is empty
    def isEmpty(self):
      return self.getSize() == 0
    
    # Get the top item of the stack
    def Top(self):
        if self.isEmpty()==True:
            raise Exception("stack is empty")

        return self[self.top-1]
    
    # Push a value into the stack.
    def push(self, value):
        if self.getSize()==self.MAX:
            raise Exception("stack is full")

        self[self.top] = value
        self.top += 1
      
    # Remove a value from the stack and return.
    def pop(self):
      if self.isEmpty():
         raise Exception("stack is empty")
      e = self[self.top-1]
      self[self.top-1] = None
      self.top -= 1
      
      return e
            