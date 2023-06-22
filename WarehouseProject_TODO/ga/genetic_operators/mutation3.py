import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        #TODO
        #SCRAMBLE MUTATION
        # 1. Choose two random positions in the individual
        # 2. Shuffle the values of the two positions
        # ANTES DE MUTAR
        size = ind.num_genes

        child = ind.genome.copy()

        start = np.random.randint(0, size - 1)
        end = np.random.randint(start + 1, size)

        while end == start:
            end = np.random.randint(start + 1, size)

        subarray = child[start:end+1]
        np.random.shuffle(subarray)
        child[start:end+1] = subarray

        ind.genome = child


    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
