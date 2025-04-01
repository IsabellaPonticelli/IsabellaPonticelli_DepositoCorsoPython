#esercizio 4

nome_utente = "narcisa"
password = "corsopy25"
nome = input("Inserisci nome utente: ")
passw = input("Inserisci password: ")
risp1 = "rosso"
risp2 = "cane"

if nome == nome_utente:
    print("Nome utente corretto")
    if passw == password:
        print("Benvenut*")
        domanda1 = input("Qual è il tuo colore preferito?")
        if domanda1 == risp1:
            domanda2 = input("Qual è il tuo animale preferito?")
            if domanda2 == risp2:
                print("Risposte esatte")
            else:
                print("Risposte errate")
else:
    print("Credenziali errate")
