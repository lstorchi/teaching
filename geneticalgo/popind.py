import random
import sys 

# @author Loriano Storchi based on Vijini's Java code

# Individual class
class Individual:

    def __init__(self, size = 5):
        self._fitness = 0
        self._genes = []
        self._geneLength = size

        #Set genes randomly for each individual
        for i in range(self._geneLength):
            val = random.random()

            if val < 0.5:
                self._genes.append(0)
            else:
                self._genes.append(1)

        #print self._genes

        self._fitness = 0

    def get_geneLength(self): 
        return self._geneLength

    def get_fitness(self):
        return self._fitness

    def get_genes(self):
        return self._genes

    # Calculate fitness
    def calcFitness(self):

        self._fitness = 0
        for i in range(self._geneLength):
            if (self._genes[i] == 1):
                    self._fitness = self._fitness + 1

# Population class
class Population:
    
    def __init__(self):
        self._popSize = 0
        self._individuals = []
        self._fittest = 0

    def toStdout(self):
        for i in range(self._popSize):
            print self._individuals[i].get_genes()

    def get_fittestval (self):
        return self._fittest

    def get_individuals(self):
        return self._individuals

    # Initialize population
    def initializePopulation(self, size): 
        self._popSize = size

        for i in range(self._popSize):
            individuo = Individual()
            individuo.calcFitness()

            self._individuals.append(individuo)

    # Get the fittest individual
    def getFittest(self):
        
        maxFit = - sys.maxint - 1
        maxFitIndex = 0
        for i in range(self._popSize):
            if (maxFit <= self._individuals[i].get_fitness()):
                maxFit = self._individuals[i].get_fitness()
                maxFitIndex = i

        self._fittest = maxFit
        return self._individuals[maxFitIndex]

    # Get the second most fittest individual
    def getSecondFittest(self):

        maxFit1 = 0
        maxFit2 = 0
        for i in range(len(self._individuals)):
            if (self._individuals[i].get_fitness() > 
                self._individuals[maxFit1].get_fitness()):
                maxFit2 = maxFit1
                maxFit1 = i
            elif (self._individuals[i].get_fitness() >
                  self._individuals[maxFit2].get_fitness()):
                maxFit2 = i
        
        return self._individuals[maxFit2]

    #Get index of least fittest individual
    def getLeastFittestIndex(self):
        minFitVal = sys.maxint
        minFitIndex = 0;
        
        for i in range(len(self._individuals)):
            if (minFitVal >= self._individuals[i].get_fitness()):
                minFitVal = self._individuals[i].get_fitness()
                minFitIndex = i

        return minFitIndex

    #Calculate fitness of each individual
    def calculateFitness(self):

        for i in range(len(self._individuals)):
            self._individuals[i].calcFitness()
