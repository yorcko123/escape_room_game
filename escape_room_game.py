pos_ich = [
    ["0.0", "0.1", "0.2", "0.3", "0.4"],
    ["1.0", "1.1", "1.2", "1.3", "1.4"],
    ["2.0", "2.1", "2.2", "2.3", "2.4"],
    ["3.0", "3.1", "3.2", "3.3", "3.4"],
    ["4.0", "4.1", "4.2", "4.3", "4.4"]
]
pos_tod = [
    ["0.0", "0.1", "0.2", "0.3", "0.4"],
    ["1.0", "1.1", "1.2", "1.3", "1.4"],
    ["2.0", "2.1", "2.2", "2.3", "2.4"],
    ["3.0", "3.1", "3.2", "3.3", "3.4"],
    ["4.0", "4.1", "4.2", "4.3", "4.4"]
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
