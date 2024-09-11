'''Estruturas Condicionais

a. Escreva um programa que receba um número do usuário e verifique se ele é par ou ímpar. Exiba uma mensagem apropriada.

b. Escreva um programa que receba a nota de um aluno e determine se ele foi aprovado, reprovado ou se está em recuperação. As notas são consideradas da seguinte forma:

Aprovado: Nota >= 7
Recuperação: Nota entre 5 e 6.9
Reprovado: Nota < 5'''

'''a'''
numero = int(input("Coloque um número inteiro, para que o programa o descreva como par ou impar: "))

if numero % 2 == 0:
    print("Seu número é par")
else:
    print("Seu número é impar")

'''b'''
nota = float(input("Insira a nota do aluno: "))

if nota >= 7 < 10:
    print("Aprovado")
elif nota >= 5 < 7:
    print("Recuperação")
elif nota < 5:
    print("Reprovado")