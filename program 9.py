our_pass="pass123"
my_pass=""
no_of_try=0
no_of_Max_try=3
Max_try="not reached"

while my_pass!=our_pass and Max_try!="reached":
    if no_of_try<no_of_Max_try:
        my_pass=input("enter the password:")
        no_of_try
        no_of_try=no_of_try+1
    else:
        Max_try="reached"
    
if Max_try=="reached":
    print("access blocked")
else:
    print("access granted")
