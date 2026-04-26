# Simular um sistema que controla o acesso/clima de um evento da UNIFEL
# Caso 1: VALIDAÇÃO COM IN
convidados = ["jorge", "genaldo", "ewerton", "denise", "falcao", "milena"]
usuario = input(" Digite seu nome: ").lower()

if usuario in convidados:
    print(" LIBERADO! Seja bem-vindo ao evento!")

    # Aninhamento (um if dentro de outro)
    idade = int(input(" Qual sua idade? "))
    if idade >= 18:
        print("Você recebeu uma pulseira da área VIP! \n")
    else:
        print("Você recebeu uma pulseira da área KIDS (infantil)! \n")

else:
    print("ACESSO NEGADO. Seu nome não consta na lista. Procure a rececpção!")
print("-" * 30)