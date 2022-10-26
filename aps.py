# Constantes:
Densidade_gasolina = 0.75
Fator_transformacao_gasolina_em_CO2 = 3.7
CO2_por_arvore = 0.1428571429

print('\n\033[1;31;40mCalculadora de Pegade de Carbono (viagens)\033[m\n')

distancia_percorrida = float(input('Digite a distância percorrida na viagem (km): '))
qty_viagens = int(input('Quantas viagens dessa você faz por ano? '))
qty_passageiros = int(input('Quantos passageiros em média vão nessas viagens? '))

km_litro = float(input('Quantos kms/litro seu veículo consume? '))
combustivel_gasto = (distancia_percorrida / km_litro) # cálculo do combustível gasto em uma viagem (l)
combustivel_anual = qty_viagens * combustivel_gasto

# escolha do tipo de combustivel
print('\n1 - Gasolina \n2 - Diesel')
tipo_combustivel = int(input('Digite uma opção com base no menu acima: '))

# Total de CO2 emitido
CO2_gasolina = combustivel_anual * 0.82 * Densidade_gasolina * Fator_transformacao_gasolina_em_CO2
CO2_diesel = combustivel_anual * 0.83 * Fator_transformacao_gasolina_em_CO2

if tipo_combustivel == 1:
    CO2 = CO2_gasolina
elif tipo_combustivel == 2:
    CO2 = CO2_diesel
else:
    print('Opção inválida.')

# conversão de CO2 para toneladas
CO2_tonelada = CO2 / 1000

print(f'\nEmissão anual de carbono por passageiro: {CO2_tonelada:.2f}t.')
print(f'Considerando que {qty_passageiros} passageiros vão nessas viagens, a emissão total de carbono anual será: {CO2_tonelada * qty_passageiros:.2f}t.\n')

print('\033[33m-=\033[m' * 35)
print('\033[1;36mhttps://br.investing.com/commodities/carbon-emissions-historical-data\033[m')
print('\033[33m-=\033[m' * 35)

cotacao_carbono = float(input('\nDigite a cotação atual do Crédito de Carbono buscando no site destacado acima: € '))
cotacao_euro = float(input('Digite a cotaçaõ atual do euro: € '))
conversao_real = cotacao_carbono * cotacao_euro

print(f'\nValor do crédito de carbono: R$ {conversao_real:.2f}\n')

qty_total_carbono = CO2_tonelada * qty_passageiros
qty_arvores = qty_total_carbono / CO2_por_arvore

valor_total_carbono = conversao_real * (CO2_tonelada * qty_passageiros)
print(f'\033[1mPara compensar sua emissão de CO2, pague: R$ {valor_total_carbono:.2f} ou plante {qty_arvores:.0f} árvores.\033[m')
