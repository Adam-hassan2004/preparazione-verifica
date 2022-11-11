numeri = [44, 16, 69, 2, 9]
animali =["giraffa", "squalo", "camaleonte", "deca","yous...scimmie"]

listona = numeri + animali
for x in listona:
    if isinstance(x, int) and x >5:
        print(x)
