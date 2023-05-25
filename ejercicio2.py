class Pokemon:
    def __init__(self, nombre, tipo, ps, ataque, defensa, ataque_especial, defensa_especial, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.ps = ps
        self.ataque = ataque
        self.defensa = defensa
        self.ataque_especial = ataque_especial
        self.defensa_especial = defensa_especial
        self.velocidad = velocidad
        self.evoluciones = []  
        print(f'El Pokemon {self.nombre} se ha creado con éxito.')

    def agregar_evolucion(self, pokemon):
        return self.evoluciones.append(pokemon)
        
    def clasificacion(self):
        return f'Pokemon: {self.nombre}, Tipo: {self.tipo}, PS: {self.ps}, Ataque: {self.ataque}, Defensa: {self.defensa}, Ataque Especial: {self.ataque_especial}, Defensa Especial: {self.defensa_especial}, Velocidad: {self.velocidad}'

class NodoArbol:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izq = None
        self.der = None

    def insertar(self, pokemon):
        if pokemon.nombre < self.pokemon.nombre:
            if self.izq is None:
                self.izq = NodoArbol(pokemon)
            else:
                return self.izq.insertar(pokemon)
        else:
            if self.der is None:
                self.der = NodoArbol(pokemon)
            else:
                return self.der.insertar(pokemon)

    def buscar(self, nombre):
        if nombre < self.pokemon.nombre:
            if self.izq is None:
                return None
            else:
                return self.izq.buscar(nombre)
        elif nombre > self.pokemon.nombre:
            if self.der is None:
                return None
            else:
                return self.der.buscar(nombre)
        else:
            return self.pokemon

#EXPERIMENTACION

import unittest
import random

class TestEjercicios(unittest.TestCase):

    def setUp(self):
        self.pokemons = [
            Pokemon("Pikachu", "Eléctrico", 35, 55, 40, 50, 50, 90),
            Pokemon("Charizard", "Fuego/Volador", 78, 84, 78, 109, 85, 100),
            Pokemon("Blastoise", "Agua", 79, 83, 100, 85, 105, 78),
            Pokemon("Venusaur", "Planta/Veneno", 80, 82, 83, 100, 100, 80),
            Pokemon("Mewtwo", "Psíquico", 106, 110, 90, 154, 90, 130),
            Pokemon("Gengar", "Fantasma/Veneno", 60, 65, 60, 130, 75, 110),
            Pokemon("Alakazam", "Psíquico", 55, 50, 45, 135, 95, 120),
            Pokemon("Machamp", "Lucha", 90, 130, 80, 65, 85, 55),
            Pokemon("Gyarados", "Agua/Volador", 95, 125, 79, 60, 100, 81),
            Pokemon("Arcanine", "Fuego", 90, 110, 80, 100, 80, 95),
        ]

    def test_clasificacion(self):
        for pokemon in self.pokemons:
            print(pokemon.clasificacion())

if __name__ == "__main__":
    unittest.main()

# a. Generar 50 Pokemons
tipos = ['Fuego', 'Agua', 'Planta', 'Eléctrico', 'Hielo', 'Lucha', 'Veneno', 'Tierra', 'Volador', 'Psíquico', 'Bicho', 'Roca', 'Fantasma', 'Dragón', 'Siniestro', 'Acero', 'Hada']
nombres = ['Pokemon' + str(i) for i in range(1, 51)]
pokemons = []
for i in range(50):
    nombre = nombres[i]
    tipo = random.choice(tipos)
    ps = random.randint(50, 100)
    ataque = random.randint(50, 150)
    defensa = random.randint(50, 150)
    ataque_especial = random.randint(50, 150)
    defensa_especial = random.randint(50, 150)
    velocidad = random.randint(50, 150)
    pokemon = Pokemon(nombre, tipo, ps, ataque, defensa, ataque_especial, defensa_especial, velocidad)
    pokemons.append(pokemon)

# Cargar Pokemons en dos tablas hash
tabla_hash_tipo = {}
tabla_hash_nombre = {}
for pokemon in pokemons:
    # Tabla hash por tipo
    tipo = pokemon.tipo
    if tipo not in tabla_hash_tipo:
        tabla_hash_tipo[tipo] = []
    tabla_hash_tipo[tipo].append(pokemon)

    # Tabla hash por nombre
    nombre = pokemon.nombre
    if nombre not in tabla_hash_nombre:
        tabla_hash_nombre[nombre] = []
    tabla_hash_nombre[nombre].append(pokemon)

# c. Determinar si el Pokemon 'Pikachu' está en la lista
nombre_buscar = 'Pikachu'
encontrado = any(pokemon.nombre == nombre_buscar for pokemon in pokemons)
print(f'El pokemon {nombre_buscar} {"está" if encontrado else "no está"} en la lista.')

# d. Obtener pokemons de tipo 'Fuego' y 'Agua'
equipo_fuego = tabla_hash_tipo.get('Fuego', [])
equipo_agua = tabla_hash_tipo.get('Agua', [])

print('Pokemons de tipo Fuego:', ', '.join(map(str, equipo_fuego)))
print('Pokemons de tipo Agua:', ', '.join(map(str, equipo_agua)))

# e. Obtener pokemons con nombre 'Pokemon1' y 'Pokemon2'
pokemon1 = tabla_hash_nombre.get('Pokemon1', [])
pokemon2 = tabla_hash_nombre.get('Pokemon2', [])

print('Pokemon con nombre Pokemon1:', ', '.join(map(str, pokemon1)))
print('Pokemon con nombre Pokemon2:', ', '.join(map(str, pokemon2)))
