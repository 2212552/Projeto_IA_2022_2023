from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # Por exemplo um produto com as cordenadas [3,2] fica [2,3]
        for i in range(len(ind.genome)):
            if ind.genome[i] % 2 == 0:
                ind.genome[i] = ind.genome[i] + 1
            else:
                ind.genome[i] = ind.genome[i] - 1


    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
