from datetime import date
# Constantes:
Densidade_gasolina = 0.75
Fator_transformacao_gasolina_em_CO2 = 3.7
CO2_por_arvore = 0.1428571429
Ano_atual = date.today().year
Ano_passado = Ano_atual - 1

print(f'\033[1;31;40mCalculadora de Pegade de Carbono (viagens)\033[m\n')

# pegada de carbono do ano passado
print('\033[1;33m-\033[m' * 50)
print(f'Ano: {Ano_passado}')
nome_empresa = str(input('Digite o nome da sua empresa: '))
distancia_percorrida = float(input('Digite a distância percorrida na viagem (km): '))
qty_viagens = int(input('Quantas viagens dessa são feitas ao ano? '))
qty_passageiros = int(input('Quantos passageiros em média vão nessas viagens? '))

km_litro = float(input('Quantos kms/litro consomem os veículos da sua frota? '))
combustivel_gasto = (distancia_percorrida / km_litro) # cálculo do combustível gasto em uma viagem (l)
combustivel_anual = qty_viagens * combustivel_gasto

# escolha do tipo de combustivel
print('\n1 - Gasolina \n2 - Diesel')
tipo_combustivel = int(input('Digite uma opção com base no menu acima: '))
while tipo_combustivel < 1 or tipo_combustivel > 2:
    tipo_combustivel = int(input('Opção inválida. Digite uma opção com base no menu acima: '))
print('\033[1;33m-\033[m' * 50)

# Total de CO2 emitido
CO2_gasolina = combustivel_anual * 0.82 * Densidade_gasolina * Fator_transformacao_gasolina_em_CO2
CO2_diesel = combustivel_anual * 0.83 * Fator_transformacao_gasolina_em_CO2

if tipo_combustivel == 1:
    CO2 = CO2_gasolina

elif tipo_combustivel == 2:
    CO2 = CO2_diesel

# conversão de CO2 para toneladas
CO2_tonelada_ano_passado = CO2 / 1000
CO2_total_ano_passado = CO2_tonelada_ano_passado * qty_passageiros

# pegada de carbono do ano atual
print(f'Ano: {Ano_atual}')
distancia_percorrida = float(input('Digite a distância percorrida na viagem (km): '))
qty_viagens = int(input('Quantas viagens dessa são feitas ao ano? '))
qty_passageiros = int(input('Quantos passageiros em média vão nessas viagens? '))

km_litro = float(input('Quantos kms/litro consomem os veículos da sua frota? '))
combustivel_gasto = (distancia_percorrida / km_litro) # cálculo do combustível gasto em uma viagem (l)
combustivel_anual = qty_viagens * combustivel_gasto

# escolha do tipo de combustivel
print('\n1 - Gasolina \n2 - Diesel')
tipo_combustivel = int(input('Digite uma opção com base no menu acima: '))
while tipo_combustivel < 1 or tipo_combustivel > 2:
    tipo_combustivel = int(input('Opção inválida. Digite uma opção com base no menu acima: '))
print('\033[1;33m-\033[m' * 50)

# Total de CO2 emitido
CO2_gasolina = combustivel_anual * 0.82 * Densidade_gasolina * Fator_transformacao_gasolina_em_CO2
CO2_diesel = combustivel_anual * 0.83 * Fator_transformacao_gasolina_em_CO2

if tipo_combustivel == 1:
    CO2 = CO2_gasolina

elif tipo_combustivel == 2:
    CO2 = CO2_diesel

# conversão de CO2 para toneladas
CO2_tonelada_ano_atual = CO2 / 1000
CO2_total_ano_atual = CO2_tonelada_ano_passado * qty_passageiros

print(f'\nEmpresa: {nome_empresa}')
print(f'Emissão total de carbono no ano de {Ano_passado}: {CO2_total_ano_passado:.2f}t')
print(f'Emissão total de carbono no ano de {Ano_atual}: {CO2_total_ano_atual:.2f}t')

if CO2_total_ano_atual > CO2_total_ano_passado:
    consumo = CO2_total_ano_atual - CO2_total_ano_passado
    CO2_tonelada = consumo
    print(f'Sua empresa \033[1;31maumentou\033[m suas emissões de carbono em aproximadamente {consumo:.2f}t comparado ao ano passado.\n')
    
    print('\033[33m-=\033[m' * 35)
    print('\033[1;36mhttps://br.investing.com/commodities/carbon-emissions-historical-data\033[m')
    print('\033[33m-=\033[m' * 35)

    valor_credito_carbono = float(input('\nDigite a cotação atual do crédito de carbono buscando no site destacado acima: € '))

    cotacao_euro = float(input('Digite a cotaçaõ atual do euro: € '))
    conversao_real = valor_credito_carbono * cotacao_euro

    print(f'Valor do crédito de carbono: \033[1mR$ {conversao_real:.2f}\033[m\n')

    qty_total_carbono = CO2_tonelada * qty_passageiros
    qty_arvores = qty_total_carbono / CO2_por_arvore
    valor_total_carbono = conversao_real * (CO2_tonelada * qty_passageiros)

    print(f'\033[1mPara compensar sua emissão de CO2, pague R$ {valor_total_carbono:.2f} ou plante {qty_arvores:.0f} árvores.\033[m')

elif CO2_total_ano_passado > CO2_total_ano_atual:
    reducao = CO2_total_ano_passado - CO2_total_ano_atual
    CO2_tonelada = reducao
    if CO2_tonelada >= 1:
        print(f'Sua empresa \033[1;32mreduziu\033[m suas emissões de carbono em aproximadamente {reducao:.2f}t comparado ao ano passado e ganhou {reducao:.0f} crédito(s) de carbono.\n')
    else:
        print(f'Sua empresa \033[1;32mreduziu\033[m suas emissões de carbono em aproximadamente {reducao:.2f}t comparado ao ano passado. \n')

else:
    CO2_tonelada = CO2_total_ano_passado
    print(f'Não houve redução ou aumento na emissão de carbono da sua empresa na comparação entre {Ano_atual} x {Ano_passado}.\n')