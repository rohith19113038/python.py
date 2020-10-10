#a) Print those numbers which are divisible by 7 and multiple of 5, between 75 and 200.

#b) Print all the numbers from 0 to 10 except 3 ,6 and 9.

    #Expected Output: 0 1 2 4 5 7 8 10
    
#program 1
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)
        
        
        
#program2 
for x in range(10):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
    
    
    
    
