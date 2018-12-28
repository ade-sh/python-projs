#print statement 10000 times
import time
a=time.time()
d=input("Enter something:")
for i in range(0,10000):
 print(d)
b=time.time()
print("Time Taken:",b-a)

 
