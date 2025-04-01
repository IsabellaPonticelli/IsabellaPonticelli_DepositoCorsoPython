# FUNZIONE CON ESECUZIONE
def saluta(nome): #nome è un parametro 
    print("Ciao,", nome) #questo è il corpo della funzione con le istruzioni
    print("Benvenuto nel nostro programma!")
    

saluta("Isabella") #richiamo della funzione saluta

#FUNZIONE CON VALORE DI RITORNO
def quadrato(numero):
    return numero*numero


risultato = quadrato(4) #dobbiamo sempre salvare il risultato in una variabile
print(risultato) 