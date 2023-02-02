'''l=[1,2,3,4,5,6,7,8]        #console input
for i in range(len(l)):
    if(i%2==0):
        print(i)  '''

size = int(input("enter size"))
l =[]                        #user input
for i in range(size):
    from_user = int(input("enter user element"))
    l.append(from_user)
print(l)

#finding even number
for j in l:
    if j%2==0:
        print(j)
