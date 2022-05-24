price=330
txt="The price of my food is {} rupees."
print(txt.format(price))

a=20
b=32
c=58

order="I want {} pieces of item number {} for {:.2f} rupees"
print(order.format(a,b,c))

order="I want {2} pieces of item number {0} for {1} rupees."
print(order.format(a,b,c))

name="sid"
age=25
data="His name is {1} and {1} is {0} years old."
print(data.format(age, name))