lista = []


while len(lista) < 5:
    num = int(input("Inserisci un numero: "))
    if num % 2 == 0:
        print(f"Il numero '{num}' è pari")
        lista.append(num)
    else:
        print("Il numero '{num}' non è pari")
        
print("Ora ci sono 5 numeri pari.")