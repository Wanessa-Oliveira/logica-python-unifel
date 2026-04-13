#print ("Olá, Mundo! Meu primeiro app Python!")

#o que é bytecode no python?#Bytecode é uma representação intermediária do código-fonte Python que é gerada pelo interpretador
#quando um programa Python é executado. O bytecode é uma forma de código que pode ser interpretada pela máquina virtual Python 
# (PVM) para executar o programa. Ele é mais eficiente do que o código-fonte original, pois é otimizado para execução rápida. 
# O bytecode é armazenado em arquivos .pyc ou .pyo, que são gerados automaticamente pelo interpretador quando um módulo é
#  importado pela primeira vez.
#onde fica guardada a instrução otimizada do python?#A instrução otimizada do Python é armazenada em arquivos de bytecode, que são
#  gerados automaticamente pelo interpretador Python quando um módulo é importado pela primeira vez. Esses arquivos de bytecode 
# têm a extensão .pyc ou .pyo e são armazenados em um diretório específico, geralmente chamado __pycache__, dentro do diretório onde
# o módulo original está localizado.(é uma pasta oculta)(.pyc)
# qual a vantagem do python usaar uma maquina virtual?#A vantagem de usar uma máquina virtual em Python é que ela permite que o código 
# Python seja executado em diferentes plataformas
#o python compila o codigo para um arquivo .exe como c# ou c++?#Não, o Python não compila o código para um arquivo .exe como C# ou C++.
#  Em vez disso, o Python é uma linguagem interpretada, o que significa que o código-fonte é executado diretamente pelo interpretador Python.
#  No entanto, existem ferramentas como PyInstaller e cx_Freeze que podem empacotar um programa Python em um arquivo executável (.exe) para facilitar 
# a distribuição, mas isso não é o mesmo que a compilação tradicional de linguagens como C# ou C++.(python compila em tempo real(Runtime))
#se eu deleta a pasta pycache, o que acontece, meu programa para de funcionar?#Se você deletar a pasta __pycache__, o programa Python ainda funcionará 
# normalmente. A pasta __pycache__ é onde o interpretador Python armazena os arquivos de bytecode (.pyc) gerados a partir dos arquivos de 
# código-fonte (.py). se pagar ele vai criar de novo quando o programa for executado novamente. No entanto, a exclusão da 
# pasta __pycache__ pode resultar em um tempo de inicialização ligeiramente mais longo na próxima vez que o programa for executado,
#  pois o interpretador precisará recompilar os arquivos de código-fonte para gerar os arquivos de bytecode novamente.
#python é compilao ou interpretado?#Python é uma linguagem de programação interpretada, o que significa que o código-fonte
#  é executado diretamente pelo interpretador Python,(python é híbrido) sem a necessidade de uma etapa de compilação separada.
#  No entanto, o Python também pode ser compilado para bytecode, que é uma forma intermediária de código que pode ser executada 
# pela máquina virtual Python (PVM). O bytecode é gerado automaticamente pelo interpretador quando um programa Python é executado,
#  e é armazenado em arquivos .pyc ou .pyo para otimizar a execução subsequente do programa.

#a=30
#nome_funcionario = None
#nome_funcionario = "João"
#print(nome_funcionario)

#   def apresentar(self):
  #      print ("Olá,eu sou uma pessoa!")

#jorge_dantas = Pessoa()
#jorge_dantas.apresentar()

# por debaixo dos pano
#Pessoa.apresentar(jorge_dantas) #classe /metodo /objeto





class Pessoa:
    especie = "Ser Humano"

    @classmethod
    def mostrar_especie(cls):
        print(cls.especie)



class Conta:
    def __init__(self):
        self.saldo = 5000 # publico e todos podem acessar esse atributo(variavel de uma classe)!

#fora da classe
conta_falcao = Conta() 
print(conta_falcao.saldo)
conta_falcao.saldo


class Conta:
    def __init__(self):
        self.__saldo = 1000 # protegido (convenção)

    def mostrar_saldo(self):
        print(self.__saldo)

        # outa classe
conta_wanessa = Conta()
print (conta_wanessa.__saldo)
print (conta_wanessa.mostrar_saldo())

print (conta_wanessa._Conta__saldo) # o python muda o nome do atributo para evitar acesso direto e erros de HERANÇA!