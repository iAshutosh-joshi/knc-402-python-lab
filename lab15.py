print("Lab 15 by Ashutosh Joshi")
c='A'
for i in range(5):
    s=""
    for j in range(5):
        s=s+c
    print(s)
    c=chr(ord(c) + 1)