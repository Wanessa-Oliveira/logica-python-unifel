# 03. Decomposição de Tempo (Automação Industrial): Um sensor de esteira
# conta o tempo de operação em segundos. Receba um valor inteiro de segundos
# (ex: 10.000) e decomponha-o em Horas, Minutos e Segundos restantes.
# ● Exemplo: 3661 segundos = 1 Hora, 1 Minuto e 1 Segundo.
# ● Use ferramentas dadas em aulas até aqui. Não use funções prontas

tempo_em_segundos = int(input=("Digite o tempo em segundos: "))
horas = tempo_em_segundos // 3600
resto_segundos = tempo_em_segundos % 3600   
minutos = resto_segundos // 60
segundos_restantes = resto_segundos % 60    
print(f"{tempo_em_segundos} segundos = {horas} Hora(s), {minutos} Minuto(s) e {segundos_restantes} Segundo(s).")
