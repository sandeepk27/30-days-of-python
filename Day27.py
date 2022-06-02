import math

me="sandeep kumar"
x1=2
x="this is %s" %me
print(x)

y="this is {1} {0}"
z=y.format(me,x1)
print(z)


n=f"this is {me} {x1} {4*8} {math.sin(30)}"
print(n)