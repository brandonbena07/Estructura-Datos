class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.next = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        if self.es_vacio() or (self.cabeza.prioridad < prioridad) or (self.cabeza.prioridad == prioridad and self.cabeza.fecha_vencimiento > fecha_vencimiento):
            nueva_tarea.next = self.cabeza
            self.cabeza = nueva_tarea
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None and (nodo_actual.next.prioridad > prioridad or (nodo_actual.next.prioridad == prioridad and nodo_actual.next.fecha_vencimiento <= fecha_vencimiento)):
                nodo_actual = nodo_actual.next
            nueva_tarea.next = nodo_actual.next
            nodo_actual.next = nueva_tarea

    def eliminar_tarea_por_descripcion(self, descripcion):
        nodo_actual = self.cabeza
        if nodo_actual is not None:
            if nodo_actual.descripcion == descripcion:
                self.cabeza = nodo_actual.next
                return
            while nodo_actual.next is not None:
                if nodo_actual.next.descripcion == descripcion:
                    nodo_actual.next = nodo_actual.next.next
                    return
                nodo_actual = nodo_actual.next

    def eliminar_tarea_por_posicion(self, posicion):
        nodo_actual = self.cabeza
        if posicion == 0:
            self.cabeza = nodo_actual.next
            return
        contador = 0
        while nodo_actual is not None and contador < posicion - 1:
            nodo_actual = nodo_actual.next
            contador += 1
        if nodo_actual is not None and nodo_actual.next is not None:
            nodo_actual.next = nodo_actual.next.next

    def mostrar_tareas(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de vencimiento: {nodo_actual.fecha_vencimiento}")
            nodo_actual = nodo_actual.next

    def buscar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.descripcion == descripcion:
                return f"Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de vencimiento: {nodo_actual.fecha_vencimiento}"
            nodo_actual = nodo_actual.next
        return "Tarea no encontrada"

    def marcar_tarea_completada(self, descripcion):
        self.eliminar_tarea_por_descripcion(descripcion)
        
lista_tareas = ListaTareas()
print("Agregamos tareas")
lista_tareas.agregar_tarea("Estudiar para examen", 1, "2024-09-25")
lista_tareas.agregar_tarea("Comprar víveres", 3, "2024-09-30")
lista_tareas.agregar_tarea("Hacer ejercicio", 2, "2024-09-23")

print("Mostramos todas las tareas")
lista_tareas.mostrar_tareas()

print("Buscamos tarea por descripción")
resultado_busqueda = lista_tareas.buscar_tarea("Hacer ejercicio")
print(resultado_busqueda)

print("Marcamos tarea como completada")
lista_tareas.marcar_tarea_completada("Hacer ejercicio")

print("Mostramos todas las tareas tras completar una")
lista_tareas.mostrar_tareas()
