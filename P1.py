n = int(input("cislo: "))
sucet = 0
while n > 0:
    sucet += n % 10
    n = n // 10
print(sucet)
