import random

pos_ich = [4,2]
pos_tod = [2,4]

eg = True

karte_eg = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", "Treppe", "."],
    [".", ".", "Eingang", ".", "."]
]

def move():
    try:
        # .lower() ist wichtig, damit "Nord" auch als "nord" erkannt wird
        richtung = input("Wohin möchtest du gehen? ").lower()
    except:
        print("du pisser")
        return # WICHTIG: Bricht hier ab, falls der Input fehlschlägt

    match richtung:
        case "nord":
            print("du kek")

        case "ost":
            print("du kek")

        case "süd":
            print("du kek")

        case "west":
            print("du kek")

        case _:
            # Fängt falsche Eingaben ab, sonst passiert einfach "nichts"
            print("Falsche Richtung")

move()
print (karte_eg[4][2])
