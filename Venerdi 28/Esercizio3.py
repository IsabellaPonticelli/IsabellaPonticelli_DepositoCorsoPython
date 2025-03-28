#esercizio 3
scelta = input("Vuoi creare un account? Si o No? ")


lista_account = []
next_id = 1

if scelta == "Si":
    #Allora crea l'account 
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la password:")
    
    #qui va a inserire i nuovi dati nella lista
    nuovo_account = [next_id, nome, password]
    lista_account.append(nuovo_account)
    
    print(f"Account creato con successo! ID assegnato: {next_id}")
    next_id += 1

    nome = input("Inserisci il tuo nome di nuovo: ")
    password = input("Inserisci la tua password di nuovo: ")
    
    if nome.lower() and password.lower() in nuovo_account:
        print("Account esistente")
