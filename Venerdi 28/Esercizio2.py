#esercizio 2
print("Inserisci 1 per aggiungere un elemento.")
print("Inserisci 2 per rimuovere un elemento.")
print("Inserisci 3 per eliminare tutti gli elementi.")
lista = [1,2,3]
operazione = int(input("Scegli l'operazione da eseguire: "))

if operazione == 1:
    elemento = input("Inserisci l'elemento da aggiungere: ")
    lista.append(elemento)
    print(f"Elemento aggiunto con successo.")

elif operazione == 2:
    elemento = input("Inserisci l'elemento da rimuovere: ")
    if elemento in lista:
        lista.remove(elemento)
        print(f"Elemento rimosso con successo.")
    else:
        print(f"Elemento non trovato nella lista.")
    
elif operazione == 3:
    lista.clear()
    print(f"Tutti gli elementi sono stati eliminati con successo.")
    
else:
    print("Operazione non prevista")