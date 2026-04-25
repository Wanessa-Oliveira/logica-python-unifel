# ENTRADA DE DADOS
preco_vip = 450.00
taxa_conveniencia = 35.00
quant_ingressos = 4

# PROCESSAMENTO
sub_total = preco_vip * quant_ingressos
taxa_total = taxa_conveniencia * quant_ingressos
valor_final = sub_total + taxa_total

# SAÍDA (RECIBO ORGANIZADO)
print("-" * 30)

print(f"{'RECIBO DA COMPRA:^30'}")

print("-" * 30)

print(f"SUB-TOTAL : R$ {sub_total:>8.2f}")
print(f"TAXAS     : R$ {taxa_total:>8.2f}")

print("-" * 30)

print(f"TOTAL     : R$ {valor_final:>8.2f}")

print("-" * 30)