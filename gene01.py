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

(nb_of_int, tabdata)=tab_int("small.txt")

# tabdata=[5, -2, -3, 7, 4,10,-10,1]
# nb_of_int=8




class Individual:
    def __init__(self):
        self.gen_code=[0 for i in range(nb_of_int)] # tableau de 0
        n=random.randint(1,nb_of_int)# nb de gene
        t=random.sample([i for i in range(nb_of_int)],n)# tableau d'indices des genes
        for i in t:
            self.gen_code[i]=1
        
        
        
        self.fitness=sum(np.array(self.gen_code)*np.array(tabdata))
        self.length=sum(self.gen_code)


    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people):
        self.ListOfIndividuals = [Individual() for i in range(nb_of_people)]


#trier le code genetic

def crossover_individuals(list):
    offsprings=[]
    split = nb_of_int//2
    for i in range(40):

        A=random.sample(list,2)
        a=A[0]
        b=A[1]
        

        child1 = Individual()
        child2 = Individual()

        
        child1.gen_code = a.gen_code[:split] + b.gen_code[split:]
        child2.gen_code = b.gen_code[:split] + a.gen_code[split:]
        offsprings.append(child1)
        offsprings.append(child2)
    list=list+offsprings
    return list
   # population.ListOfIndividuals.append(child)



def indice(int,indiv):
    L=[]
    for i in range(nb_of_int):
        if indiv.gen_code[i]==int:
            L.append(i)
    return L


def mutate(list):
    for a in list:

        if random.uniform(0.0,1.0)<=0.2:
            
            a.gen_code[random.choice(indice(0,a))],a.gen_code[random.choice(indice(1,a))]=a.gen_code[random.choice(indice(1,a))],a.gen_code[random.choice(indice(0,a))]
            

    return list






def fitness(List): #écart à 0
    for individual in   List:
        individual.fitness=sum(np.array(individual.gen_code)*np.array(tabdata))
    return List


def select_individuals(list):
    list = sorted(list, key=lambda individual: individual.fitness, reverse=True)
    list = list[:19]
    return list






def ga():
    best_sol=[]
    
    population = Population(100)
    for gen in range(1000):

            
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

i1=Individual()
i2=Individual()
a=mutate([i1])
print(a[0].gen_code)
