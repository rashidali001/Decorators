people=[
    {"name":"rashid","age":20},
     {"name":"omar","age":13},{"name":"halima","age":12}
     
   
]
#one way of doing it
#..............................................
#def f(person):
#    return person["name"]
#people.sort(key=f)
#..............................................
#OR
people.sort(key=lambda person: person['name'])

print(people)