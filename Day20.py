import re
txt="RegEx can be used to check if a string contains the specified pattern"

x=re.findall("[e-i]",txt)
print(x)
x=re.findall("b..s",txt)
print(x)
x=re.findall("20",txt)
print(x)
x=re.findall("python$",txt)
if x:
    print("yes, the string ends with python")
else:
    print("No match")

x=re.split("\s",txt,3)
print(x)

x=re.search(r"\bs\w+",txt)
print(x)

x=re.findall("r.{5}n",txt)
print(x)

x=re.search("if.pattern$",txt)
print(x)