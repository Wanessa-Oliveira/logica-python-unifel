# 01. Gestão de Estoque Crítico: Uma importadora de hardware precisa de um
# sistema de reposição inteligente. Receba a categoria (string) e a quantidade (int).
# ● Se a categoria for "Acessórios": Repor se estoque estiver menor que 15.
# ● Se a categoria for "Periférico": Repor se estoque estiver menor que 25.
# ● O Desafio: Se a categoria for qualquer outra, o estoque mínimo de
# segurança é sempre 10.
# ● Saída: Exiba "REPOSIÇÃO SOLICITADA" apenas se o estoque estiver abaixo
# do limite para a categoria específica. Caso contrário, exiba "ESTOQUE
# INTEGRAL".

# Raciocinio para desenvolver o codigo: Pense como uma pessoa:

# 👉 “Qual é o limite dessa categoria?”

# se for acessórios → 15
# se for periférico → 25
# se for outro → 10

# 👉 Depois:

# “Tem menos que isso?”

# # sim → repor
# # não → tudo ok
# Sempre escreva antes assim:

# Se categoria for X → limite = Y
# Se categoria for Z → limite = W
# Senão → limite = K

# Se quantidade < limite → repor

# # 👉 Depois vira código  ou seja
# Fica assim:

# Se categoria = "Acessórios"
#     limite = 15

# Se categoria = "Periférico"
#     limite = 25

# Se for qualquer outra categoria
#     limite = 10

# Depois o sistema pergunta:

# quantidade < limite?

# Se sim:

# REPOSIÇÃO SOLICITADA

# Se não:

# ESTOQUE INTEGRAL

# Exemplo:

# Acessórios com 14 → repõe
# Acessórios com 15 → estoque integral

# Periférico com 24 → repõe
# Periférico com 25 → estoque integral

# Teclado com 9 → repõe
# Teclado com 10 → estoque integral

categoria = input(" Digite a categoria do produto: ")
quantidade = int(input(" Digite a quantidade em estoque: "))

if categoria == "Acessórios":
    if quantidade < 15:
        print("REPOSIÇÃO SOLICITADA")
    else:
        print("ESTOQUE INTEGRAL")
elif categoria == "Periférico":
    if quantidade < 25:
        print("REPOSIÇÃO SOLICITADA")
    else:
        print("ESTOQUE INTEGRAL")
else:
    if quantidade < 10:
        print("REPOSIÇÃO SOLICITADA")
    else:
        print("ESTOQUE INTEGRAL")