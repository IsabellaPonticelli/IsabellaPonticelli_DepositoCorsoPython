# Scrivi un programma che chieda all'utente di inserire numeri interi
# fino a quando non inserisce 0, a quel punto il programma calcola la somma 
# di tutti i numeri inseriti e la stampa

somma = 0 #inizializzo una var vuota per fare poi la somma
num = int(input("Inserisci un numero intero: "))

while num != 0: #finchè il numero è diverso da 0
   somma += num #aggiungi il numero a somma
   num = int(input("Inserisci un numero intero: ")) #e chiedi di nuovo l'input
print("La somma è") #sullo stesso livello di while perchè questo è il risultato quando trova 0
print(somma) #il ciclo si ferma e stampa il risultato
