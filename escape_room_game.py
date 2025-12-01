import random
import time
import threading

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

#Position Spieler im Sidegame
etage_P = 0
pos_x_P = random.randint(0,4)
pos_y_P = random.randint(0,4)
richt= [(0,1),(0,-1),(1,0),(-1,0)]
rr=random.choice(richt)
nach_x=pos_x_P+rr
nach_y=pos_y_P+rr

def entfernung():
    return abs(pos_ich_x - pos_x_P) + abs(pos_ich_y - pos_y_P)

# Da man auf seinem Adventure verschiedene Items mitnimmt, braucht man ein Inventar
inventar=[]

def nehmen(item): #Item aufnehmen
    inventar.append(item) #Item aufgenommen

timer_abgelaufen = False #globale Variable, die speichert, ob Timer abgelaufen ist oder nicht

def countdown():
    global timer_abgelaufen #damit gesagt, dass man eine globale Var ändern möchte. Ohne erkennt das Programm nicht, dass der Timer abgelaufen ist
    for i in range(30, 0, -1):#zählt immer ein runter
        print(f"\n {i} Sekunden übrig...")  
        time.sleep(1)#timer wartet eine Sekunde

    timer_abgelaufen = True
    print("\n⏰ Zeit ist abgelaufen!\n")

def BlJa_gewonnen():
    print("Nach dem Sieg wird dir schwummrig und deine Vision blurry auf den Bildschirm erkennst du weniger, aber es wirkt so als ob dir zwei gelbe Augen entgegen starren")
    print("Als du erwachst bemerkst du, bist du auf einmal ein Monster, eine Stimme sagt dir, dass du den Spieler fangen sollst")
    print("Fange den Spieler!, du hast 30 sec", 
)
    
    threading.Thread(target=countdown, daemon=True).start() #threads erlauben Timer während Game zu laufen




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

#Karte, die anzeigt in welchen Zimmer man schon gewesen ist
entdeckt =[
    [False for x in range(len(karte_eg[0][0]))]# innere Schleife, erzeugt Spalten pro Zeile, bei karte_eg[0][0] --> erste Spalte; „Erstelle eine Liste mit so vielen Zeilen, wie die Karte hat. Jede Zeile besteht aus so vielen False-Einträgen wie die Karte Spalten hat.“
    for y in range(len(karte_eg[0])) # äußere Schleife, erzeugt Etagen, das karte_eg[0], ist das aktive Geschoss, das len(karte_eg[0]= Anzahl der Zeilen für die ?-Karte)
]

#Funktion, die die neu erforschte Karte anzeigt

def zeige_karte():
    etage = karte_eg[etage_ich] #diese Zeile holt sich die Etage, auf der sich der Spieler befindet
    for y in range(len(etage)): #len(etage) = Anzahl der Zeilen der aktuellen Ebene.
        for x in range(len(etage[y])): #Für jede Zeile (etage[y]) iterierst du über die Spalten. Dann hat sie len(etage[y]) = 5 Spalten -> x läuft von 0 bis 4.
            if entdeckt[y][x]: #hier wird geschaut, ob der Spieler bereits in dem Raum war oder nicht , dementsprechend wird ein ? oder der Raumname ausgegeben
                print(f"[{etage[y][x]:12}]", end=" ")# Raumname ausgegeben und das end sagt kein Zeilenumbruch
            else:
                print("[     ?      ]", end=" ") # Raum noch nicht entdeckt
        print() #Zeilenumbruch
    print() #Abstand zum nachstehenden Text

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

    entdeckt[pos_ich_y][pos_ich_x] = True
    zeige_karte()

    #Wenn man in Garten angekommen ist, kann man mit der Umgebung interagieren
    if(ich_bin_in=="Garten"):
        print("Der Garten ist groß, möchtest du ihn noch weiter erkunden? So gehe nach westen")
    
    # an der Stelle [0][0][0] kann man was besonderes machen
    if etage_ich==0 and pos_ich_x==0 and pos_ich_y ==0:
        print ("Die Erde scheint an dieser Stelle weich zu sein. Vielleicht kann man hier as ausgfraben? Möchtest du graben?")
        #das .lower() ist wichtig, damit sowohl ein groß als auch ein kleingeschriebenes Ja bzw. nein angenommen wird
        graben = str(input("ja oder nein?").lower())
        if graben == "ja":
            print("Hmm, bisher wurde noch nichts gefunden, möchtest du weiter graben?") 
            weitergraben = input("Bist du neugierig? ja oder nein? ").lower()

            if weitergraben == "ja":
                print("Irgendwie sehe ich immer noch nichts... weitergraben?")
                nochweiter = input("Immernoch weitergraben? ja oder nein? ").lower()

                if nochweiter == "ja":
                    print("Du findest eine Kiste. Sie ist riesig... Im Inneren liegt eine Person mit, toter gelber Haut, gelber als Frankensteins Monster und 3 goldenen Zähnen. Erschrocken wirfst du den Deckel zu.")
                else:
                    print("Völlig außer Atem richtest du dich auf und schaust dich um...")
    
            else:
                print("Du schaufelst das Loch wieder zu und gehst zurück zum Haus.")
                print("Aus dem Augenwinkel siehst du zwei gelbe Punkte, die dich anschauen...")

        elif graben == "nein":
            print("Du gehst wieder Richtung Haus.")

    
    
#Raum Büro
    if(ich_bin_in == "Büro"):
        print("Dieser Raum sieht ziemlich unordentlich aus, überall liegen Papiere herum auf den Boden, Tischen. Die Gardinen sind halb zugezogen vielleicht ist hier etwas zu finden")
        print("Möchtest du etwas durchsuchen? Schreibtisch, Regale, Computer")
        Entscheidung_Büro= str(input("Was möchtest du dir anschauen?").lower())
        if (Entscheidung_Büro == "schreibtisch"):
            print("Du öffnest alle möglichen Schubladen und findest viele Büromaterialien. Darunter eine Büroklammer, möchtest du sie mitnehmen?")
            Büroklammern_mitnehmen= str(input("ja oder nein?").lower())
            if(Büroklammern_mitnehmen=="ja"):
                nehmen("Büroklammern")
            else: 
                print("Du schließt die Schublade wieder")
        elif(Entscheidung_Büro=="regale"):
            "Du siehst ein massiven Bücherschrank, der förmlich mit Büchern überquilt. Verscheidene Genre mehrfach vertreten, jedoch sind Horrorbücher nur 5 mal vorhanden"
        elif(Entscheidung_Büro == "computer"):
            print("Gib das Passwort ein:")
            passwort=str(input("Passwort:"))
        if(passwort=="Frankenstein"):
            print("Du öffnest den Computer und du befindest dich in einem Spiel BlackJack. Der Dealer gegenüber hat eine 7")
            zahlen=random.randint(4,21)
            print("Deine Zahlen sind summiert sind:",zahlen , "hit oder stand?")
            hit=(str(input("ja oder nein?")).lower())
            if(hit=="ja"):
                zahl3=random.randint(4,21)
                print ("Deine dritte Karte ist:",zahl3 )
                
                if(zahlen+zahl3>21):
                    print("Leider verloren")
                else:
                    print("Gewonnen!")
                    BlJa_gewonnen()
            if(hit=="nein" and zahlen+zahl3>17<=21):
                print("Gewonnen")
                BlJa_gewonnen()
                dist=entfernung()
                if(dist==0):
                    print("Du hast den Spieler gefangen")
                elif(dist==1):
                    print("Du hörst Schritte im Nebenraum")
                elif(dist==2):
                    print("Es sind entfernte Geräusche zu hören")
            else:
                print("Leider verloren")
        else:
            print("Falsch, suche woanders weiter")
    else:
        print("Du verlässt den Raum")










        






