logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import random
import replit

def caesars_cipher(text, shift, choice):
  if choice == 'encode':
    encrypted_text = ''
    for letter in text:
      if letter not in alphabet:
        encrypted_text += letter
      else:
        shifted_location = alphabet.index(letter)+ shift
        encrypted_text += alphabet[shifted_location]
    print(f"The encoded text is: {encrypted_text}")
    
  elif choice == 'decode':
    decrypted_text = ''
    for letter in text:
      if letter not in alphabet:
        decrypted_text += ' '
      else:
        shifted_location = alphabet.index(letter)- shift
        decrypted_text += alphabet[shifted_location]
    print(f"The encoded text is: {decrypted_text}")







end_program = False

# #Start Program Loop
while end_program == False:
  if end_program == False:
    print(art.logo)
#     #While loop to make sure direction input is acceptable
    acceptable_direction = False
    
    while acceptable_direction == False:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      if direction == 'encode' or direction == 'decode':
        acceptable_direction = True
      else:
        print("That is not an acceptable choice")
    
    
    
     #Text Input
    text_input = input("Type your message:\n").lower()
    
#     #Shift Input
    acceptable_shift = False

    while acceptable_shift == False:
      try:
          shift_input = int(input("Type the shift number:\n"))
          acceptable_shift = True
      except ValueError:
          print("Please only use numbers")
    
    if shift_input > 36:
      shift_input = shift_input%26
    else:
      shift_input = shift_input
    
    
    caesars_cipher(text=text_input,shift=shift_input, choice=direction)

    restart = input("Type 'Yes' if you would like to go again. Otherwise type 'No'.\n").lower()
    if restart == 'yes':
      end_program = False
      replit.clear()
    elif restart == 'no':
      print("Goodbye!")
      end_program = True
    
    