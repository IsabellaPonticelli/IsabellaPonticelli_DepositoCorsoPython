
def quadrato():
    numero = int(input("Dammi un numero: "))
    numero*numero
    print (f"Il quadrato è '{numero*numero}'")
    
#quadrato()
    
lista = [1, 3, 4, 7, 10]

def somma_lista(lista):
    somma = 0
    for numero in lista:
        somma += numero 
    print(f"La somma è '{somma}'")

#somma_lista(lista) 

while True: #questo serve a ripetere il ciclo e a ricominciare
    quadrato()
    somma_lista(lista)
    scelta = input("Vuoi continuare?")
    if scelta == "no":
        break
    