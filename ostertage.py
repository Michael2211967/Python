#!/usr/bin/env python3
# Berechnungdes Ostersonntag nach Gauß für 1583 bis 2199 */
from datetime import date, timedelta

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
        return date(jahr, 4, OS - 31)
    else:
        return date(jahr, 3, OS)
    
def easter_day(easter):
    easter_days = []
    easterdays = [["Weiberfastnacht    ", -52],
                  ["Rosenmontag        ", -48],
                  ["Aschermittwoch     ", -46],
                  ["Karfreitag         ", -2],
                  ["Ostersonntag       ", 0],
                  ["Ostermontag        ", 1],
                  ["Christi Himmelfahrt", 39],
                  ["Pfingstsonntag     ", 49],
                  ["Pfingstmontag      ", 50],
                  ["Fronleichnam       ", 60]]
    for days in easterdays:
        date = easter + timedelta(days=days[1])
        easter_days.append([days[0], date])    
    return easter_days
    

if __name__ == "__main__":
        print("\t-------------------------")
        print("\t   Osterdatum nach Gauss")
        print("\t-------------------------")
         
        jahr = int(input("Jahr zwischen 1583 und 2199 eingeben! "))
        print()
        easter = ostern(jahr)
        easter_days = easter_day(easter)
       
        for i in easter_days:
            print(f"{i[0]}: {i[1]:%d.%m.%Y}")
        
        
