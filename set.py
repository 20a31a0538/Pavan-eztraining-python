s = {1,2,3,4,2,4,5}
print(s)         #duplicates are not allowed  ---> unordered ---> no indexing

#funtions

s.add(55)  # add()--> randomly append element
print(s)

s.update([10,20,30,40])  #append multiple elements
print(s)

s.discard(55)  # delete element --> not gives error if we delete --> not present element
print(s)

s.remove(30)
print(s)

#operations
s1={1,2,3}
s2={1,2,3,4,5,6}
print(s1|s2)   # s1.union(s2)
print(s1&s2)  #s1.intersection(s2)
print(s1-s2)  #s1.difference(s2)

#other functions
print(s2.issuperset(s1))  #superset
s3={1,2,3,4,5,10}
s4={4,1,9,2,10}
print(s3^s4)  # symmetric_difference  
print(s3.symmetric_difference(s4))


