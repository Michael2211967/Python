def lade_fragen(dateiname):
    fragen = {}
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if zeile:
                    frage, antwort = zeile.split(';')
                    fragen[frage.strip()] = antwort.strip()
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
        return {}
    return fragen

if __name__ == "__main__":
    # Testcode, der nur ausgeführt wird, wenn die Datei direkt aufgerufen wird
    geladene_fragen = lade_fragen('testfragen.txt')
    if geladene_fragen:
        print("Geladene Fragen:")
        for q, a in geladene_fragen.items():
            print(f"- {q}: {a}")
    else:
        print("Keine Fragen geladen.")
