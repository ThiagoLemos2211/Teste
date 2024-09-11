'''a. Crie um dicionário para armazenar informações sobre um livro, incluindo o título, autor e ano de publicação. Imprima cada uma dessas informações.

b. Escreva um programa que conte a frequência de cada caractere em uma string fornecida pelo usuário e armazene essas frequências em um dicionário.
'''

livro = {'Título': '', 'Autor': '', 'Ano_Publicação': ''}

livro['Título'] = 'Neuromancer'
livro['Autor'] = 'William Gibson'
livro['Ano_Publicação'] = '1984'

# livro['Título'] = 'Cidade nas Estrelas'
# livro['Autor'] = 'Arthur C. Clarke'
# livro['Ano_Publicação'] = '1956'

# livro['Título'] = 'Frankenstein'
# livro['Autor'] = 'Mary Shelley'
# livro['Ano_Publicação'] = '1818'

print(livro)

'''b'''

frase = str(input("Digite uma frase: "))

def contador(frase):
    dicionario = {}
    for i in frase:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario

resultado = contador(frase)

for i, contador in resultado.items():
    print(f"{i} : {contador}")