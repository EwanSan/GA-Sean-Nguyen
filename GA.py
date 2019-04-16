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

def tab_initialization(nb_of_int):
    t=[0 for i in range(nb_of_int)]
    n=random.randint(1,nb_of_int)
    tabde1=random.sample([i for i in range(nb_of_int)],n)
    for i in tabde1:
        t[i]=1
    return t


class Individual:
    def __init__(self, nb_of_int):
        self.gen_code=tab_initialization(nb_of_int)
        self.fitness=-1
        self.length=sum(self.gen_code)

    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people, nb_of_int):
        self.ListOfIndividuals = [Individual(nb_of_int) for _ in range(nb_of_people)]

def fitness(gen_code):


#C'est mon test
def ga():
    population = Population(100, nb)
    for individual in population.ListOfIndividuals:
        print(individual.gen_code)
        print("\n")
ga()
