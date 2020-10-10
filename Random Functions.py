import random

print("1,2,3,4,5,6,7")

print("Random number = ",end=" " )

print(random.choice([6,78,4,5,1,3]))

print("Random number from range 50 to 100 =",end=" ")

print(random.randrange(50,100,5))

print("Random number between 0 and 1 =",end=" ")

print(random.random())

random.seed(5)

print("The mapped random number with 5 is ")

print(random.random())

print(random.random())

print(random.random())

random.seed(7)

print ("The mapped random number with 7 is ")

print (random.random())

print(random.random())

print(random.random())

random.seed(3)

print("The mapped random number with 3 is ")

print(random.random())

print(random.random())

print(random.random())

random.seed(6)

print ("The mapped random number with 6 is ")
 
print (random.random())

print(random.random())

print(random.random())
