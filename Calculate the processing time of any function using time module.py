import datetime
current_time=datetime.datetime.now()
print("time now in my device is:",end="")
print(current_time)
import calendar
y=int(input("input the year:"))
m=int(input("input the month:"))
print(calendar.month(y,m))
from time import process_time
n=60
t1_start=process_time()
for i in range(n):
    print(i,end='')
print()
t1_stop=process_time()
print("elapsed time:",t1_stop,t1_start)
print("elapsed time during the whole program in seconds:",t1_stop,t1_start)
