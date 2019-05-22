# GA-Sean-Nguyen
Genetic algorithm project.

PROBLEM: Given a set of integers, does it exist a subset of integers whose sum is 0? If yes, provide the subset of integers of largest cardinal size. 

METHOD: In order to solve the problem mentioned above, we are going to use a genetic algorithm. This method is inspired by the evolution theory of Darwin and in particular by natural selection: we simulate a population and its evolution through numerous generations. The basic steps of this algorithm are the following: 
(i) Calculate the fitness of every individual in the population (how close each individual is from the solution we need). 
(ii) Select the individuals with the best fitness. 
(iii) Mix the remaining individuals with crossover in order to create new ones (inspired by chromosomal crossover). (iv) Introduce mutations in order to give more variety. 
Then repeat these steps through multiple generations. 

OPTIMIZATIONS: Strategies involvings 2 interactings populations.


How to use the files.
-Copy the txt files in the same folder as the .py file
-write the .txt filename in the .py file to use it
-execute the .py, input the strategy:
1- 1 population
2- 2 populations: Warring states
3- 2 populations : Migration
4- 2 populations : independants

A graph will appear showing the evolution of the fitness for the populations.
- close the graph to see in the terminal, the best solution along with its length.

