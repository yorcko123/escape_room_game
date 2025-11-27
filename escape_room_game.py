karte = [
    ["Start", "Flur", "Küche", "Vorratskammer", None],       # Zeile 0 (y=0)
    ["Garten", "Flur", "Wohnzimmer", None, None],            # Zeile 1 (y=1)
    ["Werkstatt", None, "Schlafzimmer", "Bad", None],        # Zeile 2 (y=2)
    [None, None, "Balkon", None, None],                      # Zeile 3 (y=3)
    [None, None, None, None, "Ausgang"]                      # Zeile 4 (y=4)
]

def move():
    try:
        richtung = str(input("Wohin möchtest du gehen?"))
    except:
        print("du pisser")
        
    match(richtung):
        
    
move()
      