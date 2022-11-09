import re
from typing import List
l="Beautiful is better than ugly."
matches=re.findall("beautiful",l,re.IGNORECASE)
print(matches)

zen="""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
m=re.findall("idea.$",zen,re.MULTILINE)
print(m)

import re
string="Two too."
m=re.findall("t[wo]o",string,re.IGNORECASE)
print(m)
line="123 hi 34 hello."
m=re.findall("\d",line)
print(m)

t="__one__ __two__ __three__"
found=re.findall("__.*?__",t)
for i in found:
    print(i)

import re
text="I love $"
m=re.findall("\$",text,re.IGNORECASE)
print(m)

import re
text="The ghost that says boo haunts the loo."
ans=re.findall(".oo",text,re.IGNORECASE)
print(ans)
