class Nodo:
    def __init__(self, id):
        self.id = id
        self.vecinos = []

# Crear los nodos
nodos = [Nodo(i) for i in range(10)]

# Establecer los vecinos para cada nodo
nodos[1].vecinos = [nodos[6], nodos[8]]
nodos[2].vecinos = [nodos[7], nodos[9]]
nodos[3].vecinos = [nodos[4], nodos[8]]
nodos[4].vecinos = [nodos[3], nodos[9], nodos[0]]
nodos[5].vecinos = []
nodos[6].vecinos = [nodos[1], nodos[7], nodos[0]]
nodos[7].vecinos = [nodos[2], nodos[6]]
nodos[8].vecinos = [nodos[1], nodos[3]]
nodos[9].vecinos = [nodos[2], nodos[4]]
nodos[0].vecinos = [nodos[4], nodos[6]]

def total_teletransportes(movimientos):
    # Crear una matriz de tamaño [movimientos + 1][10] para almacenar los resultados de los subproblemas
    dp = [[0 for _ in range(10)] for _ in range(movimientos + 1)]
    
    # Inicializar la matriz para el caso base cuando movimientos == 1
    for i in range(10):
        dp[1][i] = len(nodos[i].vecinos)

    # Rellenar la matriz para los demás casos
    for m in range(2, movimientos + 1):
        for i in range(10):
            for vecino in nodos[i].vecinos:
                dp[m][i] += dp[m - 1][vecino.id]

    # Sumar todos los teletransportes posibles para la cantidad de movimientos
    total = sum(dp[movimientos])

    return total

# Probar la función
print(total_teletransportes(1))  # 20
print(total_teletransportes(2))  # 46
print(total_teletransportes(3))  # 104
print(total_teletransportes(5))  # 240
print(total_teletransportes(8))  
print(total_teletransportes(10))  
print(total_teletransportes(15))  
print(total_teletransportes(18))  
print(total_teletransportes(21))  
print(total_teletransportes(23))  
print(total_teletransportes(32))  
