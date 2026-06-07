# Desafio da mentoria do Codificadas — Resolvendo problemas do Codesforce

> Repositório criado como parte de um desafio de aprendizado: escolher problemas do Codeforces, resolvê-los e documentar toda a jornada.

---

## Problemas escolhidos

| # | Problema | Rating | Link |
|---|----------|--------|------|
| 1 | 339A - Helpful Maths | 800 | https://codeforces.com/problemset/problem/339/A |
| 2 | 71A - Way Too Long Words | 800 | https://codeforces.com/problemset/problem/71/A |
| 3 | 158A - Next Round | 800 | https://codeforces.com/problemset/problem/158/A |

---

## Problema 1 — 339A: Helpful Maths

### O que o problema pede

Xenia está aprendendo adição na escola, mas só consegue calcular uma soma se os números estiverem em ordem não-decrescente. A professora escreveu uma expressão na lousa com apenas os digitos 1, 2 e 3 separados por `+`. A tarefa é reordenar os números e imprimir a expressão corrigida.

**Entrada:** uma string não-vazia contendo digitos 1, 2, 3 e sinais `+`.  
**Saída:** a mesma expressão com os números em ordem não-decrescente.

### Estratégia usada

A string já tem todos os elementos que preciso então só foi preciso separar os digitos dos `+`, ordenar os digitos e reunir tudo de volta com `+` entre eles. Em Python, isso coube em duas linhas usando list comprehension, `sorted()` e `str.join()`.

```
1. Filtrar só os caracteres que não são '+'
2. Ordenar
3. Juntar com '+'
```

### Solução

```python
s = input()

nums = sorted(c for c in s if c != '+')

print('+'.join(nums))
```

### Casos de teste

| Entrada | Saída esperada | Saída obtida |
|---------|---------------|--------------|
| 3+2+1 | 1+2+3 |  1+2+3 |
| 1+1+3+2 | 1+1+2+3 |  1+1+2+3 |
| 3 | 3 |  3 |

---

## Problema 2 — 71A: Way Too Long Words

### O que o problema pede

Dadas **n** palavras, abreviar cada palavra com mais de 10 caracteres no formato:  
`primeira_letra` + `quantidade de letras internas` + `última_letra`

Por exemplo: "internationalization" → "i18n".  
Palavras com 10 ou menos caracteres ficam inalteradas.

**Entrada:** inteiro n, seguido de n palavras.
**Saída:** cada palavra abreviada ou original, uma por linha.

### Estratégia usada

Para cada palavra, verifiquei a quantidade de letras com o comprimento. Se `len(word) > 10`, construí a abreviação como `word[0] + str(len(word) - 2) + word[-1]`. O `-2` descontou a primeira e última letra que já aparecem na abreviação.

### Solução

```python
n = int(input())

for _ in range(n):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
    else:
        print(word)
```

### Casos de teste

| Entrada | Saída esperada | Saída obtida |
|---------|---------------|--------------|
| word | word |  word |
| localization | l10n |  l10n |
| internationalization | i18n |  i18n |

---

## Problema 3 — 158A: Next Round

### O que o problema pede

Em uma competição com **n** participantes, os **k** primeiros avançam para a próxima fase. A pontuação mínima para avançar é igual à pontuação do k-ésimo colocado — mas **com zero ponto ninguém avança**. Quantos participantes avançam?

**Entrada:** n e k, depois as pontuações em ordem não-crescente.  
**Saída:** número de participantes que avançam.

**Detalhe importante:** as pontuações podem ter empates, então mais de k pessoas podem avançar se tiverem a mesma pontuação que o k-ésimo.

### Estratégia usada

1. Identifiquei o limiar com `threshold = scores[k - 1]`;
2. Contei todos os participantes com `score >= threshold` **e** `score > 0`.

O segundo critério `> 0` foi a pegadinha do problema, se o k-ésimo colocado tiver 0 pontos, ninguém com 0 deve avançar.

### Solução

```python
n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k - 1]
count = sum(1 for s in scores if s >= threshold and s > 0)

print(count)
```

### Casos de teste

| Entrada | Saída esperada | Saída obtida |
|---------|---------------|--------------|
| 8 5 / 10 9 8 7 7 7 5 5 | 6 |  6 |
| 5 3 / 0 0 0 0 0 | 0 |  0 |

---

## Linguagem de programação

Usei **Python** para todos os problemas. A escolha foi natural pelo meu contexto de desenvolvimento de projetos para meu portfolio em Python para área de dados e, agora também para engenharia de software. Python também tem sintaxe muito legível, o que ajuda na hora de entender a lógica antes de otimizar.

---

## IA utilizada e como ajudou

Usei o **Claude** como parceiro de aprendizado neste desafio:

- **Seleção dos problemas:** Escolhi alguns e pedi sugestões sobre resolução dos problemas que teriam bom valor didático.
- **Revisão da lógica:** Depois de pensar na estratégia, expliquei meu raciocínio para o Claude e ele confirmou ou apontou casos que eu tinha ignorado.

---

## Dificuldades encontradas

**339A - Helpful Maths:** A lógica é simples, mas o formato de entrada exige atenção. A tentação inicial foi fazer `split('+')` para ordenar e juntar, mas pensar em filtrar os caracteres diretamente com list comprehension foi simples também e pareceu mais limpo.

**71A - Way Too Long Words:** A dificuldade foi lembrar que `len(word) - 2` é o número de letras *internas*, não o comprimento total. Confundi uma vez e o resultado ficou errado por 2 unidades.

**158A - Next Round:** Este foi o mais complexo. O enunciado menciona que participantes com zero ponto não avançam, mas isso não é o comportamento natural da condição `>= threshold`. Se o limiar for zero, precisamos tratar isso separadamente com `and s > 0`. Sem ler com atenção, essa condição passa despercebida.

---

## O que aprendi

- **Ler o enunciado devagar vale mais do que codificar rápido.** Os três problemas tinham pegadinhas em detalhes pequenos que mudam completamente a solução.
- **A IA é melhor como tutor do que como codificador.** Usar o Claude para verificar meu raciocínio em vez de pedir a solução pronta foi muito mais eficaz para o aprendizado.
- **Python oferece simplicidade para manipulação de strings:** list comprehension + `sorted()` + `join()` resolve o 339A em duas linhas legíveis.

---

## Experiência geral

Foi uma experiência surpreendentemente satisfatória. Esperava que problemas de rating 800 fossem mecânicos e sem graça, mas todos tinham pelo menos um detalhe que exigia atenção real.

**O que mais gostei:** o momento "Entendi!" quando entendo *porquê* a condição funciona, não só *que* ela funciona. No 158A, entender que o limiar pode ser zero e que isso muda o comportamento esperado é o tipo de insight que só vem de ler com calma.

**O que foi mais difícil:** resistir ao impulso de pedir logo a solução para o Claude. Forçar-me a tentar primeiro, mesmo sem certeza, foi desconfortável, mas valeu cada segundo.

**Próximos passos:** avançar para problemas de rating 900–1000 com foco em manipulação de strings e lógica condicional mais complexa, antes de entrar em estruturas de dados.

---

## Estrutura do Repositório

```
codeforces-desafio/
├── README.md
└── solutions/
    ├── 339A_helpful_maths.py
    ├── 71A_way_too_long_words.py
    └── 158A_next_round.py
```

---

*Desafio realizado em junho de 2026 · Python · Auxílio: Claude*
