import fragen_loader
quiz_fragen =  fragen_loader.lade_fragen('quizfragen.txt')
punkte = 0  # Initialisiere den Punktestand

if not quiz_fragen:
    print("Keine Quizfragen geladen. Das Spiel wird beendet.")
else:
    # ... der restliche Code deines Quizspiels bleibt unverändert ...
    for frage, richtige_antwort in quiz_fragen.items():
        print(frage, end=" - ")
        benutzer_antwort = input("Deine Antwort: ")

        # Antwort in Kleinbuchstaben umwandeln, um Groß-/Kleinschreibung zu ignorieren
        benutzer_antwort = benutzer_antwort.lower()
        richtige_antwort = richtige_antwort.lower()

        if benutzer_antwort == richtige_antwort:
            print("Richtig!")
            punkte += 1  # Erhöhe den Punktestand um 1
        else:
            print(f"Falsch. Die richtige Antwort war: {richtige_antwort}")
        print(f"Aktueller Punktestand: {punkte}")
        print("-" * 60)


    print(f"\nQuiz beendet! Dein Endergebnis: {punkte} von {len(quiz_fragen)} Fragen richtig.")
