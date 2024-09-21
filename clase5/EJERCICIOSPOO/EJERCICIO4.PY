class Vehiculo:
    def __init__(self, marca, modelo, tipo, combustible, capacidad_tanque):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo  
        self.combustible = combustible  
        self.capacidad_tanque = capacidad_tanque  
        self.encendido = False  

    def encender(self):
        nivel_combustible = self.combustible / self.capacidad_tanque
        if nivel_combustible < 0.10:
            print(f"Advertencia: El {self.tipo} {self.marca} {self.modelo} necesita ir a la gasolinera. Nivel de combustible muy bajo.")
        else:
            self.encendido = True
            print(f"El {self.tipo} {self.marca} {self.modelo} está encendido.")

    def __str__(self):
        return f"Vehículo tipo {self.tipo}: {self.marca} {self.modelo}, Combustible: {self.combustible} galones"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_moto, combustible, capacidad_tanque):
        super().__init__(marca, modelo, "Moto", combustible, capacidad_tanque)
        self.tipo_moto = tipo_moto  

    def __str__(self):
        return f"{super().__str__()}, Tipo específico: {self.tipo_moto}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, num_puertas, combustible, capacidad_tanque):
        super().__init__(marca, modelo, "Carro", combustible, capacidad_tanque)
        self.num_puertas = num_puertas 

    def __str__(self):
        return f"{super().__str__()}, Número de puertas: {self.num_puertas}"


moto = Moto("Yamaha", "YZF-R3", "Deportiva", combustible=1, capacidad_tanque=4) 
carro = Carro("Toyota", "Corolla", 4, combustible=0.5, capacidad_tanque=12) 


print(moto)
print(carro)

print("\nIntentamos encender los vehículos:")
moto.encender()  
carro.encender()  
