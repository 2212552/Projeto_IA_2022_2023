from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
import numpy as np

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        #Determine the length of the parent chromosome
        chromosome_length = len(ind1)

        #Select a random crossover point
        cut = np.random.randint(0, chromosome_length - 1)

        #Create the offspring chromosomes by swapping the genetic material
        offspring1 = ind1[:cut] + ind2[cut:]
        offspring2 = ind2[:cut] + ind1[cut:]

        return offspring1, offspring2



    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
