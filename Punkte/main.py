import random
def main():
    global punkte
    punkte = int(input("Bitte gebe die Punkteanzahl an! "))
    if(punkte <= 4):
        print("Durchgefallen")
    elif(punkte <= 9):
        print("Bestanden.")
    elif(punkte <= 15):
        print("Bestanden mit auszeichnung!")
    elif(punkte >= 16):
        print("Fehler")
    else:
        print("Bestanden mit auszeichnung")
    main()
main()
    
