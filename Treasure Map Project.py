# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, 
       row2, 
       row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row_value = int(position[0])-1

column_value = int(position[1])-1

map[column_value][row_value]= "X"

# Uneccessary Logic
# if column_value == 0:
#   row1[row_value] = "X"
# elif column_value == 1:
#   row2[row_value] = "X"
# elif column_value == 2:
#   row3[row_value] = "X"
# else:
#   print("Not a valid space.")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")