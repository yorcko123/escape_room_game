import random

#Position des Spielers
etage_ich = 0
pos_ich_y = 4
pos_ich_x = 2

#Position des Todes
etage_tod = 0
pos_tod_y = 3
pos_tod_x = 3

karte_eg = [
    [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", "Garderobe", "Treppe", "."],
    [".", ".", "Eingang", ".", "."],
    ["XX", "XX", "Ende", "XX", "XX"]
    ],
    [
    [".", ".", ".", ".", "."],
    [".", "Küche", ".", "Speisekammer", "."],
    [".", ".", ".", ".", "."],
    [".", "Wohnzimmer", "Esszimmer", ".", "."],
    [".", ".", ".", ".", "."]
    ]
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
            print("Du gehst richtung Norden.")
            pos_ich_y -= 1

        case "ost":
            print("Du gehst richtung Osten.")
            pos_ich_x += 1

        case "süd":
            print("Du gehst richtung Süden.")
            pos_ich_y += 1

        case "west":
            print("Du gehst richtung Westen.")
            pos_ich_x -= 1

        case _:
            # Fängt falsche Eingaben ab, sonst passiert einfach "nichts"
            print("Falsche Richtung")

move()
print (karte_eg[etage_ich][pos_ich_y][pos_ich_x])
