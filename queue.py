class Queue():
    def __init__(self) -> None:
        self.items=[]
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)

queue=Queue()
print(queue.is_empty())
print(queue.size())
for i in range(5):
    queue.enqueue(i)
print(queue.size())

while queue.size() > 0 :
    print(queue.dequeue())
print()
print(queue.size())
