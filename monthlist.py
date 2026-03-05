#! /usr/bin/python3
from datetime import date, datetime, timedelta
from ostertage import ostern, easter_day
from age import age_calc
from locale import setlocale, LC_ALL

setlocale(LC_ALL, '')

def monthlist(year, month):
    monthlist = "Januar Februar März April Mai Juni "
    monthlist += "Juli August September Oktober November Dezember"
    months = monthlist.split()
    print()

    try:
        if int(month) < 13:
            month = int(month)
            day_one = date(year, month, 1)
        else:
            print("Soviele Monate gibt's in Deutschland nicht!")
            
    except:
        if month in months:
            for i, j in enumerate(months):
                if j == month:
                    month = i + 1
            day_one = date(year, month, 1)
        else:
            print(f"Den Monat {month} gibt's in Deutschland nicht!")

    easter_sun = ostern(year)
    easter_days = easter_day(easter_sun)
    easter = easter_days[0]
    
    try:
        day_month = day_one
        mounth_list = []
        while day_one.month == day_month.month:
            mounth_list.append(day_month)
            day_month += timedelta(days=1)
        print(f"{months[month - 1]} {year}")
        birthday = date(year, 11, 22)
        age = age_calc("22.11.1967", birthday)
        micha = f"Michael ({age})"
        for day in mounth_list:
            print(day.strftime("%a, %d.%m."), end=" ")
            for i in easter_days:
                if day == i[1]:
                    easter = i
            
            if day == date.today():
                print("heute", end=" ")
            elif day in easter:
                print(easter[0], end=" ")
            elif day == birthday:
                print(micha, end=" ")
            print()
            
    except:
        print("Monat konnte nicht übernommen werden!!!")

if __name__ == "__main__":
    try:
        year = int(input("Geben Sie das Jahr ein: "))
    except:
        year = date.today().year
    month = input("Geben Sie den Monat ein: ")
    if month == "":
        month = date.today().month
    monthlist(year, month)
