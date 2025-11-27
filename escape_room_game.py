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

    global pos_ich_y, pos_ich_x #Copilot hat gesagt, das soll so
    match richtung:
        case "nord":
            print("Du gehst richtung Norden.")
            if(pos_ich_y > 0):
                pos_ich_y -= 1
            else:
                print("Du kannst nicht weiter nach Norden gehen.")

        case "ost":
            print("Du gehst richtung Osten.")
            if(pos_ich_x < 4):
                pos_ich_x += 1
            else:
                print("Du kannst nicht weiter nach Osten gehen.")

        case "süd":
            print("Du gehst richtung Süden.")
            if(pos_ich_y < 5):
                pos_ich_y += 1
            else:
                print("Du kannst nicht weiter nach Süden gehen.")

        case "west":
            print("Du gehst richtung Westen.")
            if(pos_ich_x > 0):
                pos_ich_x -= 1
            else:
                print("Du kannst nicht weiter nach Westen gehen.")

        case _:
            # Fängt falsche Eingaben ab, sonst passiert einfach "nichts"
            print("Falsche Richtung")
            exit() #SPÄTERLÖSCHEN

while True:
    move()
    print ("Du befindest dich in "+karte_eg[etage_ich][pos_ich_y][pos_ich_x])
