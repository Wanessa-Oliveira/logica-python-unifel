# 13. Detector de Pico de Pressão: Um sensor envia um dado. O sistema deve
# exibir "PERIGO" se o valor for estritamente maior que 100, e "OK" caso contrário.
# Proibido usar if.
# ● A tarefa: O sensor às vezes envia o valor como string e às vezes como float.
# O sistema deve saber lidar com ambos.
# ● Além disso, se o dado vier vazio (""), o sistema deve exibir "ERRO DE
# SENSOR" em vez de quebrar.
# ● O Desafio: Resolva usando só expressões lógicas que tratem o valor vazio
# antes de tentar converter para número (para evitar que o programa trave).
# ● Imprima (no final) algo como “Status do Sistema:” + o status devido.
print ("\n")

# string vazia(""), pode ser numero (float) ou pode ser numero (int)...
dado = input (" Digite o dado do sensor: ")

# Operador ternário + comparaçoes logicas ( expressoes lógicas/boleanas)
#CURTO-CIRCUITO
status = (dado == "" and "ERRO DE SENSOR (String Vazia)")
or (float (dado) > 100 and "PERIGO (Float digitado)")
or "OK"

input ("ok")

print ("\n")
print( f" Status do Sistema : {status}")
print("-" * 30)