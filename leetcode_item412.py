from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_n=list(range(1,n+1))
        list_s=[]
        for i in list_n:
            if i % 15 == 0:
                list_s.append("FizzBuzz")
            elif i % 3 == 0:
                list_s.append("Fizz")
            elif i % 5 == 0:
                list_s.append("Buzz")
            else:
                list_s.append(str(i))
        return list_s

Solution().fizzBuzz(45)
            



list_n=list(range(1,6))
list_n