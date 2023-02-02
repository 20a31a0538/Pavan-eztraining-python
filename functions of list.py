l=[1,4,2,2,4,5,6,7,8]   #9 functions
print(len(l))   #length of list

# append element
l.append(1)  # append one element at a time in end 
print(l)
#extend()
l.extend("10,20")  # append multiple elements at a time
print(l)

#insert element in the middle of the list
l.insert(2,30)  # where 2--> is index
print(l)

#deleting elements from list
l.remove(30)   # remove() takes value
print(l)
print(len(l))
l.insert(13,200)
print(l)
l.pop(13)  #pop takes index
print(l)
'''l.clear()  # clear entire list
print(l)  '''
l.reverse()
print(l)
