#Implement Stacks using Lists
# create a stack names as Stackedlist. Insert Element 25, 20, 10, 5. POp 25,20 insert 15
#insert 20 , 25 . print stack. Pop  all elements.Insert elemnt 50 . print list
from inspect import stack


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items.clear()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items