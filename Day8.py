dict={
    "name":'Sandeep',
    'place':'hyderabad',
    'study':'PG',
    'year':'2022',
    'year':'2019',
}

print(dict)
print(len(dict))
print(type(dict))

dict["member"]='Natasha,'sid','Tony'
print(dict) #print updated dict

x=dict.keys() #print keys only
print(x)

dict.update({'name':'sid'}) #updates the new value
print(dict)

fam={
    'c1':{
        'name':'sid'
    },
    'c2':{
        'name':'Tony'
    }
}
print(fam)