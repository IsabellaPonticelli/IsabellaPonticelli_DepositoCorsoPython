numero =10
if numero > 0:
    print("Il numero è positivo")
else:
    print("Blocco Else")
     
comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")