def funargs(normal, *arg, **kwargs):
    print(normal)
    for item in arg:
        print(item)
    print("\n Now i would like to introduce me")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
        
me=["sandeep kumar","my age is :23","live in hyderabad"]


normal="I am sandeep and i am learning python"

kw={
    "Name":"sandeep",
    "Age":"25",
    "city":"Hyderabad",
}


funargs(normal,*me,**kw)