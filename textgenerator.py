#! /usr/bin/python3
from datetime import date, datetime

def age_calc(birth):
    today = datetime.combine(date.today(), datetime.min.time())
    day_of_birth = datetime.strptime(birth, "%d.%m.%Y")
    age = today.year - day_of_birth.year

    if today.month < day_of_birth.month or (today.month == day_of_birth.month and today.day < day_of_birth.day):
        age -= 1
    return age

if __name__ == "__main__":
    today = date.today()
    name = input("Geben Sie Ihren Namen ein: ")
    birthday = input("Wann sind Sie geboren? ")
    city = input("Wo wohnen Sie? ")
    age = age_calc(birthday)
    space = 70 * ' '

    print(f"\n{space}{today:%d.%m.%Y}\n")
    print(f"Mein Name ist {name}. Ich bin am {birthday} geboren. Ich bin {age} Jahre alt.")
    print(f"Ich wohne in {city}.")

    input()
