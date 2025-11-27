import random

pos_ich_y = 4
pos_ich_x = 2

pos_tod_y = 3
pos_tod_x = 3

eg = True

karte_eg = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", "Garderobe", "Treppe", "."],
    [".", ".", "Eingang", ".", "."]
]

def move():
    try:
        # .lower() ist wichtig, damit "Nord" auch als "nord" erkannt wird
        richtung = input("Wohin möchtest du gehen? ").lower()
    except:
        print("du pisser")
        return # WICHTIG: Bricht hier ab, falls der Input fehlschlägt

    global pos_ich_y, pos_ich_x
    match richtung:
        case "nord":
            print("du kek")
            pos_ich_y -= 1

        case "ost":
            print("du kek")
            pos_ich_x += 1

        case "süd":
            print("du kek")
            pos_ich_y += 1

        case "west":
            print("du kek")
            pos_ich_x -= 1

        case _:
            # Fängt falsche Eingaben ab, sonst passiert einfach "nichts"
            print("Falsche Richtung")

move()
print (karte_eg[pos_ich_y][pos_ich_x])
