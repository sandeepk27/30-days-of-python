tp=('apple','cherry','mango','kiwi')
myiter=iter(tp)
print(next(myiter))
print(next(myiter))


str = "Sandeep"
a = iter(str)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


class Numbers:
    def __iter__(self):
        self.a =1
        return self
    
    def __next__(self):
        if self.a <=10:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        
myclass = Numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)   