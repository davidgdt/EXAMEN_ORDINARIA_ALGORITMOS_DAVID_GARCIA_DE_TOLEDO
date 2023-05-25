# Representación de las rutas y los posibles teletransportes
rutas = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6],
}

# Función para contar los teletransportes válidos
def contar_teletransportes(nodo, movimientos):
    # Caso base: si no hay más movimientos, hemos encontrado un teletransporte válido
    if movimientos == 0:
        return 1

    # Caso recursivo: explorar cada posible teletransporte
    total = 0
    for vecino in rutas[nodo]:
        total += contar_teletransportes(vecino, movimientos - 1)

    return total

# Función para calcular el total de teletransportes válidos para una cantidad de movimientos
def total_teletransportes(movimientos):
    total = 0
    for nodo in rutas:
        total += contar_teletransportes(nodo, movimientos - 1)  # restamos 1 porque el primer movimiento no cuenta
    return total

# Probar la función
print(total_teletransportes(1))  # 20
print(total_teletransportes(2))  # 46
print(total_teletransportes(3))  # 104
print(total_teletransportes(5)) #
print( total_teletransportes(8))   
print( total_teletransportes(10))
print(total_teletransportes(15))
print(total_teletransportes(18))
print(total_teletransportes(21))
print(total_teletransportes(23))
print(total_teletransportes(32))