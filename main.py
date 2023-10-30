qtd = int(input("Digite uma quantidade de vezes: "))
soma = 0

for n in range(1, qtd):
    int(input(f"Digite o {n}/{qtd}:"))
    soma = soma + n
print(f"O Resultado da soma é {soma}")