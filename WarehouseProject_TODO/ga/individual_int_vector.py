
from abc import abstractmethod
from ga.problem import Problem
from ga.individual import Individual
import numpy as np
import random
class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        #size = 5  # Desired size of the array
        #range_start = 1  # Start of the range (inclusive)
        #range_end = 100  # End of the range (exclusive)

        self.genome = random.sample(range(1, num_genes+1),num_genes)
        #self.genome = np.array(random.sample(range(1, num_genes+1), num_genes))

        #print("ddd")
        #print("GENOME: ", self.genome)

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
