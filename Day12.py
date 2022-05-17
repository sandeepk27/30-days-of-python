x=lambda a:a+10
print(x(5))


y=lambda a,b:a*b
print(y(3,4))


def myfunc(n):
    return lambda a:a*n
multi=myfunc(3)
print(multi(4))


def mynum(n):
    return lambda a:a-n

fnum=mynum(2)
snum=mynum(3)

print(fnum(22))
print(snum(33))
print(type(fnum))