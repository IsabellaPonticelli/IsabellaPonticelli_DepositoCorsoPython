#esempi di liste
numeri = [1, 2, 3, 4, 5]
nomi= ['Alice', 'Bob', 'Charlie']
misto = [1, 'due', True, 4.5]

print(numeri[3])
print(nomi[2])
#se voglio cambiare un valore scrivo il nome della lista
# e tra parentesi quadra indico la posizione e il valore nuovo da assegnare
print(numeri)
numeri[2]= 10
print(numeri)

numeri = [3,1,4,2,5]

print(len(numeri)) #lunghezza della lista
numeri.append(6) #aggiungi il numero 6 alla fine
print(numeri)
numeri.insert(2,10) #inserisci in posizione 2 il valore 10
print(numeri)
numeri.remove(4) #rimuove quel valore indicato non la posizione
print(numeri)
numeri.sort(reverse=True) #ordina per ordine numerico
print(numeri)
numeri.pop
print(numeri)