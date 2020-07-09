from datetime import datetime
from petshops import MeuCaninoFeliz, VaiRex, ChowMara


def encontra_dia_semana(data_string):
    dia, mes, ano = tuple(map(lambda string: int(string), data_string.split('/')))
    date = datetime(day=dia, month=mes, year=ano)
    return ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO'][date.weekday()]


def mais_viavel(meu_canino_feliz: "MeuCaninoFeliz", vai_rex: "VaiRex", chow_mara: "ChowMara", qtde_pequenos: int,
                qtde_grandes: int, fim_de_semana: bool):
    preco_meu_canino_feliz = meu_canino_feliz.calcular_preco(qtde_pequenos, qtde_grandes, fim_de_semana)
    preco_vai_rex = vai_rex.calcular_preco(qtde_pequenos, qtde_grandes, fim_de_semana)
    preco_chow_mara = chow_mara.calcular_preco(qtde_pequenos, qtde_grandes)
    lista_precos = [preco_meu_canino_feliz, preco_vai_rex, preco_chow_mara]
    menor_preco = min(lista_precos)
    qtde_menor_preco = lista_precos.count(menor_preco)
    if qtde_menor_preco == 1:
        index_menor_preco = lista_precos.index(menor_preco)
        if index_menor_preco == 0:
            pet_viavel = meu_canino_feliz.nome
        elif index_menor_preco == 1:
            pet_viavel = vai_rex.nome
        else:
            pet_viavel = chow_mara.nome
    elif qtde_menor_preco == 2:
        if lista_precos[0] == menor_preco and lista_precos[1] == menor_preco:
            pet_viavel = vai_rex.nome
        else:
            pet_viavel = chow_mara.nome
    else:
        pet_viavel = chow_mara.nome
    return pet_viavel, menor_preco


def solucao(entrada: str):
    data_string, pequenos, grandes = entrada.split()
    qtde_pequenos, qtde_grandes = int(pequenos), int(grandes)
    dia_semana = encontra_dia_semana(data_string)
    fim_de_semana = True if dia_semana == 'SABADO' or dia_semana == 'DOMINGO' else False
    meu_canino_feliz, vai_rex, chow_mara = MeuCaninoFeliz(), VaiRex(), ChowMara()
    return mais_viavel(meu_canino_feliz, vai_rex, chow_mara, qtde_pequenos, qtde_grandes, fim_de_semana)