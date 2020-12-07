Punkte = int(input("Bitte gebe die Punkteanzahl an! "))
if(Punkte <= 4):
    print("Durchgefallen")
elif(Punkte <= 9):
    print("Bestanden.")
elif(Punkte <= 15):
    print("Bestanden mit auszeichnung!")
elif(Punkte >= 16):
    print("Fehler")
else:
    print("Bestanden mit auszeichnung")