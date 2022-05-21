
import json
from re import X
x='{"name":"Sandeep","age":25,"city":"Hyderabad"}'
y=json.load(x)
print(y)
print(y['name'])


A={
    "name":"Sandeep",
    "age": 25,
    "city":"Hyderabad",
    "status":"Single",
    "pets":"None",
}

B=json.dumps(A)
print(B)
print(json.dumps(["apple","guava","kiwi"]))
print(json.dumps(("sid","stella")))
print(json.dumps(A))