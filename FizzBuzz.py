from collections import defaultdict
from re import S
from typing import DefaultDict


def fizzbuzz():
    for i in range(1,101):
        if i % 3 != 0 and i % 5 != 0:
            print(i)
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 3 != 0 and i % 5 == 0:
            print("buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
fizzbuzz()
        
def fizzbuzz2():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 ==0 :
            print("Fizz")
        elif i % 5 ==0 :
            print("Buzz")
        else:
            print(i)
fizzbuzz2()

def ss(number_list,n):
    found=False
    for i in number_list:
        if i == n:
            found=True
            break
    return found

numbers=range(1,100)
print(ss(numbers,55))
print(ss(numbers,105))

def palindrome(word):
    word=word.lower()
    return word == word[::-1]
palindrome("Papap")

def anagram(w1,w2):
    w1=w1.lower()
    w2=w2.lower()
    return sorted(w1) == sorted(w2)

anagram("iceman","cinema")

def count_str(s):
    count_dict={}
    #s=s.lower()
    for i in s:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    print(count_dict)

count_str("Dynacity")
from collections import defaultdict
def count_characters(string):
    count_dict= defaultdict(lambda:0)#defaultdict(int)と等価。int()とカッコはつけない
    print(count_dict)
    for c in string:
        count_dict[c] += 1#cがキーにない場合__missing__メソッドが呼ばれ
                          #与えられたkey(この場合はc)に対応するデフォルト値(この場合は0)
                          #を提供する。それに対し１インクリメントする、という式
    print(count_dict)

count_characters("Dynacity")

from collections import defaultdict
def count_characters(string):
    count_dict= defaultdict(list)
    print(count_dict)
    for c in string:
        count_dict[c].append(c)
    print(count_dict)

count_characters("Dynacity")

#以下はhttps://qiita.com/crambon/items/bba0b01aa7711760a3f4より引用
#__missing__がわからなかったため
class LeetDict(dict):
    def __missing__(self, key):#keyが存在しなかった場合keyの値を返すようオーバーライド
        return key

leet_dict = LeetDict(   #一般的な辞書オブジェクトの作り方(LeeDictはdictのサブクラス)
    O='0',
    I='1',
    S='5',
    T='7',
    E='3',
)
print(leet_dict)
question = 'NOW IS THE TIME'
answer_list =  [leet_dict[k] for k in question]
#↑ kが辞書(のサブクラス)leet_dictのキーにあればバリューを返し、なければキーの値をバリューとして返す
print(answer_list)
print(''.join(answer_list)) # N0W 15 7H3 71M3


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(d)
for k, v in s:#kがキーにない場合__missing__メソッドが呼ばれ
              #与えられたkey(この場合はk)に対応するデフォルト値(この場合は[])
              #を提供する。それに対しvをアペンドする、という式
    d[k].append(v)
print(d)
sorted(d.items())

from collections import Counter
print(Counter(cat=3,dog=1))
print(Counter("masaakimatsuda"))
c=Counter("MsaaakiMatsuda")
c["M"]
c=Counter("girlfriend")
print(c)
c["g"]=0
print(c)
for i in c:
    print(i)
print(c)
c["g"]
list(c)