Simulador de ATM (Caixa Eletrônico): Peça um valor de saque.
# Verifique se o valor é múltiplo de 10 (operador).
# Se for, use a estrutura apropriada para simular a entrega de notas; se não for,
# avise que a máquina só possui notas de 10, 20 e 50.
# OBS: Emitir o aviso "Saque de alto valor: Verifique o limite diário."
# caso o saque seja MAIOR QUE 500.
# OBS 2: Tem que tratar as notas (10, 20, 50) com MATCH-CASE
valor_saque = int(input("Quanto vai sacar?? (notas de 10, 20 e 50): "))

if valor_saque > 0 and valor_saque % 10 == 0:  # O valor é múltiplo de 10?

    # Decomposição
    # Ex: 130
    # D1 = 130 / 50 = 2
    # Resto D1 = 30
    # D2 = 30 / 20 = 1
    # Resto D2 = 10
    notas_50 = valor_saque // 50  # Quebrando o valor em 50
    resto = valor_saque % 50  # Pegando o resto da divisão acima

    notas_20 = resto // 20  # Quebrando o resto da divisão acima em 20
    resto = resto % 20  # Pegando o resto da divisão acima

    notas_10 = resto // 10  # Quebrando o valor em 50

    print(f"\n Saque autorizado | Valor de: R$ {valor_saque} \n")

    match valor_saque:

        case 10 | 20 | 50:
            print(f" Saque simples: Entregando 1 nota de R$ {valor_saque}")

        case _ if valor_saque > 500:
            print(f"\n Saque de alto valor: Verifique o limite diário \n")

            # Impressões com a decomposição
            if notas_50:  # Truthy / Falsy
                print(f" - {notas_50} notas(s) de R$ 50,00 \n")
            if notas_20:
                print(f" - {notas_20} notas(s) de R$ 20,00 \n")
            if notas_10:
                print(f" - {notas_10} notas(s) de R$ 10,00 \n")

        case _:
            # Impressões com a decomposição
            if notas_50:  # Truthy / Falsy
                print(f" - {notas_50} notas(s) de R$ 50,00 ")
            if notas_20:
                print(f" - {notas_20} notas(s) de R$ 20,00 ")
            if notas_10:
                print(f" - {notas_10} notas(s) de R$ 10,00 \n")
else:
    print(" [ERRO]: Valor inválido!")
    print(" Este caixa só trabalha com notas de 10,00 | 20,00 | 50,00 \n")
    print(" Ou você digitou um valor negativo ou zerado. Tente novamente !! \n")

print("-" * 30)
print("\n")



