print("printing first 10 or 11 of fibonachi")

i0 = 0 
i1 = 1
for i in range(10): 
    new = i0 + i1 
    i0 = i1 
    i1 = new 
    print(new)