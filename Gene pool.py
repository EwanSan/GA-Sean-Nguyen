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

class Individual:
    def __init__(self, nb_init):
        self.gen_code=random.sample(tabdata, nb_init)
        self.fitness=-1
        self.length=len(self.gen_code)

    def getFitness(self):
        return self.fitness

    def getLen(self):
        return self.length


class Population:
    def __init__(self,nb_of_people):
        self.ListOfIndividuals = [Individual(4) for _ in range(nb_of_people)]



#C'est mon test
def ga():
    population = Population(100)
    for individual in population.ListOfIndividuals:
        print(individual.gen_code)
        print("\n")

ga()
        
#trier le code genetic

listgen=[1,2,3,4,5,6,7,8,9]
def crossover_individuals(a,b): # melanger le code génétique sans qu'il y ait de répetitions et sans 
    n=a.getLen()

    if a.gen_code[n//2]>b.gen_code[n//2]:
        a,b=b,a
        
    child = Individual([])
       
    split = n//2
    child.gen_code = a.gen_code[0:split] + b.gen_code[split:n]
   # population.ListOfIndividuals.append(child)
    
 
def randomgene(a):
    L=[]
    for x in listgen:
        if x not in a.gen_code:
            L.append(x)
    return random.choice(L)
    
    

def mutate(a):
    if random.uniform(0.0,1.0)<=0.2:
        a.gen_code[random.randint(1,len(a.gen_code))-1]=randomgene(a)
        a.gen_code=sorted(a.gen_code)
    print(a.gen_code)
    
    
    
        
 
    
    
    
    
    

def fitness(List): #écart à 0 
    for individual in   List:
        individual.fitness=sum(individual.gen_code)
        

def select_individuals(list):
    list = sorted(list, key=lambda list: list.fitness, reverse=True) #trier les individuals
    
    
a=Individual([1,2,3,4]) # test 
b=Individual([5,6,7,8])    
crossover_individuals(a,b)
random.choice(listgen)
randomgene(a)
mutate(a)

