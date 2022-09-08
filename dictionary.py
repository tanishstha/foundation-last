"""
It is always represent in the form of:
my_dictionary ={"key":"Value"}
"""

# why we need dictionary?
#--> To overcome the problem exist in list.
#For eg:
#user_detail=["Tanish","Stha",20,["English","Nepali","Japnese"],9845102340,["Burger","pizza","momo"]]

user_details={"first_name":"Tanish",
"last_name":"Stha",
"language_spoken":["English","Nepali","Japnese"],
"contact":9845102340,
"fav_food":["Burger","pizza","momo"]

}

# print(user_details["first_name"])


for key,value in user_details.items():
    print(f"key is {key}")