# lets build a small calculator 
first = input("enter your first number :")
operator = input("enter your operator(+,*,/,-,%) :")
second =input('enter your second number :')

first = int(first)
second = int(second)

if operator == '+':
    print(first + second)

elif operator == '-':
    print(first - second)
    
elif operator == '*':
    print(first * second)
    
elif operator == '/':
    print(first / second)
    
elif operator == '%':
    print(first % second)
    
else:
    print("invalid input")
