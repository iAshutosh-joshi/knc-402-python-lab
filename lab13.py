print("Lab 13 by Ashutosh Joshi")
def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter N:"))  
i=2 
lst=[] 
while(1):  
    if(Prime(i)):  
        lst.append(i) 
        if(len(lst)==N): 
            break 
    i+=1 
print("First "+str(N)+" Prime numbers are:",end="") 
print(*lst)