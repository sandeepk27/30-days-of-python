def my_name(fname,lname):
    print(fname," "+lname)
print("My family member are:")

my_name('tony','stark')
my_name('peter','parker')
my_name('Natasha','Romanoff')



def my_fun(*fruits):
    print("The fruit name is:" +fruits[2])

my_fun('apple','orange','guava','mango')



def child(c1,c2,c3):
    print('The younger child of my family is:' +c3)
child(c1='stan',c2='steve',c3='smith')


def function(food):
    for i in food:
        print(i)
fruits=['apple','mango','banana','guava']
function(fruits)


def num(x):
    return 5*x
print(num(3))
print(num(7))