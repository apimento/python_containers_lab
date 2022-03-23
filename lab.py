# CHALLENGE 1
students= ["Andrew", "Jupiter", "Pear", "Water Bottle"]

# print(students[1]) 

#CHALLENGE 2 
foods = ("couscous" , "lemon", "pepper", "olive oil") 
# for x in foods: 
#     # print(x, "is a good food") 

# #CHALLENGE 3 
#     print(foods[-2 : ],"are good foods") 

#CHALLENGE 4 
# hometown = { 
#     "city": "Toronto", 
#     "province": "Ontario", 
#     "population": "7 million"
# } 
# print("I was born in", hometown["city"],hometown["province"], "- population of", hometown["population"]) 

#CHALLENGE 5 
# hometown = { 
#     "city": "Toronto", 
#     "province": "Ontario", 
#     "population": "7 million"
# } 
# for key in hometown:
#     print(key, "=", hometown[key]) 

#CHALLENGE 6 
# cohort = []

# for x in range(len(students)):

#     cohort.append({
#         "student": students[x], 
#         "fav_food": foods[x]
#         })  

# print(cohort) 

#CHALLENGE 7 

# awesome_students = [f"{x} is awesome" for x in students]
# print(awesome_students) 


#CHALLENGE 8 
a_foods = []
for x in foods: 
    if "o" in x: 
        a_foods.append(x) 
print(a_foods)