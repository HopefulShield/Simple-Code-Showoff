#get string 
#get cipher shift number 
#make string lowercase 
#make string to list form 
#iterate through list string and shift all alpha chars by cipher shift 
#   make sure alpha chars remain alpha char, with modulo
#return string as "".join(list string)
#test string "ABCdefghijklmnopqrstuvwxyz1%" 

import sys

cipher = "a"
while not cipher.isdigit():
    cipher = input("Please input an integer for the cipher shift: ") 
#print(cipher.isdigit())
cipher = int(cipher)

userString = input("Please input a string: ") 
print("User input string:", userString)
userString = userString.lower() 
userString = list(userString) 

for i in range(len(userString)): 
    #print(var[i], "isalpha?:", var[i].isalpha())
    if userString[i].isalpha(): 
        shifted = ord(userString[i]) + cipher 
        shifted = ((shifted - 97) % 26) + 97
        userString[i] = chr(shifted)
        #print(var[i])

print("En/De-crypted input string: ", "".join(userString)) 










