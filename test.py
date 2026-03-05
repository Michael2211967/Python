import datetime
from openpyxl import Workbook, load_workbook

months = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split()

today = datetime.date.today()
a = input()
a += str(today.year)
a += ".xlsx"
file = load_workbook("T:/Eigene Dateien/Tabellen/" + a, data_only=True)
sheet = file[months[today.month - 1]]

a21 = sheet["A21"].value
b21 = sheet["B21"].value
d21 = sheet["D21"].value
f21 = sheet["F21"].value
g21 = sheet["G21"].value
h21 = sheet["H21"].value

print(a21, b21,d21, f21, g21, h21)

