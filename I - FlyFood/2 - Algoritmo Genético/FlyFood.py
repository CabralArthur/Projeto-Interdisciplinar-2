"""
    FlyFood - Algoritmo Genético
    Aluno: Pedro Arthur Carlos Cabral Da Silva
    Bacharelado Em Sistemas De Informação - UFRPE
"""

import random, operator as op

"""
    Classe DeliveryPoint, que será utilizada
    para criar e admnistrar os pontos de entrega
"""

class DeliveryPoint:
    # Essa classe conterá as coordenadas x e y
    def __init__(self, pointName, x, y):
        self.pointName = pointName
        self.coordinateX = x
        self.coordinateY = y

    def getDistance(self, deliveryPoint):
        """
            Função que irá retornar a distância entre os 2 pontos de entrega

            deliveryPoint = Ponto à ser utilizado para comparação
            Return = Distância entre os 2 pontos
        """

        xDistance = deliveryPoint.coordinateX - self.coordinateX if deliveryPoint.coordinateX > self.coordinateX else self.coordinateX - deliveryPoint.coordinateX
        yDistance = deliveryPoint.coordinateY - self.coordinateY if deliveryPoint.coordinateY > self.coordinateY else self.coordinateY - deliveryPoint.coordinateY
        return abs(xDistance + yDistance)

    def __repr__(self):
        return f'({str(self.pointName)})'

"""
    Classe FitnessRoute, que dá o retorno do fitness
    de uma rota previamente escolhida.
"""

class FitnessRoute:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0

    def getRouteDistance(self):
        """
            Função getRouteDistance, que percorre toda uma rota
            validando e calculando sua trajetória e somando-a a uma variável
            de tamanho (routeDistance), por fim, retornando-a.
        """
        if self.distance == 0:
            routeSize = 0

            for i in range(0, len(self.route)):

                deliveryPoint = self.route[i]
                nextDeliveryPoint = None

                if i + 1 < len(self.route):
                    nextDeliveryPoint = self.route[i + 1]

                else:
                    nextDeliveryPoint = self.route[0]

                routeSize += deliveryPoint.getDistance(nextDeliveryPoint)

            self.distance = routeSize

        return self.distance

    def getFitnessRoute(self):
        """
            Função getFitnessRoute, que irá calcular o fitnes de modo inverso.
            nesse caso, quanto menor for o tamanho da rota, maior será o fitness,
            e vice-versa.
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.getRouteDistance())

        return self.fitness

def routerRank(deliveryRoutes):
    """
        Função routerRank, que irá percorrer todas as rotas de delivery e irá
        retornar uma lsita contento o id de cada uma das rotas, bem como o valor
        do fitness obtido para cada uma delas.
    """

    fitnessResults = {}

    for i in range(0, len(deliveryRoutes)):

        fitnessResults[i] = FitnessRoute(deliveryRoutes[i]).getFitnessRoute()

    routedRank = sorted(fitnessResults.items(), key = op.itemgetter(1), reverse = True)

    return routedRank

def tournamentSelection(deliveryPoints, elitismSize):
    """
        Função tournamentSelection, que retorna os indexes dos pontos
        mais bem qualificados na seleção.
    """
    winnnerIndexesResult = []
    
    firstPoint = deliveryPoints[random.randint(0, len(deliveryPoints) - 1)]

    secondPoint = deliveryPoints[random.randint(0, len(deliveryPoints) - 1)]

    for i in range(0, elitismSize):
        winnnerIndexesResult.append(deliveryPoints[i][0])
        
    for i in range(0, len(deliveryPoints) - elitismSize):

        firstPoint = deliveryPoints[random.randint(0, len(deliveryPoints) - 1)][0]

        secondPoint = deliveryPoints[random.randint(0, len(deliveryPoints) - 1)][0]

        while secondPoint == firstPoint:
            secondPoint = deliveryPoints[random.randint(0, len(deliveryPoints) - 1)][0]

        if firstPoint >= secondPoint:
            winnnerIndexesResult.append(firstPoint)
        
        else:
            winnnerIndexesResult.append(secondPoint)

    return winnnerIndexesResult

def getSelectedRoutes(deliveryPoints, tournamentWinners):
    """
        Função getMatingPool, que retorna
        os indivíduos selecionados da população.
    """
    selectedBetterPoints = []

    for i in range(0, len(tournamentWinners)):
        index = tournamentWinners[i]
        selectedBetterPoints.append(deliveryPoints[index])

    return selectedBetterPoints

def crossOverOfParents(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2

    return child

def getSelectedRoutes(routes, selectedIndexes):
    """
        Função getSelectesRoutes, que irá retornar as rotas
        dos indexes mais bem qualificados na seleção por torneio.
    """
    selectedRoutes = []
    
    for i in range(0, len(selectedIndexes)):
        index = selectedIndexes[i]
        selectedRoutes.append(routes[index])
    
    return selectedRoutes

def crossOverOfRoutes(matingPool, elitismSize):
    children = []
    crossOverLength = len(matingPool) - elitismSize
    drawnRoutes = random.sample(matingPool, len(matingPool))

    for i in range(0, elitismSize):
        children.append(matingPool[i])

    for i in range(0, crossOverLength):
        child = crossOverOfParents(drawnRoutes[i], drawnRoutes[len(matingPool) - i - 1])
        children.append(child)

    return children


def mutateRoute(deliveryRoute, mutationRate):
    """
        Função mutateRoute, que tem por objetivo
        variar a introdução de novas rotas,
        trocando a posição aleatoriamente
    """
    for changedPosition in range(len(deliveryRoute)):

        if(random.random() < mutationRate):
            currentPosition = int(random.random() * len(deliveryRoute))

            changedDeliveryPoint = deliveryRoute[changedPosition]
            currentDeliveryPoint = deliveryRoute[currentPosition]

            deliveryRoute[changedPosition] = currentDeliveryPoint
            deliveryRoute[currentPosition] = changedDeliveryPoint

    return deliveryRoute

def mutateRoutes(deliveryRoutes, mutationRate):
    """
        Função mutateRoutes, que, junto à função mutateRoute,
        irá retornar as rotas que sofreram mutações,
        confirmando a variação.
    """
    mutatedRoutes = []

    for i in range(0, len(deliveryRoutes)):

        mutatedRoute = mutateRoute(deliveryRoutes[i], mutationRate)

        mutatedRoutes.append(mutatedRoute)

    return mutatedRoutes

def getInitialPopulation(quantityOfRoutes, deliveryPoints):
    """
        Função getInitialPopulation, que será utilizada na parte
        inicial do algoritmo, com o objetivo de gerar a população
        inicial e retorná-la.
    """
    initialRoutes = []

    for _ in range(0, quantityOfRoutes):
        initialRoutes.append(getRandomRoute(deliveryPoints))

    """
        Essa função só será utilzada uma vez, tendo em vista
        que as demais gerações serão feitas utilizando conceitos
        de crossOver e mutação para garantir a variação.
    """
    return initialRoutes

def getRandomRoute(deliveryPoints):
    """
        Função getRandomRoute, que retorna uma rota aleatória
        dentre todos os pontos de entrega.
    """
    route = random.sample(deliveryPoints, len(deliveryPoints))

    return route


def getNextPopulations(currentRoutes, elitismSize, mutationRate):
    """
        Função getNextPopulations, que irá fazer
        o rankeamento das rotas, selecionando e
        ordenando as mais bem aplicadas, fazer a
        seleção por torneio, posteriormente fazer o crossOver
        para retornar uma próxima população de rotas variadas.
    """

    rankedRoutes = routerRank(currentRoutes)

    winnerIndexes = tournamentSelection(rankedRoutes, elitismSize)

    selectedRoutes = getSelectedRoutes(currentRoutes, winnerIndexes)

    children = crossOverOfRoutes(selectedRoutes, elitismSize)

    nextPopulation = mutateRoutes(children, mutationRate)

    return nextPopulation

def geneticAlgorithm(population, popSize, elitismSize, mutationRate, generations):
    #Fazendo a geração da população incial
    currentDeliveryPoints = getInitialPopulation(popSize, population)

    for _ in range(0, generations + 1):
        #Geração das próximas gerações
        currentDeliveryPoints = getNextPopulations(currentDeliveryPoints, elitismSize, mutationRate)

    bestRouteIndex = routerRank(currentDeliveryPoints)[0][0]

    bestRoute = currentDeliveryPoints[bestRouteIndex]

    return print(bestRoute)

def getMatrixPointsAndPositions():
    """
        Retorna os pontos e as posições desses presentes na matriz

        Arguments:
            file -> Entrada do problema

        Returns:
            list: Lista com todos os pontos à serem analisados no problema
    """

    # Escolhendo arquivo de leitura de entrada #
    file = open('I - FlyFood/2 - Algoritmo Genético/16_delivery_points.txt', 'r')

    matrixElements = []

    line = file.readline()

    # Inserindo todos os elementos na matriz
    for line in file:
        elements = line.split()
        matrixElements.append(elements)

    file.close()

    #Dicionário matrixPoints que irá conter os pontos e suas respectivas posições
    matrixPoints = {}

    #Percorrendo toda a matriz e inserindo os pontos e posições de cada
    for i in range(len(matrixElements)):
        for j in range(len(matrixElements[0])):
            point = matrixElements[i][j]
            if matrixElements[i][j] == 'R':
                matrixPoints[point] = [i, j]
            elif matrixElements[i][j] != '0':
                matrixPoints[point] = [i, j]

    deliveryPoints = []

    """
        Inserindo todos os pontos utilizando a classe DeliveryPoints
        e retornando todos os pontos (classes) com nome e posição, bem como os nomes.
    """
    for pointName, coordinates in matrixPoints.items():
        deliveryPoints.append(DeliveryPoint(pointName, coordinates[0], coordinates[1]))

    return deliveryPoints

#Todos os pontos presentes no plano com seus respectivos nomes e posições
deliveryPoints = getMatrixPointsAndPositions()

#Chamada da função principal geneticAlgorithm
geneticAlgorithm(deliveryPoints, 30, 20, 0.01, 250)