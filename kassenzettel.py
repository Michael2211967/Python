from openpyxl import Workbook, load_workbook

workbook = load_workbook("Kassenzettel.xlsx")
sheet = workbook["Kassenzettel"]

def get_price(name):
    preislist = workbook["Hit"]
    for row in range(2,13):
        if preislist["A{}".format(row)].value == name:
            return preislist["B{}".format(row)].value
    return 9999

sum = 0
for row in range(2,6):
    artikel = sheet["A{}".format(row)].value
    b = sheet["B{}".format(row)].value
    c = get_price(artikel)
    d = b * c
    if c < 9999:
        sum += d
    sheet["C{}".format(row)].value = c
    sheet["D{}".format(row)].value = d
    print(c,d)

sheet["D12"].value = sum
print(sum)

workbook.save("Kassenzettel.xlsx")
