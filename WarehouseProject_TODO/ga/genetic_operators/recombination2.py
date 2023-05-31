from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        self.recombine(ind1, ind2)
        pass


    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
