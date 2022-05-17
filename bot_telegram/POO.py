# um pouco de POO em python 

class Veiculo:
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo

    def tipoVeiculo(self):
        print(self._nome)

v1 = Veiculo("Carro","Terrestre")

v2 = Veiculo("Caminhao","Terrestre")

v2.tipoVeiculo()

moto = Veiculo("Honda", "Terrestre")
barco = Veiculo("Barco pequeno", "maritimo")


