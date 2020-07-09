class Petshop:
    def __init__(self, nome: str, distancia_canil: float):
        self._distancia_canil = distancia_canil  # A distância do canil ao petshop é dada em quilômetros
        self.nome = nome


class MeuCaninoFeliz(Petshop):
    def __init__(self):
        super().__init__('Meu Canino Feliz', 2)

    def calcular_preco(self, qtde_caes_pequenos: int, qtde_caes_grandes: int, fim_de_semana: bool):
        if fim_de_semana is False:
            return qtde_caes_pequenos * 20 + qtde_caes_grandes * 40
        return 1.2 * (qtde_caes_pequenos * 20 + qtde_caes_grandes * 40)


class VaiRex(Petshop):
    def __init__(self):
        super().__init__('Vai Rex', 1.7)

    def calcular_preco(self, qtde_caes_pequenos: int, qtde_caes_grandes: int, fim_de_semana: bool):
        if fim_de_semana is False:
            return qtde_caes_pequenos * 15 + qtde_caes_grandes * 50
        return qtde_caes_pequenos * 20 + qtde_caes_grandes * 55


class ChowMara(Petshop):
    def __init__(self):
        super().__init__('Chow Mara', 0.8)

    def calcular_preco(self, qtde_caes_pequenos: int, qtde_caes_grandes: int):
        return qtde_caes_pequenos*30 + qtde_caes_grandes*45
