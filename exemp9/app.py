 #exemp_11: A Herança Dividida (Divisão e Resto Real)
#Cenário: Um investidor deixou 1.000 barras de ouro para 7 herdeiros.
#O que não puder ser dividido igualmente (a sobra) deve ser doado para um museu.
#Objetivo: Calcule quantas barras cada herdeiro recebe e quantas barras serão doadas.

#Saída esperada: "Herdeiros: X barras cada. Museu: Y barras."
# exemp_11: A Herança Dividida

total_barras = 1000
herdeiros = 7

# quanto cada herdeiro recebe
barra_por_herdeiro = total_barras // herdeiros

# sobra para o museu
doacao_museu = total_barras % herdeiros

print("PARTILHA:")
print(f"Herdeiros: {barra_por_herdeiro} barras cada.")
print(f"Museu: {doacao_museu} barras.")
