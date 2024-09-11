'''a. Crie uma lista contendo cinco números inteiros. Adicione um número no final da lista e remova o primeiro número. Em seguida, imprima a lista atualizada.

b. Escreva um programa que encontre o maior e o menor número em uma lista.'''

'''a'''

lista = [1,5,23,64,85]

lista.remove(1)
lista.append(37)

print(lista)

'''b'''

numero = lista[0]

for i in lista:
    if i > numero:
        numero = i

print(numero)