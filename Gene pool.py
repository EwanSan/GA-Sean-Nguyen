class Individuals:
    def __init__(self,gen_code,sum,len,):
        self.gen_code=gen_code
        self.sum=sum
        self.len=len
        
    def getFitness(self):
        return self.sum
        
        
        
        
        
        
class Population:
    def __init__(self,ListOfIndividuals):
        self.ListOfIndividuals=ListOfIndividuals
        
        
