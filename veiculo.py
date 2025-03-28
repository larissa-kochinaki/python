class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O veículo acelerou para {self.velocidade} km/h.")

    def mover(self):
        if self.velocidade > 0:
            print(f"O veículo {self.marca} {self.modelo} está se movendo a {self.velocidade} km/h.")
        else:
            print(f"O veículo {self.marca} {self.modelo} está parado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def info(self):
        print(f"Carro: {self.marca} {self.modelo}, Portas: {self.portas}")

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.info()
meu_carro.acelerar(20)
meu_carro.mover()