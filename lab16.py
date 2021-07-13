print("Lab 16 by Ashutosh Joshi")
c='A'
temp=5
for i in range(5):
    s=""
    for j in range(temp):
        s=s+c
        c=chr(ord(c) + 1)
    print(s)
    temp=temp-1
    c='A'