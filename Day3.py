int=5
float=1.9
complex=3j
X=40
Y=20
A="Hello"
Text="the \'Board\' Pass Number is {} but become {}"

print(int+float+complex)
print(type(X))
print(type(Y))
print(type(A))
print(Text.format(Y,X))
print('word between 1 to 4 is:'+A[1:4])
print('starting from 0 and ending in 6 is:' +A[:4])
print('starting from 2 and ending in last word is:' +A[2:])