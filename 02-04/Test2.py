import random
print("Ciao, tu!")


def verifica_età(età):
    if età >= 18 and età <= 30:
        print("Okay, puoi andare avanti")
        if età == 20:
            print("...But, not a teen anymore :(")
        return True  #L'età è valida, il gioco può partire
    elif età > 30:
        n = 100 - età
        print("Mi dispiace, sei vecchio, tra", n, "anni sarai ai 100!")  
        return True  #Anche sopra i 30 si può continuare
    else:
        print("Mi dispiace, non sei maggiorenne e non puoi andare avanti.")
        return False  #Età inferiore a 18, il gioco non può partire
        
  
lista = [1,2,3,4,5]
def gioco():
    
    while True:
        scelta = input("Lo vuoi un consiglio ecologico? (1 per si/2 per no)")
        if scelta == 2 or scelta.lower() =="no":
            print("Ok, *********!")
            break
        if scelta == 1 or scelta.lower() == "si":
            print("Ecco il consiglio ecologico del giorno: ")
            numero = random.choice(lista) #genera un numero casuale dalla lista
        
            if numero == 1:
                print("Spegni le luci quando esci da una stanza!")
            elif numero == 2:
                print("Usa la borraccia invece delle bottiglie di plastica")
            elif numero == 3:
                print("Pianta un albero!")
            elif numero == 4:
                print("Preferisci i mezzi pubblici!")
            else:
                print("Mangia più verdure e meno carne!")
                
            break  #Esce dal ciclo dopo aver dato il consiglio
            
while True: #questo serve a ripetere il ciclo e a ricominciare
    età = int(input("Quanti anni hai?"))
    if not verifica_età(età):
        break
    gioco() #quindi viene richiamato solo se verifica_età restituisce True
    scelta = input("Vuoi continuare?")
    if scelta.lower() == "no":
        print("Ok, basta consigli per oggi.")
        break
"""     
#Decoratore per stampare un messaggio prima e dopo la funzione
def decoratore(funzione):
    def wrapper():
        print("Inizio della verifica...")
        funzione() 
        print("Fine della verifica.")
    return wrapper


@decoratore
def verifica_età():
    if età >= 18 and età <= 30:
        print("Okay, puoi andare avanti")
        if età == 20:
            print("...But, not a teen anymore :(")
    elif età > 30:
        n = 100 - età
        print("Mi dispiace, sei vecchio, tra", n, "anni sarai ai 100!")  
    else:
        print("Mi dispiace, non sei maggiorenne")

#età = int(input("Quanti anni hai? "))
 """