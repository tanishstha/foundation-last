from re import T
from signal import default_int_handler


def addName(first,second):
    return(first + " " + second)

f_Name = input("Enter first Name:")
s_Name = input("Enter Second Name:")
print("Your Name:",addName(f_Name,s_Name))

#string formatting
print("My-1 name-2 is-3 abc-4 def-5")

phone_num =98490
print(f"your phone number is{phone_num}")

first =1
second =2
third =3
fourth =4
fifth =5

print(f"My-{first} name-{second} is-{third} abc-{fourth} def-{fifth} ")


# len function
length_of_this = len("Education")
print(length_of_this)

#conditional statement in python

name=input("what's your name please?")
age= int(input("what,s your age please?"))

if age<0:
    print(f"Invalid Age")
elif age==10:
    print(f"Dear {name}, your ticket price is:100")
elif age>10:
    print(f"Dear {name}, Your ticket price is:150")
else:
    print(f"Dear{name}, Your ticket price is:50")
    
def calc_weight(m,g=10):
    print(f"Your weight is:{m*g}N")

mass = int(input({"Please enter your mass:"}))
print(calc_weight(mass))

#1 Ask a two integer number with user and a function should return their addition
#2 Ask an information of your laptop and a function should return like this:
"""
Brand_Name_Model_Name available_at Price

Ex: Dell Vostro @ Rs. 80000

"""
def add(num1,num2):
    sum= num1 +num2
    return(sum)

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number"))
sum = add(num_1,num_2) 
print(f"sum is {sum}")

def retInformation(brand,model,price):
    print(f"{brand} {model} @Rs. {price}")

BName =input("Enter brand name:")
MName =input("Enter model name:")
Price =int(input("Enter price:"))
retInformation(BName,MName,Price)

# Working model of atm machine :

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False
required_amt = int(input("Please enter a amount:"))


def read_card():
    card_details=input("Please insert your atm card:")
    card_details =[1200,False,False]
    total_price =card_details[0]
    is_same_bank=card_details[1]
    is_expired =card_details[2]
    if is_expired == False:
        perform_transaction(total_price,is_same_bank)  
    else:
        print ("Sorry, this card cannot be accepted here")


def perform_tansaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


print("Please insert your atm card:")
input()
print("Card inserted!!")
required_amt = int(input("Please enter a amount:"))
read_card()    

#range (s,s,s) --> start , stop, step
for i in range(0,10,1):
    print(f"the value of i is:{i}")

days_list = [
    'sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]    
for day in days_list:
    print(f"The single day is:{day}")

#append() method
#--> It is used to insert data into the existing list 
print(days_list)
days_list .append("sunnyday") 
print(days_list)

for day in days_list:
    print("your recent days")
for day in days_list:
    print(day,end="")
#pop()
#--> It is used to eject the last element/item from the list and return to us.
print(days_list)
days_list.pop()
print(days_list)
#But if you want to remove specific item then,
days_list.pop(2)
print(days_list)