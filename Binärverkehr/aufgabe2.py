print("Lass uns Schere-Stein-Papier spielen.")

player1 = input("Spieler A wählt: ")
player2 = input("Spieler B wählt: ")

if player1 == "Schere" or player1 == "Stein" or player1 == "Papier" and player2 == "Schere" or player2 == "Stein" or player2 == "Papier":
        if player1 == player2:
            print(f"Unentschieden. Beide haben {player1}")
        elif player1 == "Schere" and player2 == "Stein":
            print("Spieler B gewinnt. Stein schlägt Schere.")
        elif player1 == "Schere" and player2 == "Papier":
            print("Spieler A gewinnt. Schere schlägt Papier")
        elif player1 == "Stein" and player2 == "Schere":
            print("Spieler A gewinnt. Stein schlägt Schere.")
        elif player1 == "Papier" and player2 == "Stein":
            print("Spieler A gewinnt. Papier schlägt Stein.")
        elif player1 == "Papier" and player2 == "Schere":
            print("Spieler B gewinnt. Schere schlägt Papier")
        else:
            print(f"Spieler A: {player1} : Spieler B:{player2}")
        
