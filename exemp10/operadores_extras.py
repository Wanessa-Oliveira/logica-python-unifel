a= [1 , 2]
b= [1 , 2]
print (a==b) # true
print (a is b) # false # a e b não são a mesma coisa na memoria pq apontam para locais diferentes ou seja a e b não são o mesmo endereço na memoria

#  se nesse caso abaixo:
b = a # b agora aponta para o memso endereço que a, e o objeto [1,2] de b será destruído!
print (a==b) # true
print (a is b) # true


print("\n\n\n")

#FUNÇÃO BOOL() => mÉtodo que retorna o VALOR LÓGICO do objeto
print(bool(0)) # false
print(bool(1)) # true   
print(bool("")) # false
print(bool(" oi")) # true
print(bool([])) # false
print(bool([1,2,3])) # true