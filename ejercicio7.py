import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return self.nombre

# a. Generar 800 Pokemons
tipos = ['Agua', 'Fuego', 'Tierra', 'Eléctrico', 'Normal', 'Fantasma']
pokemons = []
for i in range(800):
    tipo = random.choice(tipos)
    nivel = str(random.randint(100, 900)) + str(random.choice(['78', '37'])) # Aseguramos que el nivel termine en '78' o '37'
    nombre = tipo + '-' + nivel
    pokemon = Pokemon(nombre, tipo, nivel)
    pokemons.append(pokemon)

# b. Cargar Pokemons en dos tablas hash
tabla_hash_nivel = {}
tabla_hash_tipo = {}
for pokemon in pokemons:
    # Tabla hash por nivel (últimos dos dígitos)
    nivel = pokemon.nivel[-2:] # Usamos los últimos dos dígitos del nivel
    if nivel not in tabla_hash_nivel:
        tabla_hash_nivel[nivel] = []
    tabla_hash_nivel[nivel].append(pokemon)

    # Tabla hash por tipo
    tipo = pokemon.tipo
    if tipo not in tabla_hash_tipo:
        tabla_hash_tipo[tipo] = []
    tabla_hash_tipo[tipo].append(pokemon)

# c. Determinar si el Pokemon Fantasma de nivel 187 está cargado
nombre_buscar = 'Fantasma-187'
encontrado = any(pokemon.nombre == nombre_buscar for pokemon in pokemons)
print(f'El Pokemon {nombre_buscar} {"está" if encontrado else "no está"} cargado.')

# d. Obtener Pokemons terminados en 78 y 37
mision_asalto = tabla_hash_nivel.get('78', [])
mision_exploracion = tabla_hash_nivel.get('37', [])

print('Pokemons para la misión de asalto:', ', '.join(map(str, mision_asalto)))
print('Pokemons para la misión de exploración:', ', '.join(map(str, mision_exploracion)))


# e. Obtener Pokemons de tipo 'Tierra' y 'Fuego'
custodia_profesor_oak = tabla_hash_tipo.get('Tierra', [])
mision_exterminacion = tabla_hash_tipo.get('Fuego', [])

print('Pokemons para la mision exploracion:', ', '.join(map(str, custodia_profesor_oak)))
print('Pokemons para la misión de exterminación:', ', '.join(map(str, mision_exterminacion)))