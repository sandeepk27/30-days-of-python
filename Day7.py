s1={'sid','Nat','jessy','stella'}
s2={'pepper','Tony','Nat'}

print(type(s1))
print(s1)
print(s2)

s3=s1.symmetric_difference(s2)
print(s3)
s1.update(s2)
print(s1)
s1.pop()
print(s1)
s2.intersection_update(s1)
print(s2)
s2.remove('sat')
print(s2)

x=s1.symmetric_difference(s2)
print(x)
for y in s1:
    print(y)