# Scrivi un programma che utilizzi un ciclo for con range per stampare
# fino ad un massimo di N scelto dall'utente, con step scelto dall'utente

N = int(input("Inserisci il valore massimo N: ")) #inizializzo con input i parametri del range
step = int(input("Inserisci il valore dello step: "))

for x in range(0, N, step): #se volessimo N compreso sarebbe N+1
    print(x)

