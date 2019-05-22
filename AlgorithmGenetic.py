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

(nb_of_int, tabdata)=tab_int("largeGenerated.txt")

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
        
        nb_of_change=random.randint(1,len(a.gen_code)//100+1)
        if random.uniform(0.0,1.0)<=0.3:
            for i in range(nb_of_change):
                n=random.randint(0,nb_of_int-1)
                a.gen_code[n]=(a.gen_code[n]+1)%2
#            a.gen_code[random.choice(indice(0,a))],a.gen_code[random.choice(indice(1,a))]=a.gen_code[random.choice(indice(1,a))],a.gen_code[random.choice(indice(0,a))]
            

    return list






def fitness(List): #écart à 0
    for individual in   List:
        sum_nb=abs(sum(np.array(individual.gen_code)*np.array(tabdata)))
        individual.fitness= 1/(1+np.log(1+sum_nb**1/2))*(sum(individual.gen_code)**2) #la fitness d'une liste qui fait pas 0 n'atteindra jamais plus de nb_of_int
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
    best_sol=Individual()
    best_sol.fitness=0
    print("Choose your strategy : \n")
    strat = int(input('1 : 1 population, 400 generations (default strategy if unexpected input)\n2 : 2 populations, warring state\n3 : 2 populations, migration\n'))
    gen=0
    nb_of_gen=800
    population1 = Population(100)
    population2 = Population(100)
    population1.ListOfIndividuals = fitness(population1.ListOfIndividuals)
    population1.ListOfIndividuals = select_individuals(population1.ListOfIndividuals)

    if strat==2 or strat==3:
        nb_of_gen=400
        population2.ListOfIndividuals = fitness(population2.ListOfIndividuals)
        population2.ListOfIndividuals = select_individuals(population2.ListOfIndividuals)
    

    while gen<nb_of_gen or (abs(sum(np.array(best_sol.gen_code)*np.array(tabdata)))) !=0:
        print("gen =",gen)
        # print( best_sol )
            
        
        population1.ListOfIndividuals = crossover_individuals(population1.ListOfIndividuals) # population1
        population1.ListOfIndividuals = mutate(population1.ListOfIndividuals)
        population1.ListOfIndividuals = fitness(population1.ListOfIndividuals)
        population1.ListOfIndividuals = select_individuals(population1.ListOfIndividuals)
        if abs(sum(np.array(population1.ListOfIndividuals[0].gen_code)*np.array(tabdata)))==0 and population1.ListOfIndividuals[0].fitness>best_sol.fitness:
            best_sol=population1.ListOfIndividuals[0]
            print("New best solution found")

        X.append(gen)
        Y1.append(population1.ListOfIndividuals[0].fitness)

        if strat==2 or strat==3:
        
            population2.ListOfIndividuals= crossover_individuals(population2.ListOfIndividuals)#population2
            population2.ListOfIndividuals = mutate(population2.ListOfIndividuals)
            population2.ListOfIndividuals = fitness(population2.ListOfIndividuals)
            population2.ListOfIndividuals = select_individuals(population2.ListOfIndividuals) # 2populations evolving separetely if no method applied
            Y2.append(population2.ListOfIndividuals[0].fitness)

            if abs(sum(np.array(population1.ListOfIndividuals[0].gen_code)*np.array(tabdata)))==0 and population1.ListOfIndividuals[0].fitness>best_sol.fitness:
                best_sol=population1.ListOfIndividuals[0]
                print("New best solution found")
            
            if abs(sum(np.array(population2.ListOfIndividuals[0].gen_code)*np.array(tabdata)))==0 and population2.ListOfIndividuals[0].fitness>best_sol.fitness:
                best_sol=population2.ListOfIndividuals[0]
                print("New best solution found")

            if gen%20==0:
                if strat == 2: #Warring method
                    if population1.ListOfIndividuals[0].fitness>population2.ListOfIndividuals[0].fitness: # comparing the best of both population
                        population1.ListOfIndividuals[-1]=population2.ListOfIndividuals[0] #prizoner add-on
                        population1.ListOfIndividuals[-2]=population2.ListOfIndividuals[1]
                        population2 = Population(100)
                        print("War")
                    else:
                        population2.ListOfIndividuals[-1]=population1.ListOfIndividuals[0] #prizoner add-on
                        population2.ListOfIndividuals[-2]=population1.ListOfIndividuals[1]
                        population1 = Population(100)
                        print("War")
                
                else: #Migration method
                    population1.ListOfIndividuals[-1]=population2.ListOfIndividuals[0] #Migration method
                    population1.ListOfIndividuals[-2]=population2.ListOfIndividuals[1]
                    population2.ListOfIndividuals[-1]=population1.ListOfIndividuals[0]
                    population2.ListOfIndividuals[-2]=population1.ListOfIndividuals[1]
                    print("Migration")   
 
        gen+=1
       ##   for individual in population.ListOfIndividuals:
        #     print(individual.fitness)
        #     if individual.fitness==0:
        #         best_sol=individual.gen_code
                
    plt.subplot(211)
    plt.plot(X,Y1)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')

    if strat==2 or strat==3:
        plt.subplot(212)
        plt.plot(X,Y2)
        plt.ylabel('Fitness')
        plt.xlabel('Generation')

    plt.show()
    print(best_sol.gen_code,sum(best_sol.gen_code),(abs(sum(np.array(best_sol.gen_code)*np.array(tabdata)))),len(best_sol.gen_code))
    return best_sol.gen_code

ga()

