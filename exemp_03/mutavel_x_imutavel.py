# Imutáveis(seguro) 
x=10
y=x # y recebe o valor de x, ou seja, 10
x=20


#mutáveis
lista_a = [1 ,2 ,3]
lista_b = lista_a  #as duas listas apontam para o mesmo objeto
lista_a.append(4)  #Isso vai adicionar o numero 4 a lista

#Mputaveis , veja como funciona!
print(f"Mutáveis: LISTA A: {lista_a} | LISTA B: {lista_b}")
print("\n\n")

#efeito espelho

#verificando o endereço de memoria dos objestos (HEAP)
print(f" ID da lista A: {id(lista_a)} | ID da lista b: {id(lista_b)}")
print("\n\n")

#Copiar sem criar um novo objeto C(ópia rasa).Isso cria um novo objeto.

lista_b = lista_a.copy()
#PEGADINHA
lista_1 = [[1, 2],[3, 4]]
lista_2 = lista_1.copy()

print(f"Conteúdo da lista 1: {lista_1} | ID da lista 2: {lista_2}")
print ("\n\n    ")

lista_1[0][0] = 999
print(f"LISTA 1: {lista_1}\n\n")
# 999, 2, 3, 4
# alterou o original, não criou copia 1

# COPIA PROFUNDA :
import copy # para importar qualquer coisa para dentro do arquivo, os import irão ficar no inicio do codigo
lista_2 = copy.deepcopy (lista_1)

