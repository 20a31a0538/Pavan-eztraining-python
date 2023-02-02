size = int(input("enter the size"))
l=[]
for i in range(size):
    user_input = int(input("enter elements"))
    l.append(user_input)
print(l)

prod = 1
for i in range(len(l)):
    prod= prod*l[i]
print(prod)

sum = 0
for i in range(len(l)):
    sum= sum + l[i]
print(sum)

if prod<750:
    print(prod)
else:
    print(sum)
