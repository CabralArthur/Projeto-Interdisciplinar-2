"""
    FlyFood - Algoritmo de Força Bruta
    Aluno: Pedro Arthur Carlos Cabral Da Silva
    Bacharelado Em Sistemas De Informação - UFRPE
"""

from itertools import permutations

# Buscar quais serão os pontos presentes na matriz

def getMatrixPoints(matrix) -> list:
    """
        Retorna os pontos presentes na matriz

        Argumentos:
        matrix (list) -> Entrada do problema

        Returns:
            list: Lista com todos os pontos à serem analisados no problema
    """

    matrixPoints = []
    # Para cada linha na matriz
    for line in matrix:
        # Acessar cada string presente na linha
        for string in line:
            # Verificar se o espaço atual é diferente de vazio ou se é diferente da letra 'R'
            if string != '0' and string != 'R':
                matrixPoints.append(string)
    return matrixPoints


def getPointPosition(matrix, point: str) -> tuple:
    """Retorna a posição do ponto dentro da matriz.

    Arguments:
        matrix (list[list[str]]): Matriz inteira
        point (str): Ponto na qual será procurado dentro da matrix

    Returns:
        tuple: Posição (x, y) do ponto dentro da Matrix

    """
    for coordinateX, row in enumerate(matrix):
        for coordinateY, element in enumerate(row):
            if element == point:
                return coordinateX, coordinateY


def getDistance(pA: tuple, pB: tuple) -> int:
    """Retorna a distancia entre 2 pontos.

    Arguments:
        pA (tuple): Posição (x, y) do ponto pA
        pA (tuple): Posição (x, y) do ponto pB

    Returns:
        int: Distancia entre os pontos pA e pB, disconsiderando diagonais

    """
    distX = pB[0] - pA[0] if pB[0] > pA[0] else pA[0] - pB[0]
    distY = pB[1] - pA[1] if pB[1] > pA[1] else pA[1] - pB[1]
    return abs(distX + distY)


def joinList(values: list) -> list:
    joinedList = []
    for i in values:
        if isinstance(i, list):
            joinedList += joinList(i)
        else:
            joinedList.append(i)
    return joinedList


def getCompleteDistance(points):
    """Returna a distancia entre todos os pontos recebidos.

    Arguments:
        points (list): Lista de pontos em uma matrix

    Returns:
        int: Distancia total dos pontos

    """
    sumOfDistance = 0
    # Percorrendo todos os pontos
    for pos, current in enumerate(points):
        # Teste para verificar se existe outro ponto pra testar
        try:
            nextPoint = points[pos+1]
        # Caso não exista, passar
        except IndexError:
            pass
        # Caso exista, obter a distancia entre esses pontos e somar ao total
        else:
            sumOfDistance += getDistance(current, nextPoint)
    return sumOfDistance

#Função para obter a chave do valor mínimo
def getDictKey(dicionario, valor):
    for key, value in dicionario.items():
        if valor == value:
            return key


def flyFood(matrix: list[list[str]], matrixPoints: list[str]) -> str:
    """Retorna uma lista com os menores caminhos possiveis.

    Arguments:
        matrix (list[list[str]]: Uma coleção de listas
        matrixPoints (list[str]): Lista contendo os pontos presentes no caso teste

    Returns:
        list: Tupla com os todos os caminhos mais rápidos, passando pelos pontos identificados no caso teste

    """

    points = {}
    for point in matrixPoints:
        points[point] = getPointPosition(matrix, point)

    R = getPointPosition(matrix, 'R')

    # Criando um dicionário com todos os caminhos possiveis
    solutions = {}

    # Para cada combinação dentre as permutações
    for combination in list(permutations(matrixPoints)):

        temporaryList = []

        #Percorre toda a combinação
        for item in combination:
            #E adiciona à lista temporária toda a rota entre esses pontos
            temporaryList.append(points[item])

        #Rota atual, que vai do ponto R, percorrendo todas as coordenadas e voltando ao ponto R
        currentRouteList = [R, temporaryList[:], R]

        solutions[" ".join(combination)] = getCompleteDistance(joinList(currentRouteList))

        temporaryList.clear()
    return print(getDictKey(solutions, min(solutions.values())))


elementsArray = []

# Array que irá conter as linhas com as posições dos pontos
matrix = []

# Abertura do arquivo
file = open('I - FlyFood/1 - Algoritmo De Força Bruta/test.txt', 'r')

# Inserindo todos os elementos no elementsArray
for line in file:
    elements = line.split()
    elementsArray.append(elements)
file.close()

"""
    rows, columns = [int(x) for x in elementsArray[0]]
"""

matrix = elementsArray[1:]

#Obtendo todos os pontos à serem analisados
matrixPoints = getMatrixPoints(matrix)

#Chamando 
flyFood(matrix, matrixPoints)