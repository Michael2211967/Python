file = input("Textdatei zum Öffnen angeben: ")
try:
    file_pointer = open(file, "r")
    print(file_pointer.read())
    file_pointer.close()
finally:
    file_pointer = open(file, "w")
    text = input(f"Eingabe für neue Textdatei {file}: ")
    file_pointer.write(text + "\n")
    file_pointer.close()
