from functools import reduce
import re


l1=[1,2,3,4,3,4,55,32,66,32,77,8,9]

def greater_num(n):
    return n>5

gr_than_5=list(filter(greater_num,l1))
print(gr_than_5)

l2=[1,2,4,3,66,4,6,88,57,]
num=reduce(lambda x,y:x*y, l2)
num=0
for i in l2:
    num=num+i
    print(num)
print("The number is:" ,str(num))





def check(str, pattern):
    if re.search(pattern, str):
        return True
    else:
        return False


def newCheck(str, pattern):
    for i in str.lower():
        if i not in pattern.lower():
            return False
            return True


# _driver code
str1 = input()
str2 = input()
# pattern = re.compile('[str2]')
if newCheck(str1, str2):
    print("Input string is valid")
else:
    print("Input string is not valid")
    print(str1)
