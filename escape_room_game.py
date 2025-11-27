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

# Da man auf seinem Adventure verschiedene 
inventar=[]

# karte_eg = Karte Erdgeschoss
# die folgende Karte funktioniert so: oben links in der Ecke startet es mit Index[0][0]
karte_eg = [
    [
    ["Garten", "Garten", "Terasse", "Büro", "Abstellkammer"],
    ["Küche", "Küche", "Wohnzimmmer", "Wohnzimmer", "Abstellkammer"],
    ["Badezimmer", "Badezimmer", ".", ".", "."],
    [".", ".", "Garderobe", "Treppe", "."],
    [".", ".", "Eingang", ".", "."],
    ["XX", "XX", "Ende", "XX", "XX"]
    ],
    # Warum zwei Karten die identsich wirken?
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
    
    # aktuelle Position wird gespeichert, alle drei Ebenen
    ich_bin_in = karte_eg[etage_ich][pos_ich_y][pos_ich_x]

    print ("Du befindest dich in "+ ich_bin_in)

    #Wenn man in Garten angekommen ist, kann man mit der Umgebung interagieren
    if(ich_bin_in=="Garten"):
        print("Der Garten ist groß, möchtest du ihn noch weiter erkunden? So gehe nach westen")
    
    # an der Stelle [0][0][0] kann man was besonderes machen
    if etage_ich==0 and pos_ich_x==0 and pos_ich_y ==0:
        print ("Die Erde scheint an dieser Stelle weich zu sein. Vielleicht kann man hier as ausgfraben? Möchtest du graben?")
        #das .lower() ist wichtig, damit sowohl ein groß als auch ein kleingeschriebenes Ja bzw. nein angenommen wird
        graben = str(input("ja oder nein?").lower())
        if(graben== "ja"):
            print("Hmm, bisher wurde noch nichts gefunden, möchtest du weiter graben?") 
            weitergraben = str(input("bist du neugiereig oder nicht? ja onder neine?").lower)
            if(weitergraben=="ja"):
                print("Irgendwie sehe ich immer noch nichts? Weitergraben ja oder nein?")
                nochweiter= str(input("Immernoch weitergraben?").lower())
            elif(weitergraben=="nein"):
                print("Du schaufelst das gegrabene Loch wieder zu in gehst zurück zum Haus. Aus dem Augenwinkel siehst du kurz ein Flackern. Zwei gelbe Punkte, die deine jede Bewegung verfolgen")
                if(nochweiter =="ja"):
                    print("Du findest eine Kiste. Diese scheint echt groß zu sein... Woah ok, sie ist so groß wie du selsbt. Wenn du den morschen Deckel öffnest, quitscht dieser in einem unangenehmen hohen Ton, das man die Zähne zusammenbeißt. In der Kiste ist eine Person, Haut geöblicher als die von Frankensteins Monster. Sie ist weiblich und in ihren haöb offenen Mund erkennt man 3 goldene Zähne. Erschrocken lässt du den Deckel wieder fallen. Der Anblick kannst du nicht mehr vergessen")
                if(nochweiter =="nein"):
                    print("völlig außer Atem richtest du dich auf und schaust dir deine Umgebung an. Eigentlich recht hübsch im Garten. Hohe Bäume, große Blumenbeete mit Rosen, Tulpen, Vergissmeinnicht. Und noch vielen weitern Blumen, von denen man den Namen nicht kennt. Hochwertige Gartenmöbel. Der Rasen ist ziemlich hoch, es scheint so als hätte bis vor ein paar Monaten sich noch jemand um diesen Garten gekümmert. Dann gibt es noch ein paar Vogelhäuser und ein schwarzer Schatten, der durch dein Blickfeld huscht... warte was?")
        elif(graben == "nein"):
            print(" du gehst wieder Richtung Haus")
    
    if(ich_bin_in == "Büro"):
        print()






        






