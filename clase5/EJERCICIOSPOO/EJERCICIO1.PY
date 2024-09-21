class Vehiculo:
    marca: str
    combustible: str

    def __init__(self, m: str, comb: str):
        self.marca = m
        self.combustible = comb

    def encender(self):
        pass

    def arrancar(self):
        pass

    def __str__(self):
        return f"El vehículo {self.marca} utiliza combustible {self.combustible}"

carro = Vehiculo('Mazda', 'Extra')

print(carro)