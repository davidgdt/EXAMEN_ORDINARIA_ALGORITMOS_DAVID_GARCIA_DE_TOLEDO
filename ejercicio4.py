class Pokeball:
    def _init_(self, nombre, peso, precio, fecha_fabricacion):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print(f'La Pokeball {self.nombre} se ha creado con éxito.')

    def _str_(self):
        return f"Pokeball: {self.nombre}, Peso: {self.peso}g, Precio: {self.precio}$, Fecha de fabricación: {self.fecha_fabricacion}"


class NodoArbol:
    def _init_(self, pokeball):
        self.pokeball = pokeball
        self.izq = None
        self.der = None

    def insertar(self, pokeball):
        if pokeball.nombre < self.pokeball.nombre:
            if self.izq is None:
                self.izq = NodoArbol(pokeball)
            else:
                return self.izq.insertar(pokeball)
        else:
            if self.der is None:
                self.der = NodoArbol(pokeball)
            else:
                return self.der.insertar(pokeball)

    def buscar(self, nombre):
        if nombre < self.pokeball.nombre:
            if self.izq is None:
                return None
            else:
                return self.izq.buscar(nombre)
        elif nombre > self.pokeball.nombre:
            if self.der is None:
                return None
            else:
                return self.der.buscar(nombre)
        else:
            return self.pokeball


import unittest

class TestEjercicios(unittest.TestCase):

    def setUp(self):
        self.pokeballs = [
            Pokeball('pokeball1', 50, 200, '2023-01-01'),
            Pokeball('pokeball2', 50, 300, '2023-02-01'),
            Pokeball('pokeball3', 50, 400, '2023-03-01'),
            Pokeball('pokeball4', 50, 500, '2023-04-01'),
        ]

        # Ordenando las Pokeballs por fecha de fabricación
        self.pokeballs.sort(key=lambda x: x.fecha_fabricacion)

    def test_pokeball_data(self):
        # Mostrando datos de todas las Pokeballs
        for pokeball in self.pokeballs:
            print(pokeball)
            
        # Modificando el precio de la primera Pokeball
        self.pokeballs[0].precio = 1000
        print("\nDespués de modificar el precio:")
        for pokeball in self.pokeballs:
            print(pokeball)

if __name__ == "__main__":
    unittest.main()