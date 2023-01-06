age = input(" what is your age: ")
age = int(age)

if age >= 18:
    print("you can vote")
    
elif age <= 0:
    print("invalid age")

elif age <= 18:
    print("you cannot vote")

else :
    print("invalid input")
