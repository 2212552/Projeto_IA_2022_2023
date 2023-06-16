from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
import numpy as np

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        random_number=np.random.randint(0,10)

        for i in range(len(ind.genome)):
            if ind.genome[i] % 2 == 0:
                ind.genome[i] = ind.genome[i] + random_number
            else:
                ind.genome[i] = ind.genome[i] - random_number
        pass

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
