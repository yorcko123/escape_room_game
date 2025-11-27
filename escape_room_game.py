import random

# --- GLOBALE VARIABLEN ---
# Position des Spielers
etage_ply = 0
pos_ply_y = 4 
pos_ply_x = 2 

# Position des Todes (Gegner)
etage_tod = 0
pos_tod_y = 3
pos_tod_x = 3

# Karte: Liste von Etagen. Jede Etage ist eine Liste von Zeilen.
karte = [
    # Etage 0 (Erdgeschoss)
    [
        ["Garten1",    "Garten2",       "Terasse",     "Zimmer1",       "XX"],           # Zeile 0
        ["Küche1",     "Küche2",        "Wohnzimmer1", "Wohnzimmer2",   "XX"],           # Zeile 1
        ["XX",         "Klo1",          "Flur",        "Schlafzimmer",  "Klo2"],         # Zeile 2
        ["XX",         "Schlafzimmer2", "Garderobe",   "Treppe",        "XX"],           # Zeile 3
        ["XX",         "XX",            "Eingang",     "Abstellkammer", "XX"],           # Zeile 4
        ["XX",         "XX",            "Ende",        "XX",            "XX"]            # Zeile 5
    ],
    # Etage 1 (Keller)
    [
        [".", ".", ".", ".", "."],
        [".", "Küche", ".", "Speisekammer", "."],
        [".", ".", ".", ".", "."],
        [".", "Wohnzimmer", "Treppe", ".", "."], # Treppe ist hier auch bei Y=3, X=2? (Prüf das auf deiner Karte!)
        [".", ".", ".", ".", "."],
        ["XX", "XX", "XX", "XX", "XX"]
    ]
]

def move():
    global pos_ply_y, pos_ply_x # Zugriff auf globale Variablen erlauben
    
    try:
        richtung = input("Wohin möchtest du gehen? (nord, süd, ost, west): ").lower().strip()
    except:
        return 

    print("\n")
    
    match richtung:
        case "nord":
            if pos_ply_y > 0:
                pos_ply_y -= 1
                print("Du gehst Richtung Norden.")
            else:
                print("Da ist eine Wand (Norden).")

        case "ost":
            # Achtung: Breite ist 5, also Index 0-4
            if pos_ply_x < 4: 
                pos_ply_x += 1
                print("Du gehst Richtung Osten.")
            else:
                print("Da ist eine Wand (Osten).")

        case "süd":
            if pos_ply_y < 5: 
                pos_ply_y += 1
                print("Du gehst Richtung Süden.")
            else:
                print("Da ist eine Wand (Süden).")

        case "west":
            if pos_ply_x > 0:
                pos_ply_x -= 1
                print("Du gehst Richtung Westen.")
            else:
                print("Da ist eine Wand (Westen).")

        case "ende":
            exit()

        case _:
            print("Das war keine Himmelsrichtung.")


def raum():
    # WICHTIG: Damit wir die Etage wirklich wechseln können
    global etage_ply, pos_ply_y, pos_ply_x 
    
    # Welches Feld ist es?
    aktuelles_feld = karte[etage_ply][pos_ply_y][pos_ply_x]

    if aktuelles_feld == "Treppe":
        print("!!! Du stehst auf einer Treppe !!!")
        wahl = input("Willst du die Treppe benutzen? (ja/nein): ").lower()
        
        if wahl == "ja":
            if etage_ply == 0:
                etage_ply = 1
                print("Du gehst nach UNTENE in den Keller")
            else:
                etage_ply = 0
                print("Du gehst nach OBEN ins Erdgeschoss.")
            
            # Optional: Man könnte den Spieler hier vom Treppenfeld runterschubsen,
            # damit er nicht sofort wieder gefragt wird.

    elif aktuelles_feld == "Ende":
        print("Herzlichen Glückwunsch! Du hast den Ausgang gefunden!")
        exit()


# --- HAUPTSCHLEIFE ---
while True:
    # 1. Info anzeigen
    inhalt = karte[etage_ply][pos_ply_y][pos_ply_x]
    print(f"Standort: {inhalt} | Koordinaten: Etage {etage_ply}, Y: {pos_ply_y}, X: {pos_ply_x}")
    
    # 2. Bewegen
    move()
    
    # 3. Checken was im neuen Raum passiert
    raum()
