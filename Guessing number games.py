import random
n=random.randrange(1,50)
guess=int(input("guess the number"))
while n!=guess:
    if guess<n:
        print("LOW")  
        guess=int(input("guess the number"))
    elif guess>n:
        print("HIGH")  # guess is high according to system  gues : 33--->20 system --> print high
        guess=int(input("guess the number"))
    else:
        break
print("guess is correct")
