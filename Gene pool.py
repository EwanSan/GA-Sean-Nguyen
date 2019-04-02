class Individual:
    def __init__(self,gen_code,fitness):
        self.gen_code=gen_code
        self.fitness=
        self.len=len
        
    def getFitness(self):
        return self.sum
        
        
        
        
        
        
class Population:
    def __init__(self,ListOfIndividuals):
        self.ListOfIndividuals=ListOfIndividuals
        
#trier le code genetic

def fitness(List): #écart à 0
    for individual in   List:
        individual.fitness=sum(individual.gen_code)
        

def select_individuals(list):
    list = sorted(list, key=lambda list: list.fitness, reverse=True) #trier les 
    