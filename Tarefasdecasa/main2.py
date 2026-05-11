# 02. Fintech: Um banco digital quer premiar clientes. Receba três depósitos: d1 =
# 0.1, d2 = 0.1 e d3 = 0.1.
# ● Cálculo: Faça a soma total. Se a soma for exatamente 0.3, exiba "Bônus
# Ativado".
# ● Se não for, exiba "Erro de cálculo, ".
# ● OBS: No final, seu algoritmo deve testar (e provar) se a soma dá
# exatamente 0.3 dentro do print. Deve sair algo como: “Soma correta: True”
 # aprender diferença de decimal e float 
# 👉 o programa faz sozinho:

# cria os valores → soma → compara → mostra resultado

# 👉 ninguém precisa digitar nada
# Porque o objetivo NÃO era interação
# 👉 era testar lógica + precisão de cálculo
from decimal import Decimal

d1 = Decimal("0.1")
d2 = Decimal("0.1")
d3 = Decimal("0.1")

total = d1 + d2 + d3

if total == Decimal("0.3"):
    print("Bônus Ativado")
else:
    print("Erro de cálculo")

print(f"Soma correta: {total == Decimal('0.3')}")


