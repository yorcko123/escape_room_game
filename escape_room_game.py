import random

#Das print() wird sofort beim Deklarieren der Klasse ausgeführt. Besser: __init__ überschreiben oder Nachricht beim raise übergeben. Deswegen: Pass
#class InputErr(Exception):
    #pass

#Position des Spielers
#Index aufgeteilt auf die Variablen x und y [4][2]
etage_ich = 0
pos_ich_y = 4
pos_ich_x = 2

#Position des Todes
#Index aufgeteilt auf die Variablen x und y [4][2]
etage_tod = 0
pos_tod_y = 3
pos_tod_x = 3

# karte_eg = Karte Erdgeschoss
# die folgende Karte funktioniert so: oben links in der Ecke startet es mit Index[0][0]
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
    except (EOFError, KeyboardInterrupt):
        print("Eingabe kann nicht verarbeitet werden")
        return # WICHTIG: Bricht hier ab, falls der Input fehlschlägt
    # wir brauchen hier kein try und except, weil die Wildcard (mcase_) sowieso alles abfängt. Die Line mit richtung = reicht vollkommen. 
    # die Exceptions die ich hier eingebaut habe sind für Strg+c oder Strg+d gedacht, falls der User diese Sachen eintippt und das Programm damirt nicht klar kommt


    global pos_ich_y, pos_ich_x 
    # da wir diese Variable außerhalb erstellt haben und diese nun in der Funktion verändern wollen muss klar gestellt werden, dass es sich um die Var von außerhalb handelt und keine neue lokale Variable der Funktion
    match richtung:
        case "nord":
            print("Du gehst richtung Norden.")
            if(pos_ich_y > 0):
                pos_ich_y -= 1 # es muss Minus sein, weil der Index[y] nach oben hin immer kleiner wird
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

if(karte_eg[etage_ich][pos_ich_y][pos_ich_x]):
    



