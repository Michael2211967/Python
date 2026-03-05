#! /usr/bin/python3

# Berechnung des Ostersonntag nach Gauß für 1583 bis 2199 */
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
    
def leap_year(year):
    if year % 400 == 0 or year % 4 ==0:
        return(29)
    else:
        return(28)

def easter_day(easterday, distance, easter_sunday, feb):
    year, mon, day = easter_sunday
    if distance < 0:
        while day <= abs(distance):
            mon -= 1
            if mon == 2:
                day += feb
            else:
                day += 31
        day += distance
    else:
        day += distance
        while day > 31:
            if mon == 4:
                mon += 1
                day -= 30
            else:
                mon +=1
                day -= 31
    return([easterday, year, mon, day])
    

if __name__ == "__main__":
        title = "   Osterdatum nach Gauss   "
        print("\t", len(title) * "-")
        print("\t", title)
        print("\t", len(title) * "-")
         
        jahr = int(input("Jahr zwischen 1583 und 2199 eingeben! "))
        print()
        easter = ostern(jahr)
        easter_days = []
        dummy = easter - timedelta(days=52)
        easter_days.append(["Weiberfastnacht    ", dummy])
        dummy = easter - timedelta(days=48)
        easter_days.append(["Rosenmontag        ", dummy])
        dummy = easter - timedelta(days=46)
        easter_days.append(["Aschermittwoch     ", dummy])
        dummy = easter - timedelta(days=2)
        easter_days.append(["Karfreitag         ", dummy])
        easter_days.append(["Ostersonntag       ", easter])
        dummy = easter + timedelta(days=1)
        easter_days.append(["Ostermontag        ", dummy])
        dummy = easter + timedelta(days=39)
        easter_days.append(["Christi Himmelfahrt", dummy])
        dummy = easter + timedelta(days=49)
        easter_days.append(["Pfingstsonntag     ", dummy])
        dummy = easter + timedelta(days=50)
        easter_days.append(["Pfingstmontag      ", dummy])
        dummy = easter + timedelta(days=60)
        easter_days.append(["Fronleichnam       ", dummy])
        
        for i in easter_days:
            print(f"{i[0]}: {i[1].strftime('%d.%m.%Y')}")
        
        
        
