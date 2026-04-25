# Simulador de Aprovação de Crédito
# Objetivo: Desenvolver um algoritmo de decisão lógica para um
# banco digital que determine se um cliente pode ou não receber um empréstimo.


# Tarefas:
# Criar variáveis para armazenar os dados do cliente
# (Renda, Nome Limpo, Fiador e Idade).


# Aplicar as Regras de Negócio usando operadores lógicos e relacionais.
# Exibir o veredito final (True ou False) sobre a decisão de dar ou não o crédito.


# Regras de Negócio (Obrigatórias):

# Regra 1 (Saúde Financeira): O cliente deve ter renda acima de R$ 3.000,00 E o nome deve estar limpo (não negativado).
# Regra 2 (Garantia Alternativa): Se o cliente não passar na Regra 1, ele ainda pode ser aprovado se tiver um Fiador.
# Regra 3 (Restrição Etária): Em qualquer um dos casos acima, o cliente NÃO pode ter menos de 18 anos e maior que 65.

from decimal import Decimal

print("-" * 60)
print("--- SISTEMA DE CRÉDITO | LÓGICA COM PYTHON 2026.3 ---")
print("-" * 60)

# Entrada de dados do cliente
renda = Decimal(input("Digite a renda mensal do cliente: "))
sem_restricao = input("O cliente tem nome limpo? (sim/não): ").lower() == "sim"
tem_fiador = input("O cliente tem um fiador? (sim/não): ").lower() == "sim"
idade = int(input("Digite a idade do cliente: "))

# Regra 1: Saúde financeira
saude_financeira = renda > Decimal("3000") and sem_restricao

# Regra 2: Garantia alternativa
garantia_renda = tem_fiador

# Regra 3: Restrição etária
criterio_idade = idade >= 18 and idade <= 65

# Veredito final
aprovado = criterio_idade and (saude_financeira or garantia_renda)

print("-" * 30)
mensagem = aprovado and " PARABENS! O crédito foi aprovado." or " Infelizmente, o crédito não foi aprovado."
print(f"RESULTADO DA ANALISE: {mensagem}")
print("-" * 30)


