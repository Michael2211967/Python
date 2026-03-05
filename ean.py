ean = input("EAN eingeben: ")
test = ean[:-1]
d = 3
checksum = 0

for i in range(len(test)-1, 0, -1):
    checksum += int(test[i]) * d
    if d == 3:
        d = 1
    elif d == 1:
        d = 3
        
checksum += int(test[0]) * d
check = int(checksum / 10 + 0.9) * 10
checkdigit = check - checksum

if int(ean[-1]) == checkdigit:
    print("\nDie EAN sieht gut aus.")
else:
    print("\nIrgendetwas stimmt nicht.")
    print(f"Die erechnete Prüfziffer ist {checkdigit}.")

