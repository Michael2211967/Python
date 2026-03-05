temperatur_in_celsius = int(input("Geben Sie die Aussentemperatur in Celsius ein: "))
name = input("Geben Sie Ihren Namen ein: ")

if temperatur_in_celsius > 15:
    print(f"Es ist warm. Du brauchst keine Jacke {name}.")
else:
    print(f"Es ist kalt. Du brauchst eine Jacke {name}.")
