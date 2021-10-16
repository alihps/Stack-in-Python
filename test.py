# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 00:31:13 2021

"""

import stack_array as sa
a = sa.stack_array(10)
print(a)
print(a.getSize())
print(a.isEmpty())
print(a.top)
print(a.MAX)
print(a.Top())
a.push(3)
a.pop()

import stack_linked_list as sll
stack = sll.stack_linked_list()
for i in range(1, 11):
   stack.push(i)
print(f"Stack: {stack}")
 
for _ in range(1, 6):
   remove = stack.pop()
   print(f"Pop: {remove}")
print(f"Stack: {stack}")