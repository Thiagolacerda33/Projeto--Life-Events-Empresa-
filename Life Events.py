representantes = {
    'São Paulo': 'João Nascimento 94454844',
    'Minas Gerais': 'Kelly Aguiar 987436454 ',
    'Góias': 'Guilherme Dias 99464452',
    'Bahia': 'José Alves 94534168',
    'Rio Grande Do Sul': 'Daniel Alves 94641846'
}
base_publico = {'1': 10000, '2': 20000, '3': 30000}
base_regiao = {'SD': 5000, 'CO': 4000, 'ND': 2000, 'NT': 1000, 'SL': 3000}
base_classe = {'1': 3000, '2': 6000, '3': 12000, '4': 20000}
base_mes = {'1 à 6': 2000, '7 à 10': 1000, '11 e 12': 3000}
cotacao = 0


def mostra_linha():
    print('-' * 80)


while True:
    mostra_linha()
    print(
        'Bem Vindo a Life Events, o nosso atendente virtual tirará suas dúvidas...\nOlá me chamo LifeBot, estou resposável pelo seu atendimento, irei fazer algumas perguntas para efetuar o seu cadastro:'
    )
    mostra_linha()

    nome = input(str('Digite o seu nome:'))
    email = input('Digite o seu email:')
    cnpj = input('Digite o CNPJ:')
    cadastro = nome + cnpj
    print(f'{nome} Seu cadastro foi realizado com sucesso')
    escolha = input(
        str('''Escolha dentre as opções:
  [1] Saber como a contratação do serviço funciona
  [2] Contato com um representante da sua região
  [3] Efetuar cotação\nR:''')).strip()
    if escolha == '1':
        print(
            'LifeBot...\nA cotratação do serviço funciona da seguinte forma, vc preencherá um formulário referente a algumas informações básicas da sua empresa, sendo assim, com as informações preenchidas, iremos analisar e sugerir o melhor evento para sua empresa, baseado nos dados informados. Fazemos conforme o seu querer...'
        )
    if escolha == '2':
        estado = input(
            str('LifBot...\nPara a cotação via representante, segue as seguintes informações:\nAtuamos nos seguintes estados:\n[SP]São Pulo\n[MG]Minas Gerais\n[GO]Góias\n[BH]Bahia\n[RS]Rio Grade do Sul\nDigite a Sigla do seu Estado, caso não temos representante em seu Estado, digite [N]Não\nEstado:'
                )).strip().upper()
        if estado == 'SP':
            print('Representante de São Paulo:', representantes['São Paulo'])
        if estado == 'MG':
            print('Representante de Minas  Geerais:',
                  representantes['Minas Gerais'])
        if estado == 'GO':
            print('Representante de Góias:', representantes['Góias'])
        if estado == 'BH':
            print('Representante da Bahia:', representantes['Bahia'])
        if estado == 'RS':
            print('Representante do Rio Grande do Sul:',
                  representantes['Rio Grande Do Sul'])
        if estado == 'N':
            print(
                'O nosso atendente da central ficará responsável pela a sua consulta:  34694134'
            )
            break
    if escolha == '3':
        print(
            'LifeBot...\nPara realizarmos a cotação, precisamos das seguintes informação:'
        )
        publico = input(
            'Escolha o público estimado para esse evento:\n[1]10.000.00 [2]20.000.00 [3]30.000.00\R:'
        ).strip()
        if publico == '1':
            cotacao += base_publico['1']
        if publico == '2':
            cotacao += base_publico['2']
        if publico == '3':
            cotacao = +base_publico['3']
        regiao = input(
            'Em qual região do Brasil você deseja realizar o evento: [SD] Sudeste [CO] Centro Oeste [ND] Nordeste [NT] Norte  [SL] Sul\R: '
        ).strip().upper()
        if regiao == 'SD':
            cotacao = base_regiao['SD'] + cotacao
        if regiao == 'CO':
            cotacao = base_regiao['CO'] + cotacao
        if regiao == 'ND':
            cotacao = base_regiao['ND'] + cotacao
        if regiao == 'NT':
            cotacao = base_regiao['NT'] + cotacao
        if regiao == 'SL':
            cotacao = base_regiao['SL'] + cotacao
        classe = input(
            'Escolha a classe do Evento\n [1] Básica [2] Média [3] Alta [4] Premium\R:'
        ).strip()
        if classe == '1':
            cotacao = base_classe['1'] + cotacao
        if classe == '2':
            cotacao = base_classe['2'] + cotacao
        if classe == '3':
            cotacao = base_classe['3'] + cotacao

        mes = input(
            'Em qual mês vc deseja realizar o evento [1] Janeiro à Junho [2] Julho à Outubro [3] Novembro à Dezembro \nR: '
        ).strip()
        if mes == '1':
            cotacao = base_mes['1 à 6'] + cotacao
        if mes == '2':
            cotacao = base_mes['7 à 10'] + cotacao
        if mes == '3':
            cotacao = base_mes['11 e 12'] + cotacao
        print(
            f'LifeBot, realizando cotação....\n{nome} a cotação ficou:R${cotacao}, entre em contato com a gente, para finalizarmos a solicitação: 11 960977462'
        )
        break
