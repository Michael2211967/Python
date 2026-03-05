namen = []

while True:
    n = input("Name: ")
    if len(n) == 0 or n == "ende": break
    namen.append(n)

gesucht = input("\nGesucht: ")
found = False

for index in range(len(namen)):
    if namen[index] == gesucht:
        found = True

if found:
    print("Name gefunden")
else:
    print("Name nicht gefunden")

print()
for index in range(len(namen)):
    if namen[index] == gesucht:
        print(f"\u001b[32m{namen[index]}\u001b[0m")
    else:
        print(namen[index])

