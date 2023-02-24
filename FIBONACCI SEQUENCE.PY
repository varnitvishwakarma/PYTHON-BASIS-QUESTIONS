number=int(input("enter the number of element you are looking for Fibonacci sequence"))
a,b = 0,1
counter = 0

while counter < number:
    print(a)
    c=a+b
    a=b
    b=c
    counter = counter +1
