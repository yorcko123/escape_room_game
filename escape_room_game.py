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
karte_eg = [
    [
        ["Gartenende",  "Garten",           "Terrasse",     "Büro",             "."],
        ["Küchenende",  "Küche",            "Wohnzimmer",   "Wohnzimmerende",   "."],
        [".",           "Badezimmer",       "Flurende",     "Schlafzimmer",     "Badezimmersuite"],
        [".",           "Kinderzimmer",     "Flur",         "Kellertreppe",     "."],
        [".",           ".",                "Eingang",      ".",                "."]
    ],
         # Etage 1 (Keller)
    [
        [".",     ".",                   ".",                     ".",           "."],
        [".",     ".",                   ".",                     ".",           "."],
        [".",     ".",                   ".",                     ".",           "."],
        [".",     "Ritualraum",          "Abstellraum",          "Kellertreppe", "Tresorraum"], # Habe es gefixt
        [".",     "Keller links Ende",   "Keller links Mitte",   "Kellerflur",   "Keller rechts Ende"]
    ]
]

rooms = [
    {"name":"Eingang", "Beschreibung":"Der Eingang. Vor dir liegt ein Flur."},
    {"name":"Flur", "Beschreibung":"Ein langer Flur. Links und rechts sind Türen. Du kannst weiter in den Flur gehen oder zurück zum Eingang."},
    {"name":"Flurende", "Beschreibung":"Das Ende des Flurs. Es gibt Türen vorne, links und rechts. Du kannst zurück in den Flur gehen."},
    {"name":"Wohnzimmer", "Beschreibung":"Ein großes Wohnzimmer. Es hängen mehrere Gemälde. Links scheint eine große Küche zu sein."
     " Vorne führt eine Tür nach draußen. Du kannst auch weiter ins Wohnzimmer nach rechts gehen oder zurück in den Flur."},
    {"name":"Wohnzimmerende", "Beschreibung":"Das Ende des Wohnzimmers. Es gibt eine Tür vorne. Du kannst auch links ins Wohnzimmer gehen."},
    {"name":"Büro", "Beschreibung":"Ein Büro. Mitten im Raum steht ein Schreibtisch und die Wände sind voller Bücher. Hinter dir ist die Tür zum Wohnzimmer."},
    {"name":"Küche", "Beschreibung":"Eine große Küche. Sie wurde schon lange nicht mehr benutzt. Du kannst weiter nach links gehen oder rechts ins Wohnzimmer."},
    {"name":"Küchenende", "Beschreibung":"Das Ende der Küche. Auf der Arbeitsplatte liegt Besteck. Es gibt eine Tür vorne oder du kannst links in die Küche gehen."},
    {"name":"Terrasse", "Beschreibung":"Eine Holzterrasse. Es gibt ein knarrendes Bodenbrett. Links führt es in den Garten und hinten ins Wohnzimmer."},
    {"name":"Garten", "Beschreibung":"Ein großer Garten. Das Gras ist nass vom Regen. Du kannst links weiter in den Garten gehen oder rechts zurück zur Terrasse."},
    {"name":"Gartenende", "Beschreibung":"Das Ende des Gartens. Es scheint ein kleiner Haufen aufgewühlter Erde zu sein. Hinten gibt es eine Tür oder du kannst rechts in den Garten gehen."},
    {"name":"Kellertreppe", "Beschreibung":"Eine Treppe, die hinunter in den Keller führt."},
    {"name":"Badezimmer", "Beschreibung":"Ein Badezimmer. Die Badewanne ist hinter dem Vorhang versteckt. Du kannst rechts in den Flur gehen oder nach unten."},
    {"name":"Kinderzimmer", "Beschreibung":"Ein Kinderzimmer. Du hattest immer Angst vor dem Platz unter dem Bett. Du kannst nach oben oder rechts gehen."},
    {"name":"Schlafzimmer", "Beschreibung":"Ein durchschnittliches Schlafzimmer. Es gibt ein paar Familienfotos. Du kannst links in den Flur oder links gehen."},
    {"name":"Badezimmersuite", "Beschreibung":"Ein Badezimmer, das ans Hauptschlafzimmer angrenzt. Aus dem Waschbecken tropft rhythmisch Wasser. Da ist etwas drin. Du kannst links gehen."},
    {"name":"Kellerflur", "Beschreibung":"Ein Flur im Keller. Oben führt die Treppe zurück nach oben."},
    {"name":"Keller rechts Ende", "Beschreibung":"Das Ende des Flurs. Oben ist eine Tür."},
    {"name":"Keller links Mitte", "Beschreibung":"Die Mitte des Flurs. Oben ist eine Tür."},
    {"name":"Keller links Ende", "Beschreibung":"Das linke Ende des Flurs. Oben ist eine Tür."},
    {"name":"Tresorraum", "Beschreibung":"Ein Raum im Keller. Am Ende steht ein kleiner Tresor mit Symbolen darüber. Du kannst zurück in den Flur gehen."},
    {"name":"Abstellraum", "Beschreibung":"Nur ein Raum voller Sachen. Nichts fällt auf. Du kannst zurück in den Flur gehen."},
    {"name":"Ritualraum", "Beschreibung":"Ein dunkler Raum mit Symbolen auf dem Boden. Es sieht aus wie ein Pentagon. Es riecht metallisch. Du solltest gehen. Du kannst zurück in den Flur gehen."}
]

items = [
    {"name":"Kellerschlüssel", "Beschreibung":"Ein Schlüssel, der die Tür zum Keller öffnet"},
    {"name":"Eingangsschlüssel", "Beschreibung":"Ein Schlüssel, der die Tür zum Eingang öffnet"},
    {"name":"Brecheisen", "Beschreibung":"Ein stabiles Brecheisen. Gibt es ein loses Brett, das man damit anheben könnte?"},
    {"name":"Löffel", "Beschreibung":"Ein Metalllöffel. Damit hast du früher Erde gegessen."}
]

objekte = [
    {"name":"Tresor", "Beschreibung":"Ein verschlossener Tresor. Du kannst einen vierstelligen Code eingeben. Darüber sind vier Symbole: Ein Zahn, ein Buch, ein Wassertropfen und ein Dämon. Ist das ein Hinweis?"},
    {"name":"Erdehaufen", "Beschreibung":"Ein Haufen Erde mit Maden, die sich darin bewegen. Es scheint etwas darunter zu sein. Du brauchst etwas zum Graben, du willst die Maden nicht anfassen."},
    {"name":"Schädel", "Beschreibung":"Ein Schädel. Du bist dir nicht sicher, ob er echt ist. Er hat sechs Zähne im Mund."},
    {"name":"Waschbecken", "Beschreibung":"Das Waschbecken tropft rhythmisch. Drin liegen zwei Ringe."},
    {"name":"Bücherregal", "Beschreibung":"Es ist voller staubiger Bücher, doch zwei scheinen kürzlich bewegt worden zu sein: 'Sieben Dinge, die du vor deinem Tod tun solltest' und '28 Wege, Handtücher zu falten'."},
    {"name":"Lockernes Bodenbrett", "Beschreibung":"Ein lockeres Bodenbrett. Etwas Stabiles könnte es öffnen."}
]

def move():
    global pos_ply_y, pos_ply_x, etage_ply

    richtung = input("\nWohin möchtest du gehen? (nord/ost/süd/west/treppe) ").strip().lower()
    
    ply_neue_y, ply_neue_x, neue_etage = pos_ply_y, pos_ply_x, etage_ply

    match richtung:
        case "nord": ply_neue_y -= 1
        case "ost":  ply_neue_x += 1
        case "süd":  ply_neue_y += 1
        case "west": ply_neue_x -= 1
        case "treppe":
            # Spezielle Logik: nur an "Kellertreppe" erlaubt
            aktueller_raum = karte_eg[etage_ply][pos_ply_y][pos_ply_x]
            if aktueller_raum == "Kellertreppe":
                neue_etage = 1 - etage_ply  # Wechsel zwischen 0 und 1
                # Setze Position auf der anderen Etage (z. B. gleiche Stelle)
                ply_neue_y, ply_neue_x = 3, 3  # Position der Kellertreppe im Keller
            else:
                print("Hier gibt es keine Treppe!")
                return
        case _: 
            print("Ungültige Richtung!")
            return

    #Habe deine ganzen if-else im match-case zu einer einzelnen Abfrage gemacht
    #checkt ob nächster move gültig ist. Ist es im Kartenbereich? und ist der gewünschte Raum auch ein existiernder Raum?
    if (0 <= neue_etage < len(karte_eg) and
        0 <= ply_neue_y < len(karte_eg[neue_etage]) and
        0 <= ply_neue_x < len(karte_eg[neue_etage][ply_neue_y]) and
        karte_eg[neue_etage][ply_neue_y][ply_neue_x] != "."):
        
        # Bewegung erlaubt
        pos_ply_y, pos_ply_x, etage_ply = ply_neue_y, ply_neue_x, neue_etage
        aktueller_raum = karte_eg[etage_ply][pos_ply_y][pos_ply_x]
        etagen_name = "Erdgeschoss" if etage_ply == 0 else "Keller"
        print(f"\nDu bist jetzt in: {aktueller_raum} ({etagen_name})")
        print(get_room_description(aktueller_raum))
    else:
        print("Dorthin kannst du nicht gehen!")
    
    #variablen neu definiert, um move zu checken, damit man nicht in nicht existierende räume ge = pos_ply_y, pos_ply_x
    
    


def raum():
    # WICHTIG: Damit wir die Etage wirklich wechseln können
    global etage_ply, pos_ply_y, pos_ply_x 
    
    # Welches Feld ist es?
    aktuelles_feld = karte_eg[etage_ply][pos_ply_y][pos_ply_x]

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

        
#checkt den raum von karte_eg, wenn name "." ist, dann wand, dann geht er durch rooms[] durch und schaut ob Name matched. Dann gibt er die beschreibung aus
def get_room_description(room_name):
    if room_name == ".":
        return "Hier ist nichts. Nur eine Wand."
    for room in rooms:
        if room["name"] == room_name:
            return room["Beschreibung"]
    return "Unbekannter Raum."

#Test: Starte am Eingang und zeige Beschreibung
print("=== WILLKOMMEN IM HAUS ===") 
print("Du bist hier, weil deine reiche, gruselige Tante gestorben ist. Du bist auf der Suche nach ihrem Tresor voll Geld. Finde ihn.")
aktueller_raum = karte_eg[etage_ply][pos_ply_y][pos_ply_x]
print(f"Du startest in: {aktueller_raum}")
print(get_room_description(aktueller_raum))
print("-" * 50)


    

#Spielschleife mit linie zur Abschnittsmarkierung
while True:
    # 1. Info anzeigen
    inhalt = karte_eg[etage_ply][pos_ply_y][pos_ply_x]
    print(f"Standort: {inhalt} | Koordinaten: Etage {etage_ply}, Y: {pos_ply_y}, X: {pos_ply_x}")
    
    # 2. Bewegen
    move()
    
    # 3. Checken was im neuen Raum passiert
    raum()
    print("-" * 50)
