# 71A - Way Too Long Words
# https://codeforces.com/problemset/problem/71/A
#
# Problema: Dado n palavras, abreviar cada uma que tenha mais de 10 caracteres
# no formato: primeira_letra + quantidade_de_letras_do_meio + última_letra.
# Palavras com 10 ou menos caracteres são impressas sem alteração.
#
# Estratégia: Para cada palavra, checar o comprimento. Se len > 10, construir
# a abreviação como word[0] + str(len(word) - 2) + word[-1].
#
# Complexidade: O(n * L) onde L é o comprimento médio das palavras.

n = int(input())

for _ in range(n):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
    else:
        print(word)
