cars=['scorpio','baleno','swift',"BMW",'BENZ']
x=[0]
print(x)
cars=['Ford']
print(cars)

x=len(cars)
print(x)
for x in cars:
    print(x)
cars.append("Audi")
print(cars)
cars.pop(1)
print(cars)

fruits=['orange','guava','strawberry','mango','cherry']
fruits.sort()
print(fruits)


fruits.remove('guava')
print(fruits)

x=cars.extend(fruits)
print(x)