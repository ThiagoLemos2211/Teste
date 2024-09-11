'''a. Crie uma função chamada fatorial que calcule o fatorial de um número inteiro não-negativo.
Lembre-se de que o fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n. Por exemplo, o fatorial de 5 (5!) é 120.'''

def fatorial():

    x = int(input("Digite um número inteiro não negativo: "))

    if x < 0:
        print ("Números negativos não tem fatorial.")
    
    if x == 0:
        print (1)

    resultado = 1
    for i in range(1, x + 1):
        resultado = resultado * i
    print (resultado)

fatorial()