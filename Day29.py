from freegames import square


def sq(a):
    return a*a

n=[2,3,45,5,53,6,8,71,92]
square=list(map(sq,n))

squ=list(map(lambda x:x*x+3,n))
print(squ)

def square(a):
    return a*a

def cube(a):
    return a*a*a

f=[square,cube]

for i in range(5):
    val=list(map(lambda x:x(i),f))
    print(val)