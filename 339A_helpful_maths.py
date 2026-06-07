# 339A - Helpful Maths
# https://codeforces.com/problemset/problem/339/A
#
# Problema: Dada uma expressão de soma como "3+1+2", com apenas os dígitos 1, 2 e 3,
# reordenar os números em ordem não-decrescente e imprimir a nova expressão.
# Xenia só consegue calcular somas quando os parceiros estão em ordem crescente.
#
# Estratégia: extrair apenas os digitos da string,
# ordenar, e reconstruir a string com '+' entre eles.
#
# Complexidade: O(n log n)

s = input()

nums = sorted(c for c in s if c != '+')

print('+'.join(nums))
