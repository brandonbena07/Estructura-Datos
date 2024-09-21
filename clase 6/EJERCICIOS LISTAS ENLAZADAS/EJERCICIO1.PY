class Animal:
    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie

    def __str__(self):
        return f"Edad: {self.edad}, Especie: {self.especie}"

class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        nuevo_nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.dato!= animal:
                actual = actual.siguiente
            if actual.dato == animal:
                print("El animal ya existe en la lista.")
            else:
                actual.siguiente = nuevo_nodo

    def mostrar_animales_bucle(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente


zoo = ListaAnimales()
zoo.agregar_animal(Animal( 5, "León"))
zoo.agregar_animal(Animal( 3, "Elefante"))

zoo.mostrar_animales_bucle()