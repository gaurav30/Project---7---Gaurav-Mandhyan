a=int(input("Enter first number"))
b=int(input("Enter second number"))
count=0
list=[]
for i in range(1,min(a,b)+1):
	if(a%i==b%i==0):
            list.append(i)
            count=count+1
if(count>=2):
    n1=max(list)
    list.remove(n1)
    n2=max(list)
    for i in range(1,n2+1):
        print ("")
        for j in range(1,n1+1):
            print("*",end=" ")
else:
    avg=(a+b)//2
    for i in range(1,avg+1):
        print("*")
                
                

