#dict--> key:value --> key is unique
d = {1:"one", 2:"two",3:"three"}
print(d)

#functions

print(d.keys())  #extract keys from dictionary
print(d.values())
print(d.items())

#converting list to dict

l = ["hi","hello"]
print(d.fromkeys(l))  #converted
print(d.fromkeys(l,10))

#functions
#print(d.update({'c':89}))
print(d.pop(1))  # delete -->fetch and delete
print(d)

print(d.popitem())

d1 = {1:"a",2:"b"}
print(d1.setdefault(3,d))
