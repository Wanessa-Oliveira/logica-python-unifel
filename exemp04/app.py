# exemp04 por que nas boas praticas não se coloca o traço do _ andescullo, mas sim o camelCase
#Operadores Básicos

from decimal import Decimal
#Forma antiga:
#print ("Somma: 10 + 3 = ")
#print (10 + 3)

#String formatada (interpolação )
print (f"Somma: 10 + 3 = {10 + 3}")
print (f"Potencia: 2 ^ 3 = {2 ** 3}")
print (f"Divisão Float: 10 / 3 = {10 / 3}")
print (f"Divisão Inteira (Truncada): 10 // 3 = {10 // 3}")
print (f"Resto da Divisão (Módulo): 10 % 3 = {10 % 3}")
print ("\n\n")

#Sobrecargas de Operadores
print("-" * 30)  # - será impresso 30vezes

#perigo por baixo dos panos do float
print(f"FLOAT 0.8 + 0.1 = {0.8 + 0.1:.20f}") #0.90000000003... oU 0.89834324?

#dECIMAL EXIGE O USO DE ASPAS SIMPLES ''
valor_decimal1 = Decimal('0.8') # SE EU PASSAR SEM ASPAS AI SERIA FLOAT
valor_decimal2 = Decimal("0.1")

print(f"DECIMAL 0.8 + 0.1 = {valor_decimal1 + valor_decimal2}") # 0.9 exato!
print("\n\n")
