#Esempio di variabili e strutture dati 
nome = "Isa"
anni = 26
float = 3.14159

tuplaACaso = ("Sara", 3, "Ciao", 123)
set1 = {6,10,20,3,5} 
listaAcaso = [1, 2, 3, 4, 5]

#Ciclo for
for x in listaAcaso:
    print(x)
    
#Ciclo for con range 
for x in range(0,10,-1): #per ogni elemento x nel range che va da 0 a 10, al contrario
        print(x)

#if,elif,else
print("Ciao, tu!")
età = int(input("Quanti anni hai?"))

if età >= 18 and età <= 30:
    print("Okay, puoi andare avanti")
    if età == 20:
        print("...But, not a teen anymore :(")
elif età > 30:
    n = 100 - età
    print("Mi dispiace, sei vecchio, tra", n, "anni sarai ai 100!")  
else:
    print("Mi dispiace, non sei maggiorenne")

#Esempio di un ciclo while
contatore = 0
while contatore < 5:
    print(contatore)
    contatore += 1
    print("Sei arrivato a", contatore)

#Esempio di come si definisce una funzione e dei metodi incorportati per le stringhe
def funzioneXstringhe():
    s = "Hello world!"
    print("Stringa maiuscola:", s.upper())
    print("Stringa minuscola:", s.lower())
    print("Lunghezza della stringa:", len(s))
    print("Stringa modificata in:", s.replace('world', 'universe'))

#Esempio match 
input_utente =int(input("Scegli tra le due opzioni (1/2):"))
print("1. Cena fuori.")
print("2. Netflix e divano")
            
match input_utente:
    case 1:
        print("Ok, ma paghi tu.")
    case 2:
        print("Adesso si usa StreamingCommunity.")
    case _:
        print("Non è quello che ti ho chiesto.")
 
#Decoratore
def decoratore(funzione):
    def wrapper():
        print("Sto per eseguire la funzione...")
        funzione()  # Chiama la funzione originale
        print("Funzione eseguita!")
    return wrapper

@decoratore
def funzioneXstringhe():
    s = "Hello world!"
    print("Stringa maiuscola:", s.upper())
    print("Stringa minuscola:", s.lower())
    print("Lunghezza della stringa:", len(s))
    print("Stringa modificata in:", s.replace('world', 'universe'))
    
funzioneXstringhe()

