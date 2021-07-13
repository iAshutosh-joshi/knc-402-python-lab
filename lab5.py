print("Lab 5 by Ashutosh Joshi")
n=int(input()) #Number whose Square root is to be found
l=float(input()) #Tolerence level
x=n
while(1):
    root=0.5*(x+(n/x))
    if(abs(root-x)<l):
        break
    x=root
print(root)