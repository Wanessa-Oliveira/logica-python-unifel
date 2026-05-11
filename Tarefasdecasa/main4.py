# 04. Simulador de Investimento com Aporte: Um acionista quer prever seu
# saldo. Receba o valor_inicial e a taxa_rendimento (EM %).
# ● Ex: Se a taxa de rendimento digitada for 5, isso equivale a 5% (converta no
# código para que funcione).
# ● Se o rendimento final (Valor * Taxa) for um número par na sua parte inteira,
# o banco cobra uma taxa de custódia de R$ 10,00.
# ● Se for ímpar, a taxa é de R$ 5,00.
# ● Saída: Exiba o lucro líquido (Rendimento - Taxa) usando o tipo adequado.


valor_inicial = float(input("Digite o valor inicial: "))
taxa_rendimento = float(input("Digite a taxa de rendimento (%): "))

taxa_rendimento = taxa_rendimento / 100

rendimento = valor_inicial * taxa_rendimento

parte_inteira = int(rendimento)

if parte_inteira % 2 == 0:
    taxa_custodia = 10
else:
    taxa_custodia = 5

lucro_liquido = rendimento - taxa_custodia

print("Lucro líquido:", lucro_liquido)

  