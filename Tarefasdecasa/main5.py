# 05. Validador de Identidade: Receba dois inputs de texto idênticos, um após o
# outro (ex: o usuário digita "ADM" duas vezes).
# ● Armazene em user1 e user2.
# ● Crie uma lógica que imprima "Mesmo Valor" se o conteúdo das variáveis for
# igual, mas imprima "Objetos Diferentes no Heap " se as variáveis têm
# endereços distintos na memória.

user1 = input (' DIgite "ADM: ')
user2 = input ('DIgite "ADM: ')

if user1                == user2:
    print("Mesmo Valor")
    
    elif user1 is not user2:
    print("Objetos Diferentes no Help") 
