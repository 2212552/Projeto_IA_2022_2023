import math
import random

import numpy as np

from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO


        #---------------------- ORDERED CROSSOVER ----------------------
        #ANTES DE RECOMBINAR
        print(f"ANTES ind1: {ind1.genome}")
        print(f"ANTES ind2: {ind2.genome}")

        print("--> 1º",ind1.genome, ind2.genome)

        # size = ind1.num_genes
        #
        # # Choose random start/end position for crossover
        # child1, child2 = [-1] * size, [-1] * size
        # start, end = sorted([random.randrange(size) for _ in range(2)])
        #
        # print(f"size: {size}")
        #
        # # Replicate ind1 sequence for child1, ind2 sequence for child2
        # child1_inherited = []
        # child2_inherited = []
        # for i in range(start, end + 1):
        #     child1[i] = ind1.genome[i]
        #     child2[i] = ind2.genome[i]
        #     child1_inherited.append(ind1.genome[i])
        #     child2_inherited.append(ind2.genome[i])
        #
        # print("--> 2º",child1, child2)
        #
        # # Fill the remaining position with the other parents' entries
        # current_ind2_position, current_ind1_position = 0, 0
        #
        # fixed_pos = list(range(start, end + 1))
        # i = 0
        # while i < size:
        #     if i in fixed_pos:
        #         i += 1
        #         continue
        #
        #     test_child1= child1[i]
        #     if test_child1 == -1:  # to be filled
        #         ind2_trait = ind2.genome[current_ind2_position]
        #         while ind2_trait in child1_inherited:
        #             current_ind2_position += 1
        #             ind2_trait = ind2.genome[current_ind2_position]
        #         child1[i] = ind2_trait
        #         child1_inherited.append(ind2_trait)
        #
        #     # repeat block for child2 and mom
        #     i += 1

        size = ind1.num_genes

        parent1 = ind1.genome
        parent2 = ind2.genome


        # Choose random start/end position for crossover
        #alice, bob = [-1] * size, [-1] * size
        start = np.random.randint(0, size - 1)
        end = np.random.randint(start + 1, size)
        center = math.floor((start + end) / 2)


        while end == start:
            end = np.random.randint(start + 1, size)

        subarray_parent1=[0 for i in range(size)]
        subarray_parent1[start:end+1] = parent1[start:end+1]

        subarray_parent2=parent2.copy()

        for item in subarray_parent1:
            if item in parent2:
                subarray_parent2[parent2.index(item)] = 0

        counter = 0
        for i in subarray_parent2.copy():
            if i != 0:
                if subarray_parent1[counter] == 0:
                   subarray_parent1[counter] = i

                while subarray_parent1[counter] != 0 and counter+1<size and subarray_parent1[counter+1] != 0:
                    counter += 1
                counter += 1

            else:
                subarray_parent2[i]= subarray_parent1[counter]

        print()
    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
