from age import age_calc

prename = input("Wie lautet dein Vorname? ")
name = input("Wie lautet dein Nachname? ")

print(f"Hallo, {prename} {name}!")

birthday = input("Wann bist du geboren? ")

age = age_calc(birthday)

print(f"Du bist aktuell {age} Jahre alt.")

DiffToHundred = 100 - age

print(f"Wow, noch {DiffToHundred} Jahre, dann bist du 100!")
