import random
import numpy as np

def tab_int(nom_fichier):
    fichier = open(nom_fichier, "r")
    a=fichier.readline()
    nb_of_int=int(a)
    contenu = fichier.readlines()
    fichier.close()
    tab=contenu[0].split(", ")
    for i in range(len(tab)):
        tab[i]=int(tab[i])
    return (nb_of_int,tab)

(nb, tabdata)=tab_int("small.txt")

def tab_initialization():
    t=[0 for i in range(nb)]
    n=random.randint(1,nb)
    tabde1=random.sample([i for i in range(nb)],n)
    for i in tabde1:
        t[i]=1
    return t

def create_list(individual):
    liste=[]
    for i in range(len(individual.gen_code)):
        if individual.gen_code[i] == 1:
            liste.append(tabdata[i])
    return liste

class Individual:
    def __init__(self):
        self.gen_code=tab_initialization()
        self.list=create_list(self)
        self.fitness=-1
        self.length=sum(self.gen_code)
        self.result=sum(self.list)

    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people):
        self.ListOfIndividuals = [Individual() for _ in range(nb_of_people)]

def fitness(population, bestSol):
    for individual in population.ListOfIndividuals:
        individual.fitness=individual.length/(1+individual.result**2)
        if (individual.length > bestSol.length) and (individual.result == 0):
            bestSol = individual
    return (population, bestSol)


def selection(population):
    population.ListOfIndividuals = sorted(population.ListOfIndividuals, key=lambda individual: individual.fitness, reverse=True)
    population.ListOfIndividuals = population.ListOfIndividuals[:int(0.2 * len(population.ListOfIndividuals))]
    return population

def crossover(population):
    offsprings=[]
    for i in range(40):
        split = random.randint(1, nb - 1)
        A=random.sample(population.ListOfIndividuals, 2)
        a=A[0]
        b=A[1]
        child1 = Individual()
        child2 = Individual()
        child1.gen_code = a.gen_code[:split] + b.gen_code[split:]
        child2.gen_code = b.gen_code[:split] + a.gen_code[split:]
        offsprings.append(child1)
        offsprings.append(child2)
    population.ListOfIndividuals = population.ListOfIndividuals + offsprings
    return population


def mutation(population):
    for individual in population.ListOfIndividuals:
        for i in range(nb):
            if random.uniform(0.0,1.0)<=1/sum(individual.gen_code):
                individual.gen_code[i]=(individual.gen_code[i] + 1)%2
        individual.list=create_list(individual)
        individual.length=sum(individual.gen_code)
        individual.result=sum(individual.list)
    return population

generations = 1000
population_size = 100
#C'est mon test
def ga():
    population=Population(population_size)
    bestSol=population.ListOfIndividuals[0]
    firstSol=bestSol
    for generation in range(generations):
        print('Generation  ' + str(generation))
        (population, bestSol) = fitness(population, bestSol)
        population = selection(population)
        population = crossover(population)
        population = mutation(population)
    print(firstSol.gen_code)
    print(firstSol.length)
    print(bestSol.gen_code)
    print(bestSol.length)
    print(bestSol.list)
    print(bestSol.result)
ga()

