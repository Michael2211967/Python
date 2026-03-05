#!/usr/bin/python3
import time
import sys
import os

def list_file(path):
    try:
        with open(path, 'r', errors='replace') as f:
            lines = f.readlines()   
        
        for i, line in enumerate(lines):
            line = line.rstrip()
            # Prüfen: Hat die Zeile schon eine Nummer? (Typisch für .bas)
            first_word = line.split()[0] if line.split() else ""    
            if first_word.isdigit():
                # Originale Zeile ausgeben
                print(line.upper())
            else:
                # Nostalgie-Nummer hinzufügen (wie dein liste_datum.py)
                print(f"{(i+1)*10} {line.upper()}") 
            time.sleep(0.05) # Ein flüssiges, aber sichtbares Listing
        print("\nREADY.")
    except Exception as e:
        print(f"\n?FILE NOT FOUND ERROR")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "datum.py"
    list_file(target)
