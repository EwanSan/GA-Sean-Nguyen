import random
import numpy as np
import matplotlib.pyplot as plt

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
        
        
        
        self.fitness=sum(self.gen_code)
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

        if random.uniform(0.0,1.0)<=0.3:
            n=random.randint(0,nb_of_int-1)
            a.gen_code[n]=(a.gen_code[n]+1)%2
#            a.gen_code[random.choice(indice(0,a))],a.gen_code[random.choice(indice(1,a))]=a.gen_code[random.choice(indice(1,a))],a.gen_code[random.choice(indice(0,a))]
            

    return list






def fitness(List): #écart à 0
    for individual in   List:
        sum_nb=abs(sum(np.array(individual.gen_code)*np.array(tabdata)))
        individual.fitness= 1/(1+sum_nb**(1/2))*sum(individual.gen_code) #la fitness d'une liste qui fait pas 0 n'atteindra jamais plus de nb_of_int
    return List


def select_individuals(list):
    list = sorted(list, key=lambda individual: individual.fitness, reverse=True)
    list = list[:20]
    return list


def cond(list):

    for indiv in list:
        if indiv.fitness!=list[0].fitness:
            return True
    return False



def ga():
    X=[]
    Y1=[]
    Y2=[]
    best_sol=[0 for i in range(nb_of_int)]
    
    
    population1 = Population(100)
    population2 = Population(100)
    population3 = Population(100)
    gen=0
    population1.ListOfIndividuals = fitness(population1.ListOfIndividuals)
    population1.ListOfIndividuals = select_individuals(population1.ListOfIndividuals)
    
    population2.ListOfIndividuals = fitness(population2.ListOfIndividuals)
    population2.ListOfIndividuals = select_individuals(population2.ListOfIndividuals)
    
    while gen<100:
        print("gen =",gen)
        # print( best_sol )
            
        
        population1.ListOfIndividuals= crossover_individuals(population1.ListOfIndividuals) # population1
        population1.ListOfIndividuals = mutate(population1.ListOfIndividuals)
        population1.ListOfIndividuals = fitness(population1.ListOfIndividuals)
        population1.ListOfIndividuals = select_individuals(population1.ListOfIndividuals)
        
        population2.ListOfIndividuals= crossover_individuals(population2.ListOfIndividuals)#population2
        population2.ListOfIndividuals = mutate(population2.ListOfIndividuals)
        population2.ListOfIndividuals = fitness(population2.ListOfIndividuals)
        population2.ListOfIndividuals = select_individuals(population2.ListOfIndividuals) # 2populations evolving separetely if no method applied
        
        X.append(gen)
        Y1.append(population1.ListOfIndividuals[0].fitness)
        Y2.append(population2.ListOfIndividuals[0].fitness)
        
        
        
        
        if abs(sum(np.array(population1.ListOfIndividuals[0].gen_code)*np.array(tabdata)))==0 and population1.ListOfIndividuals[0].fitness>population2.ListOfIndividuals[0].fitness: # comparing the best of both population
            best_sol=population1.ListOfIndividuals[0].gen_code
            #if gen%10==0:#Warring state method
                
                #population1.ListOfIndividuals[-1]=population2.ListOfIndividuals[0] #prizoner add-on
                #population2 = Population(100)
            
        
        if abs(sum(np.array(population2.ListOfIndividuals[0].gen_code)*np.array(tabdata)))==0 and population2.ListOfIndividuals[0].fitness>population1.ListOfIndividuals[0].fitness:
            best_sol=population2.ListOfIndividuals[0].gen_code
            # if gen%10==0:
            #     population2.ListOfIndividuals[-1]=population1.ListOfIndividuals[0] #prizoner add-on
            #     population1 = Population(100)
            # 
        # if gen%10: # Migration method
        #     
        #     population1.ListOfIndividuals[-1]=population2.ListOfIndividuals[0] #Migration method
        #     population2.ListOfIndividuals[-1]=population1.ListOfIndividuals[0] 
        #     print(population1.ListOfIndividuals[0].fitness,population2.ListOfIndividuals[0].fitness)    
        #     
        #     
        gen+=1
       ##   for individual in population.ListOfIndividuals:
        #     print(individual.fitness)
        #     if individual.fitness==0:
        #         best_sol=individual.gen_code
                
    plt.subplot(211)
    plt.plot(X,Y1)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')

    plt.subplot(212)
    plt.plot(X,Y2)
    plt.ylabel('fitness')
    plt.xlabel('Generation')

    plt.show()
    print(best_sol,sum(best_sol),(abs(sum(np.array(best_sol)*np.array(tabdata)))))
    return best_sol

ga()

 