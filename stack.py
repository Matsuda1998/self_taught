class Stack:
    def __init__ (self):
        self.items=[]
    def is_empty(self):
        """空ならTrueを返す"""
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

stack=Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
stack.pop()
print(stack.is_empty())
for i in range(0,6):
    stack.push(i)
print(stack.peek())
print(stack.size())

stack=Stack()
for i in "Hello":
    stack.push(i)

reverse=""
while stack.size() > 0:
    reverse += stack.pop()
    print(reverse)
print(reverse)