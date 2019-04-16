import random


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

(nb_of_int, tabdata)=tab_int("small.txt")
tabdata=[5, -2, -3, 7, 4,10,-10,1]
nb_of_int=8
class Individual:
    def __init__(self, nb_init):
        self.gen_code=random.sample(tabdata, nb_init)
        self.fitness=-1
        self.length=len(self.gen_code)
        self.nb_init=nb_init

    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people,nb_int):
        self.ListOfIndividuals = [Individual(nb_int) for i in range(nb_of_people)]


#trier le code genetic

def crossover_individuals(list):
    offsprings=[]
    for i in range(80):

        A=random.sample(list,2)
        a=A[0]
        b=A[1]
        n=a.getLen()

        if a.gen_code[n//2]>b.gen_code[n//2]:
            a,b=b,a

        child = Individual(a.nb_init)

        split = n//2
        child.gen_code = a.gen_code[0:split] + b.gen_code[split:n]
        offsprings.append(child)
    list=list+offsprings
    return list
   # population.ListOfIndividuals.append(child)


def randomgene(a):
    L=[]
    for x in tabdata:
        if x not in a.gen_code:
            L.append(x)
    return random.choice(L)



def mutate(list):
    for a in list:

        if random.uniform(0.0,1.0)<=0.2:
            a.gen_code[random.randint(0,len(a.gen_code))-1]=randomgene(a)
            a.gen_code=sorted(a.gen_code)

    return list






def fitness(List): #écart à 0
    for individual in   List:
        individual.fitness=sum(individual.gen_code)
    return List


def select_individuals(list):
    #list = sorted(list, key=lambda individual: individual.fitness, reverse=True)
    list = list[:19]
    return list






def ga():
    best_sol=[]
    for i in range(2,nb_of_int):
        population = Population(100,i)
        for gen in range(1000):

            population.ListOfIndividuals = fitness(population.ListOfIndividuals)
            population.ListOfIndividuals = select_individuals(population.ListOfIndividuals)
            population.ListOfIndividuals= crossover_individuals(population.ListOfIndividuals)
            population.ListOfIndividuals = mutate(population.ListOfIndividuals)
            population.ListOfIndividuals = fitness(population.ListOfIndividuals)


            for individual in population.ListOfIndividuals:
                if individual.fitness==0:
                    best_sol=individual.gen_code
                    print(individual.fitness)

    print(best_sol,sum(best_sol))
    return best_sol

ga()
