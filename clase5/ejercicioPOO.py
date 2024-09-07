class vehiculo:
    def __init__ (self , marca : str , combustible : str ): 
        self . marca = marca
        self . combustible = combustible
    def encender (self):
        pass 
    def arrncar (self):
        pass
    def __str__ (self):
        return f"el vehiculo{self.marca} utiliza con combustible {self. combustible}" 
    
carro = vehiculo ("toyota", "corriente")
print (carro)
print (type(carro))

class moto (vehiculo):
    def __init__ (self, marca: str, combustible: str):
        super (). __init__ (marca, combustible)
    pass 
class carro (vehiculo):
    pass 
motocicleta = moto ("honda", "corriente")
micarro = carro ("mazda", "extra")
print (motocicleta)
print (micarro)
