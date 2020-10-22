#IN FUNCTION ASCENDING ORDER

print("ASCENDING FUNCTION")
a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOND NUMBER: "))

def ascend(a, b):
    if(a > b):
        a,b = b,a
    else:
        pass
    return [a, b]
    
print(ascend(a, b))


#CALUCLATOR FUNCTIONS

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b==0:
        return error
    else:
        return a/b
        

num1 = int(input("ENTER FIRST OPERAND: "))
num2 = int(input("ENTER SECOND OPERAND: "))
print("SELECT OPERATION: ")

choice = input("1. ADDITION  2. SUBTRACTION  3. MULTIPLICATION  4. DIVISION: ")


while True:
    if choice in ('1', '2', '3', '4'):
        
        if choice=='1':
            print(add(num1, num2))
            break
        elif choice == '2':
            print(subtract(num1, num2))
            break
        elif choice == '3':
            print(multiply(num1, num2))
            break
        elif choice == '4':
            print(divide(num1, num2))
            break
        else:
            print("WRONG INPUT")
            
