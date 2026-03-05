shoppinglist = list()
option = None

while option != 8:
    print("******************************")
    print("*   Einkaufslisten-Manager   *")
    print("******************************")
    print()
    print("1. Liste anzeigen")
    print("2. Artikel hinzufügen")
    print("3. Artikel entfernen")
    print("4. Liste sortieren")
    print("5. Liste umkehren")
    print("6. Artikel suchen")
    print("7. Anzahl der Artikel")
    print("8. Programm beenden")
    print()
    try:
        option = int(input("Wählen Sie eine Option (1 - 8): "))
    except:
        pass
    
    if option == 1:
        print()
        print("   Ihre Einkaufsliste:")
        print("   -------------------")
        print()
        if len(shoppinglist) > 0:
            for item in range(len(shoppinglist)):
                print(f"{item + 1}. {shoppinglist[item]}")
        else:
            print("Ihre Einkaufsliste ist leer")
        print()
    elif option == 2:
        print()
        shoppingItem = input("Geben Sie einen Artikel ein: ")
        if shoppingItem not in shoppinglist:
            shoppinglist.append(shoppingItem)
            print(f"{shoppingItem} wurde der Einkaufsliste hinzugefügt")
            print()
        else:
            print(f"{shoppingItem} ist in der Einkaufsliste bereits enthalten")
            print()
    elif option == 3:
        print()
        shoppingItem = input("Welchen Artikel wollen Sie aus der Einkaufsliste entfernen? ")
        if shoppingItem in shoppinglist:
            shoppinglist.remove(shoppingItem)
            print(f"{shoppingItem} wurde erfolgreich aus der Einkaufsliste gelöscht")
            print()
        else:
            print(f"{shoppingItem} ist nicht vorhanden")
            print()
    elif option == 4:
        shoppinglist.sort()
    elif option == 5:
        shoppinglist.reverse()
    elif option == 6:
        print()
        shoppingItem = input("Welchen Artikel wollen Sie suchen? ")
        if shoppingItem in shoppinglist:
            print(f"{shoppingItem} ist in der Einkaufsliste enthalten")
        else:
            print(f"{shoppingItem} ist nicht in der Einkaufsliste enthalten")
        print()
    elif option == 7:
        print()
        print(f"In der Einkaufsliste sind aktuell {len(shoppinglist)} Artikel enthalten")
        print()
    elif option == 8:
        pass
    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine Option zwischen 1 und 8")
print()
print("Programm wird beendet. Auf Wiedersehen!")
