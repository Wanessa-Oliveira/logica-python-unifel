x= [1, 2]
y= x +[3]
print(y) # [1, 2, 3]


#SOBRECARGA DE OPERADORES +  / ==  / * (MUDAM DE ACORDO COM O TIPO DE DADOS)

#mistiras controladas de tipos de dados (int, float, str, list, tuple, dict, set)

print (int ("10")+ 5)
print (str(10)+ "5")

#REPETIÇÃO DE OPERADORES
print("A" *3)
print([1, 2] + 3) # TypeError: can only concatenate list (not "int") to list

#PERTENCIEMNTO
print("a in "banana") # True 
print (4 in [4, 5, 6]) # True