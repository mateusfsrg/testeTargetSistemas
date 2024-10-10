
def verifica_letra(frase):
    contador = frase.lower().count(letra)

    if contador > 0:
        print(f'A letra {letra} aparece {contador} vezes na frase')
    else:
        print(f'A letra {letra} não foi encontrada.')
frase = input('Digite sua frase: ')
letra = input('Qual letra você quer procurar na frase?')

verifica_letra(frase)