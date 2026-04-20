from decimal import Decimal
from unicodedata import decimal
import decimal

salario = 5000 # tipo int
bonus_salario = "500" # tipo strig letra

#salario_com_bonus = salario + bonus_salario # tipe error (erro do tipo)
#salario_com_bonus = str(salario) + bonus_salario # slução usar str()

salario_com_bonus = salario + float(bonus_salario) # solução usar int()

#usar concatenação de string (antigo)
#print("\n Salário final : " + str(salario_com_bonus) + "\n" )

#interpolação de string (moderno)
print(f"\n Salário final : {salario_com_bonus} \n" )
