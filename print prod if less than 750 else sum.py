n = list(map(int,input("enter list").split()))  #user input using map
print(n)
prod = 1
sum= 0
for i in n:
    prod=prod*i
    sum = sum+ i
print(prod)
print(sum)

if prod<750:
    print(prod)
else:
    print(sum)
