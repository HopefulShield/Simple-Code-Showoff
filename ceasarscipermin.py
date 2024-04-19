#test string "ABCdefghijklmnopqrstuvwxyz1%" 

import sys

cipher = "a"
while not cipher.isdigit():
    cipher = input("Please input an integer for the cipher shift: ") #get cipher shift number 
#print(cipher.isdigit())
cipher = int(cipher)

userString = input("Please input a string: ") #get string 
print("User input string:", userString)
userString = userString.lower() #make string lowercase 
userString = list(userString) #make string to list form 

for i in range(len(userString)): #iterate through list string and shift all alpha chars by cipher shift 
    #print(var[i], "isalpha?:", var[i].isalpha())
    if userString[i].isalpha(): #   make sure alpha chars remain alpha char, with modulo
        shifted = ord(userString[i]) + cipher 
        shifted = ((shifted - 97) % 26) + 97
        userString[i] = chr(shifted)
        #print(var[i])

print("En/De-crypted input string: ", "".join(userString)) #return string as "".join(list string)










