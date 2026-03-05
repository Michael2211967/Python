def roman_v1(mdg):
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    roman = []
    for i in range(0, len(mdg)):
        roman.append(values[mdg[i]])

    for i in range(0, len(roman)-1):
        if roman[i] < roman[i+1]:
            roman[i] *= -1
       
    return sum(roman)

roman_numeral = input("Geben Sie eine römische Zahl ein: ")
          
print(roman_v1(roman_numeral))
