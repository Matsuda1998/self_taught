class Stack():
    def __init__(self) -> None:
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)

def reverse_str(s):
    """sは文字列\"\"をつけて入力"""
    r_str=""
    stack=Stack()
    for i in s:
        stack.push(i)
    while not stack.is_empty():
        r_str += stack.pop()
    return r_str

print(reverse_str("MasaakiMatsuda"))

def reverse_list(l):
    """lはリスト[]をつけて入力"""
    r_list=[]
    stack=Stack()
    for i in l:
        stack.push(i)
    while not stack.is_empty():
        r_list.append(stack.pop())
    return r_list

print(reverse_list([1,2,3,4,5]))
