#sinal = input("Digite a cor: ").strip().lower()

#if sinal == "verde":
 #   print("Pode passar")
#elif sinal == "amarelo":
#    print("Atenção")
#elif sinal == "vermelho":
#    print("Pare")
#else:
#    print("Cor inválida")


# condicional aninhada de faixa etária

# idade = int(input("Digite sua idade: "))

# if idade < 18:
#     print("menor de idade")

# elif idade >= 18 and idade <= 20:
#     print("saindo da adolescência")

# elif idade >= 21 and idade < 29:
#     print("adulto jovem")

# elif idade >= 29 and idade < 45:
#     print("maduro")

# elif idade >= 45 and idade < 50:
#     print("meia idade")

# elif idade >= 50 and idade < 60:
#     print("senhor")

# else:
#     print("idoso")

# IF TERNARIO (3)
idade = 15
    if idade >= 18:
        status = "pode entrar"
    else:
        status = "não pode entrar"

    #IF TERNARIO (1) ( só serve para uma condição ou seja if simples)
status = "pode entrar" if idade >= 18 else "não pode entrar"

# A ordem dos fatores altera o produto (elif)
# if para na verdade (verdade unica )

# erro : 0 70 anos entra no primeiro if e nunca chegara no idoso
if idade>= 18:
    print("adulto")
elif idade >= 65 # nunca sera testado se idade for maior que 18!
    print("idoso")

#certo (sempre da maior restrição para a menor):
if idade >= 65 :
print("idoso") 
elif idade >= 18:
print("adulto")




