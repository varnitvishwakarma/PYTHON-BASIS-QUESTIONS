---------------------------------------------------------------------------question 1 ---------------------------------------------------------------------------------

A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.




year=int(input("enter your service year with this company:"))

if year>=5:
    salary=int(input("enter your salary"))
    bonus=salary*5
    amount=bonus/100
    print("your bonus amount is :",amount)
elif year<5:
    print("you are not eligable for bonus")

year=int(input("enter your service year with this company:"))
​
if year>=5:
    salary=int(input("enter your salary"))
    bonus=salary*5
    amount=bonus/100
    print("your bonus amount is :",amount)
elif year<5:
    print("you are not eligable for bonus")
​
---------------------------------------------------------------------------question 2 ---------------------------------------------------------------------------------



Take values of length and breadth of a rectangle from user and check if it is square or not



length = int(input("Enter the length of your rectangle "))
breath= int(input("Enter the breath of your rectangle"))
if length==breath:
    print("Yes, it is a square")
else:
    print("No, it is not a square , it is a rectangle")

 ---------------------------------------------------------------------------question 3 --------------------------------------------------------------------------------
   
    
Take two int values from user and print greatest among them



one = int(input("Enter first number"))
two= int(input("Enter second number"))
​
if one>=two:
    print(one)
else :
    print(two)

    
---------------------------------------------------------------------------question 4----------------------------------------------------------------------------------

    
  
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user



unit=int(input("enter your purchased unit:"))
cost=100
​
if unit>=1000:
    amount=unit*100
    discount=amount*10
    new=discount/100
    money=amount-new
    print("Your total cost after discount",money)
else:
    new_money=unit*100
    print(new_money)

    
 ---------------------------------------------------------------------------question 5---------------------------------------------------------------------------------
   
    
A school has following rules for grading system:
Ask user to enter marks and print the corresponding grade.
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.



grade=int(input("ENTER YOUR GRADE:"))
if grade>=80 and grade<=100:
    print("your grade is A")
elif grade>=60 and grade<80:
    print("your grade is B")
elif grade >=50 and grade<60:
    print("your grade is C")
elif grade >=45 and grade<50:
    print("your grade is D")
elif grade >=25 and grade<45:
    print("your grade is E")
elif grade<25:
    print("your grade is F")
else :
    print("Invalid grade")

  
---------------------------------------------------------------------------question 6 ---------------------------------------------------------------------------------

    
    
Take input of age of 3 people by user and determine oldest and youngest among them.



age_one=int((input("Enter the age of first person")))
age_two=int((input("Enter the age of second person")))
age_three=int((input("Enter the age of third person")))
​
if age_one>=age_two and age_one>=age_three:
    print("The oldest person :", age_one)
    if age_two>age_three:
        print("the youngest person :", age_three)
    else:
        print("the youngest person :", age_two)
elif age_one<=age_two and age_one<=age_three:
    print("the youngest person :", age_one)
    if age_two>age_three:
        print("the oldest person :", age_two)
    else:
        print("the oldest person :", age_three)
elif age_two>=age_one and age_two>=age_three:
    print("The oldest person :", age_two)
    if age_one>age_three:
        print("the youngest person :", age_three)
    else:
        print("the youngest person :", age_three)
elif age_two<=age_one and age_two<=age_three:
    print("the youngest person :", age_two)
    if age_one>age_three:
        print("the oldest person :", age_one)
    else:
        print("the oldest person :", age_three)
elif age_three>=age_one and age_three>=age_two:
    print("The oldest person :", age_three)
    if age_one>age_two:
        print("the youngest person :", age_two)
    else:
        print("the youngest person :", age_one)
elif age_three<=age_one and age_three<=age_two:
    print("the youngest person :", age_three)
    if age_one>age_two:
        print("the oldest person :", age_one)
    else:
        print("the oldest person :", age_two)
​


---------------------------------------------------------------------------question 7 ---------------------------------------------------------------------------------



Write a program to print absolute vlaue of a number entered by user.
num=int(input("enter number:"))
​


if num<0:
    print("abosulte number is :",num*-1)
else :
    print("absoulte number is ", num)

---------------------------------------------------------------------------question 8 ---------------------------------------------------------------------------------
    
    
    
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.



total=int(input("Enter total classes held "))
attend=int(input("Enter total classes attended "))
​
per=(attend/total)*100
if per>75:
    print("you are allowed to sit in exam because your attendence is :",per,"%")
else:
    print('you are not allowed to sit in exam because your attendence is below 75%')
