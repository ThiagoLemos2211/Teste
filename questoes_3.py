'''Definição e Uso de Funções

a. Crie uma função chamada saudacao que receba um nome como parâmetro e imprima uma saudação personalizada, por exemplo: "Olá, [nome]!".

b. Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma desses números. Teste a função com diferentes valores.'''

'''a'''
def saudacao():
    nome = str(input("Digite um nome: "))
    print(f"Olá, {nome}!")

(saudacao())

'''b'''
def soma():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    return a + b

print(soma())