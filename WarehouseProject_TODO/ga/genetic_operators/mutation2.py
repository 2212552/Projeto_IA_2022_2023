import random

from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:

        #SWAP MUTATION
        # 1. Choose two random positions in the individual
        # 2. Swap the values of the two positions

       # print(f"ANTES MUT- ind1: {ind.genome}")
        size = ind.num_genes
        ind_to_mutate = ind.genome.copy()
        first = random.randint(0, size - 1)

        # Generate a second random value different from the first one
        secound = random.randint(0,  size - 1)
        while secound == first:
            secound = random.randint(0,  size - 1)

        ind.genome[first], ind.genome[secound]=ind_to_mutate[secound],ind_to_mutate[first]

        #print(f"DEPOIS MUT- ind1: {ind.genome}")



    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
