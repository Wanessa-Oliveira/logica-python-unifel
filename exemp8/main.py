#exemp8: cashback do E-commerce (Sbrecarga de operadores)
#Cenário: Uma loja quer gerar uma barra de progresso visual para o cashback do cliente.
#Objetivo : O cliente ganhou 10 pontos. Cada ponto vale um caractere "█".

# Desafio : Crie a barra de progresso usando " multiplicação de strings"
#e cocatene com a porcentagem final.

# saída esperada : Progressão : [ ██████████ ]100% (Use o + para colar os textos).

print("-" * 30)
print()

pontos = 10
ponto_barra_progressao = "█"   # caractere visível
porcentagem = "100%"

# criando a barra
barra_visual = ponto_barra_progressao * pontos

# concatenação
barra_final = "Progressão: [" + barra_visual + "] " + porcentagem
print(barra_final)

# usando f-string (melhor forma)
barra_final = f"Progressão: [{barra_visual}] {porcentagem}"
print(barra_final)

print()
print("-" * 30)