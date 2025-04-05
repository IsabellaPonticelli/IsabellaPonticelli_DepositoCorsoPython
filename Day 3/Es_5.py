# Esercizio 5
comando1= int(input("Inserisci un numero: "))
comando2 = int(input("Inserisci un altro numero: "))
comando3= input("Scegli un'operazione da eseguire tra +, -, *, /: ")

match comando3:
    case "+":
        comando1 + comando2
        print(f"Il risultato dell'addizione è'{comando1 + comando2}'.")
    case "-":
        comando1 - comando2
        print(f"Il risultato della sottrazione è'{comando1 - comando2}'.")
    case "*":
        comando1 * comando2
        print(f"Il risultato della moltiplicazione è'{comando1 * comando2}'.")
    case "/":
        if comando1 == 0 or comando2 == 0:
         print("Errore: Divisione per zero")
        else:
         comando1 / comando2
         print(f"Il risultato della divisione è'{comando1 / comando2}'.")
    case _:
        print("Operazione non riconosciuta")
        