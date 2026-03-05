#!/usr/bin/python3
name = ""
names = []
sender = input("Wer ist der Absender? ")
while name != "ende":    
    name = input("An wen geht die Nachricht ('ende' eingeben, wenn alle Empfänger eingegeben sind)? ")
    if name != "ende":
        names.append(name)
for name in names:
    print(f"\nHallo {name},")
    print("\nmit dieser E-Mail möchte ich dich über meine neue Adresse informieren")
    print("\n\tMusterstraße 123")
    print("\t12345 Musterhausen")
    print("\nViele Grüße")
    print(f"\n\n\n{sender}\n")
