# This Python file uses the following encoding: utf-8

from decimal import Decimal

with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    menor_desemprego = 0
    ocupacao = 0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    for linha in boston.readlines()[1:]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            # print(float(lista[7]))
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
            elif float(lista[7]) <= float(lista[7]):
                menor_desemprego = lista[7]
                ano_menos = lista[0]
                mes_menos = lista[1]
            while float(ocupacao) < float(lista[4]):
                ocupacao = lista[4]
                mes_ocupa = lista[1]
    print("O total de voos é: ", total_voos)
    print("|-----------------------------|")
    print("O mês/ano de maior movimento no aeroporto foi: ",
          str(mes), "/", str(ano))
    print("|-----------------------------|")
    print("O total de passageiros do ano ", ano_usuario,
          "foi de ", total_passageiros)
    print("|-----------------------------|")
    print("O mês do ano ", ano_usuario,
          "com maior média para diária de hotel foi ", mes_maior_diaria)
    print("|-----------------------------|")
    print("A menor % de desempregados em Boston no ano de", ano_usuario,
          "foi no mês", str(mes_menos), "quando ficou em", str(menor_desemprego) + "%")
    print("|-----------------------------|")
    print("No ano de", ano_usuario, "o mês com maior ocupação nos hotéis foi o mês",
          str(mes_ocupa), "com exatamente", ocupacao)
