# nalisador de Triângulos: Receba três lados (A, B e C) de um possível triângulo. Determine se eles podem formar um triângulo e, em caso positivo, defina a sua classificação (se ele é Equilátero, Isósceles ou Escaleno).

# Regra de Existência: Um triângulo só existe se a soma de dois lados for SEMPRE maior que o terceiro lado (independente de quais lados estamos verificando).
# Se (e somente se) o triângulo existir, classificar o tipo com base na igualdade dos lados.
# Equilátero: Todos os 3 lados são iguais.
# Isósceles: Apenas 2 lados são iguais.
# Escaleno: Todos os 3 lados são diferentes.

# OBS: Lados de um triângulo jamais podem ser 0 ou numeros negativos!

# Recebendo os lados do triângulo

print("-" * 30)
print(f"{'ANALISADOR DE TRIÂNGULOS':^30}")
print("-" * 30)

a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
        print("Os lados formam um triângulo!", end=" ")
        #PRINT()=>\\ o fim fe tofo print() é um "\n". O end="" tinha essa quebra de linha!

        # classificação
        if a == b == c:
            print("Triângulo Equilátero!")
        elif a == b or a == c or b == c:
            print("Triângulo Isósceles!")
        else:
            print("Triângulo Escaleno!")

    else:
        print("Os lados NÃO formam um triângulo.")
        print("Um dos lados é maior ou igual à soma dos outros dois.")

else:
    print("Valores inválidos! Os lados devem ser maiores que zero.")

print("-" * 30)