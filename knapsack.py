class Mochila:
    # Algoritmo de la mochila
    def knapsack(peso, objeto, capacidad):
        # aumenta una fila y una columna
        temp = [[0 for x in range(capacidad+1)] for x in range(len(peso)+1)]
        
        for i in range(1, len(peso)+1):
            for j in range(1, capacidad+1):
                if objeto[i-1] <= j:
                    temp[i][j] = max(temp[i-1][j], temp[i-1][j-objeto[i-1]] + peso[i-1])
                else:
                    temp[i][j] = temp[i-1][j]
        return temp[len(peso)][capacidad]


objeto = [3, 5, 6]
peso = [6, 7, 8]
capacidad = 6

valor = Mochila.knapsack(peso, objeto, capacidad)

print("El valor optimo para una mochila de {} es: {}".format(capacidad, valor))
