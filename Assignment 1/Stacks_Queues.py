"""
Challenge: Implement the Stack class from scratch
(do not use your language’s standard stack or queue library/package
 methods). In this challenge, your Stack will only accept
 Integer values. Implement the following methods:
"""

class Stack:
    def __init__(self):
        self.items = []

    # check if no element in stack
    def isEmpty(self):
        return self.items == []

    def top(self):
        if self.isEmpty():
            return self.items[-1]

    # push element into top of the stack
    def push(self,item):
        self.items.append(item)

    # remove the items on top of the stack
    def pop(self):
        return self.items.pop()

    # take a look on top of the stack
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

myStack=Stack()
#print(myStack.isEmpty())
myStack.push(42)
myStack.push(45)
myStack.push('Look for me')
myStack.push(2)
#print(myStack.peek())
print(myStack.__dict__)
print("Size of stack: ", myStack.size())
popped_value = myStack.pop()
print("Popped value: ", popped_value)
print("Size of stack: ", myStack.size())


