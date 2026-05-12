# exemp_xx (login) :crie duas variaveis user_db = "admin" e pass_db - " 123"
# Recwb via iput o usuario e senha e exiba true se ambos baterem.

user_db = "admin"
pass_db = "123"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

acesso = usuario == user_db and senha == pass_db

print(acesso)

# exemp_xx (Sensor) : Crie um sistema que exiba True se uma temperatura estiver
# entre 20 e 30 graus (faixa ideal). Receba a temperatura do usuario.

temperatura = float(input("Digite a temperatura: "))

ideal = temperatura >= 20 and temperatura <= 30

print(ideal)

# exemp_x (Elegibilidade): Um eleitor só vota se tiver idade entre 16 e 70 anos.
# Receba do usuario a idade, e então
# exiba True ou False para o candidato (teste candidatos com 15 anos,
# e tambem com 75 anos para ver seo código funciona)
idade = int(input("Digite a idade: "))

pode_votar = idade >= 16 and idade <= 70

print(pode_votar)