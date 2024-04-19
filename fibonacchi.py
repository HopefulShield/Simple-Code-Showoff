import sys

fibo = [0, 1]
curr_I = 2




fibo_n = "a"
while not fibo_n.isdigit():
    fibo_n = input("Please input an integer for the cipher shift: ") #get cipher shift number 
#print(cipher.isdigit())
fibo_n = int(fibo_n)
fibo_n = 10

i0 = 0 
i1 = 1
for i in range(fibo_n): 
    nM2 = curr_I - 2 
    nM1 = curr_I - 1 

    new = fibo[nM1] + fibo[nM2]
    fibo.append(new)
    curr_I += 1
    print(new)

print(fibo)