import random
import popind
import sys

# @author Loriano Storchi based on Vijini's java code

###############################################################################

#Selection
def selection(population):

    #Select the most fittest individual
    fittest = population.getFittest()

    #Select the second most fittest individual
    secondFittest = population.getSecondFittest()

    return fittest, secondFittest

###############################################################################

#Crossover
def crossover(population, fittest, secondFittest):

    #Select a random crossover point
    crossOverPoint = random.randint(1, 
            population.get_individuals()[0].get_geneLength()-2)

    #Swap values among parents
    for i in range(crossOverPoint):
        temp = fittest.get_genes()[i];
        fittest.get_genes()[i] = secondFittest.get_genes()[i]
        secondFittest.get_genes()[i] = temp

###############################################################################

#Mutation
def mutation(population, fittest, secondFittest):
    #Select a random mutation point
    mutationPoint = random.randint(0, 
            population.get_individuals()[0].get_geneLength()-1)
    
    #Flip values at the mutation point
    if (fittest.get_genes()[mutationPoint] == 0):
        fittest.get_genes()[mutationPoint] = 1
    else:
        fittest.get_genes()[mutationPoint] = 0

    mutationPoint = random.randint(0, 
            population.get_individuals()[0].get_geneLength()-1)

    if (secondFittest.get_genes()[mutationPoint] == 0):
        secondFittest.get_genes()[mutationPoint] = 1
    else:
        secondFittest.get_genes()[mutationPoint] = 0

###############################################################################

#Get fittest offspring
def getFittestOffspring(fittest, secondFittest):

    if (fittest.get_fitness() > secondFittest.get_fitness()):
        return fittest
    
    return secondFittest

###############################################################################

#Replace least fittest individual from most fittest offspring
def addFittestOffspring(population, fittest, secondFittest):

    #Update fitness values of offspring
    fittest.calcFitness()
    secondFittest.calcFitness()

    #Get index of least fit individual
    leastFittestIndex = population.getLeastFittestIndex()

    #Replace least fittest individual from most fittest offspring
    population.get_individuals()[leastFittestIndex] = \
        getFittestOffspring(fittest, secondFittest)

###############################################################################

random.seed(10)

generationCount = 1
population = popind.Population()
population.initializePopulation(10)

#Calculate fitness of each individual
population.calculateFitness();
population.getFittest()

sys.stdout.write("Generation: " + str(generationCount) \
        + " Fittest: " + str(population.get_fittestval()) + "\n")
population.toStdout()

while (population.get_fittestval() < 5):
    generationCount = generationCount + 1
    selection(population)
    fittest = population.getFittest()
    secondFittest = population.getSecondFittest()
    crossover(population, fittest, secondFittest)

    if random.random() > 0.5:
        mutation(population, fittest, secondFittest)

    addFittestOffspring (population, fittest, secondFittest)

    population.calculateFitness()

    sys.stdout.write("Generation: " + str(generationCount) \
        + " Fittest: " + str(population.get_fittestval()) + "\n")
    #population.toStdout()


sys.stdout.write("\nSolution found in generation " + str(generationCount) + "\n")
sys.stdout.write("Fitness: " + str(population.getFittest().get_fitness()) + "\n")
sys.stdout.write("Genes: \n")
sys.stdout.write(str(population.getFittest().get_genes()) + "\n")

