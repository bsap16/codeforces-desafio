# 158A - Next Round
# https://codeforces.com/problemset/problem/158/A
#
# Problema: Em uma competição com n participantes, os k primeiros avançam de fase.
# A pontuação mínima para avançar é a pontuação do k-ésimo colocado desde que > 0.
# Contar quantos participantes avançam pontuação >= limiar e > 0.
#
# Estratégia: Identificar o limiar como scores[k-1]. Contar todos os participantes
# com score >= limiar e score > 0.
# Atenção: se o k-ésimo colocado tiver 0 pontos, ninguém com 0 avança.
#
# Complexidade: O(n)

n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k - 1]

# Participantes que avançam: pontuação >= limiar E pontuação > 0
count = sum(1 for s in scores if s >= threshold and s > 0)

print(count)
