import random

class Individual:
    def __init__(self,nbinit):
        self.gen_code=[random.randrange(-100, 100) for i in range(nbinit)]
        self.fitness=-1
        self.length=len(self.gen_code)

    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people):
        self.ListOfIndividuals = [Individual(10) for _ in range(nb_of_people)]
        
#C'est mon test
def ga():
    population = Population(100)
    for individual in population.ListOfIndividuals:
        print(individual.gen_code)
        print("\n")
        
#trier le code genetic

def fitness(List): #écart à 0
    for individual in   List:
        individual.fitness=sum(individual.gen_code)
        

def select_individuals(list):
    list = sorted(list, key=lambda list: list.fitness, reverse=True) #trier les 
    
