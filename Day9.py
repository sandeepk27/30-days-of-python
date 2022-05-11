a=37
b=17
i=1

if a>10:
    print("a is greater than b")
elif a==b:
    print('a is equals to b')
    
c=52
if a>b and a<c:
    print("Both conditions are true")
if a<b and a>c:
    print('at least one condition is true')

while i<6:
    i+=1
    if i==4:
        break
    print(i)
    
veg=['carrot','coriander','mint']
for x in veg:
    print(x)
    if x=='coriander':
        break
    
    
for j in range(1,40,4):
    print(j)