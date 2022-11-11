lista=[1,2,3,4,5,6,7,8,9,10]
for x in lista:
    check = int(x/2)
    if check * 2 == x:
        print(x)