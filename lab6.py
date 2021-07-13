print("Lab 6 by Ashutosh Joshi")
n=int(input("Enter base: "))
p=int(input("Enter power: "))
output=1
for i in range(0,p):
    output=output*n
print ("Base is:",n)
print("Power is:",p)
print ("Output:", output)