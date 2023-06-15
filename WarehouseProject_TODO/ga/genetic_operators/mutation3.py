from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        # Semelhante ao mutation 2 se der para arranjar 1 melhor trocar
        for i in range(len(ind.genome)):
            if ind.genome[i] % 2 == 0:
                ind.genome[i] = ind.genome[i] + 2
            else:
                ind.genome[i] = ind.genome[i] - 2
        pass

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
