from solution import solucao


def testa_saida(pet_nome, pet_valor, pet_nome_esperado, pet_valor_esperado):
    assert (pet_nome, pet_valor) == (pet_nome_esperado, pet_valor_esperado)


def testar_saidas():
    objeto_resposta = {
        '03/08/2018 3 5': ('Meu Canino Feliz', 260),
        '06/07/2020 9 1': ('Vai Rex', 185),
        '07/07/2020 2 2': ('Meu Canino Feliz', 120),
        '08/07/2020 8 4': ('Vai Rex', 320),
        '09/07/2020 6 7': ('Meu Canino Feliz', 400),
        '10/07/2020 8 8': ('Meu Canino Feliz', 480),
        '11/07/2020 3 9': ('Chow Mara', 495),
        '12/07/2020 7 4': ('Vai Rex', 360)
    }
    for key, value in objeto_resposta.items():
        pet_nome, pet_valor = solucao(key)
        testa_saida(pet_nome, pet_valor, value[0], value[1])