from openpyxl import Workbook, load_workbook

wb = Workbook("easter.xlsx")
ws = wb["Ostern"]

def ostern(jahr):
    A = jahr % 19
    K = jahr // 100
    M = 15 + (3 * K + 3) // 4 - (8 * K + 13) // 25
    D = (19 * A + M) % 30
    S = 2 - (3 * K + 3) // 4
    R = D // 29 + (D // 28 - D // 29) * (A // 11)
    OG = 21 + D - R
    SZ = 7 - (jahr + jahr // 4 + S) % 7
    OE = 7 - (OG - SZ) % 7
    OS = OG + OE
    if OS > 31:
        return ([year:=jahr, mon:=4, day:=OS - 31])
    else:
        return ([year:=jahr, mon:=3, day:=OS])

input = int(input("Geben Sie das Jahr ein: "))
easter = ostern(input)

ws.append(easter)
wb.save("easter.xlsx")


