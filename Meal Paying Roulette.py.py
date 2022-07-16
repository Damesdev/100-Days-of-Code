# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# #Find length of list
# length_names = len(names)-1
# # print(length_names)
# #Generate random number from 0 to length of list
# random_name_index = random.randint(0,length_names)
# # print(random_name_index)
# #Index list result into variable
# person_paying = names[random_name_index]

person_paying = random.choice(names)

#printing results
print(f"Sorry {person_paying}, You have to pay this meal.")
