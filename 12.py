def contar_vogais(palavra):
    palavra = palavra.lower()
    vogais = 'aeiou'
    return sum(1 for letra in palavra if letra in vogais)

print(contar_vogais("Computador"))
