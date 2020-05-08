#
lista = [5,10,22,45,30,92,88,34,55]
print(lista[0])

#soma
soma = 0
for elemento in lista:
    soma += elemento
print(soma, sum(lista))

#soma pares
for elemento in lista:
    if elemento % 2 == 0:
            par += elemento
        else:
            impar += elemento
print(f'soma impar: {impar} /n' 
        f'soma par: {par}')  

# quantidade elemento
cont = 0
for item in lista
    cont +-1
print(cont, len(lista))

# mostra indice par
for indice in range(0,len(lista),2):
    print(lista[indice])

# mostra indice impar
for indice in range(1,len(lista),2):
    print(lista[indice])

