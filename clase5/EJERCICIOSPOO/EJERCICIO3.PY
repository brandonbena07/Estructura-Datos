class Vehiculo:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo  

    def __str__(self):
        return f"Vehículo tipo {self.tipo}: {self.marca} {self.modelo}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_moto):
        super().__init__(marca, modelo, "Moto")  
        self.tipo_moto = tipo_moto  

    def __str__(self):
        return f"{super().__str__()}, Tipo específico: {self.tipo_moto}"


class Carro(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo, "Carro")  
        self.num_puertas = num_puertas 

    def __str__(self):
        return f"{super().__str__()}, Número de puertas: {self.num_puertas}"

moto = Moto("Yamaha", "YZF-R3", "Deportiva")
carro = Carro("Toyota", "Corolla", 4)

print(moto)
print(carro)

