#operators ----> +, -, /, //(floor), %,
print(10/2)  #returns float
print(10//2)  # floor ---> returns integer

#relational operator --> <, >, <=, >= , !=
print(10>2)
print(10<2)
print(10>=2)
print(10<=2)
print(10==2)
print(10!=2)
print("\n")
print("LOGICAL OPERATORS")
print(10>2 and 3<10)
print(10>2 or 3>10)
print(10<2 and 3<10)
print(10<2 and 3<10)
print(not(10>2))
print("\n")
print("MULTIPLE INPUTS")
'''a,b = int(input("enter a value")), int(input("enter b value"))
print(a)
print(b)
#separate by comma
c,d = input("enter two values split with ,  operator ").split(",")
print(c)
print(d)
sum = a+b
print(sum)  #by default input() is string --> concatenation occur
e,f = input("enter two values split with ,  operator ").split(",")
print(e)
print(f)'''
print("\n")
print("BITWISE OPERATORS")
#BITWISE and, bitwise or, ~ ,exor, left shift ,
print(10&4)  # & ---> perform and operation
print(12&7)
print(10|4)  # | ---> perform or operation
'''print(12|7)
print(~10)   # ~ --> perform 1's complementory  (-(10+1))
print(5^6)  # ^ --> perform Exor operation  ---> identical gives 0
print(9^8)
print(10<<2)  # << --> 2bits shifted left
print(5<<2)
print(7>>3)'''

print("\n")
print("Conditional Statements") # --->if,ifelse, elseif, elseifladder, nestedif
print("\n")

print("Control Statements")  #---> while or for loop

i=1
while i<=5:
    print(i)
    i+=1

#range(1,10) ----> genarate sequence of numbers
#in ---> membership operator(from that range)




