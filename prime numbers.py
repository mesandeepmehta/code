#this is a program to check whether a number is prime
while True:
    flag=False     
    a=int(input("Enter a number you: "))
    if a==1:
        print("1 is not prime")
    elif a>1: 
        for i in range(2,a-1):
         if a%i==0:
            flag=True
            break
    if flag==True:
        print(a, "is not prime")
    else:
        print(a, "is prime")