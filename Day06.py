tp=('apple','ball','dog','mark','tesla')
print(len(tp))
print(tp[1:4])
print(type(tp))


fruits=('orange','strawberry','kiwi','pineapple')
x=list(fruits) #converting tuple into list
x.append('mango')
x.remove('kiwi')

#fruits=tp(x)

print(x)

(a, b, c,d)=fruits #unpacking method
print(a)
print(b)
print(c)

add= tp+fruits
print(add) #adding tp and fruits
for i in fruits:
    print(i)