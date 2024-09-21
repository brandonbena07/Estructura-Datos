class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo}"
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo}, Tipo: {self.tipo}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo) 
        self.num_puertas = num_puertas  

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Número de puertas: {self.num_puertas}"


moto = Moto("Yamaha", "MT09", "Deportiva")
carro = Carro("Toyota", "Corolla", 4)
print(moto)
print(carro)