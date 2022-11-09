import random
import time
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

def simulate_line(til_show,max_time):
    pq=Queue()
    tkt_sold=[]
    
    for i in range(100):
        pq.enqueue("person"+str(i))
    now=time.time()
    t_end=now+til_show
    while now < t_end and not pq.is_empty():
        now=time.time()
        r=random.randint(0,max_time)
        time.sleep(r)
        person=pq.dequeue()
        print(person)
        tkt_sold.append(person)
    
    return tkt_sold

sold=simulate_line(5,1)
print(sold)


