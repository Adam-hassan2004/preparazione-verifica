import random
x=random.randint(0,100)
y=random.randint(0,100)
z=random.randint(0,100)
listone=[x,y,z]
listone.sort()
print(listone)
auto=["bmw","tesla","audi","nike","adidas"]
moto=["honda","kawasaki","yamaha","puma"]
lista=auto+moto
lista.sort()
print(lista)
list=[]
for i in range(50):
    list.append(random.randint(0,100))
list=[a  for a in list if a%2 >0]
print(list)
lis=[]
for i in range(50):
    lis.append(random.randint(0,100))
lis=[a  for a in list if a>50 or a<10]
print("ho stampato", lis ,"il numero é",len(lis))

z=random.randint(10,20)
listone1=[]
for i in range(z):
    n=random.randint(0,20)
    listone1.append(n)
print(listone1)

listone2=[]
for i in listone1:
    if i<z:
        listone2.append(i)
print(listone2)

esclusi=[]
for i in listone1:
    if i<z:
        listone2.append(i)
    else:
     esclusi.append(i)
print(esclusi)

esclusi2=[]
for i in listone1:
    if i<z:
        listone2.append(i)
    else:
     esclusi.append(i)
for i in esclusi:
    o=i**2
    esclusi2.append(o)
print(esclusi2)

risultone=0
listone2=[]
for i in listone1:
    if i<z:
        listone2.append(i)
for g in listone2:
    if g>z:
        risultone+=g
print(risultone)


