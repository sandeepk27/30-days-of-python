class example:
    a = 10*5
print(example.a)


class myexample:
    x =20
obj = myexample
print(obj.x)


class person:
    def __init__(self,name,age,address,mobile):
        self.name=name
        self.age=age
        self.address=address
        self.mobile=mobile
val = person("Sandeep",25,"India",1234567890)
print('My name is : ' + val.name)
print('My age is : ' + str(val.age))
print('I live in : ' + val.address)
print('Contact : ' + str(val.mobile))
        