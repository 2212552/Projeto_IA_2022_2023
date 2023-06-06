import numpy as np

from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO

     #   print(self.genome)


    def compute_fitness(self) -> float:
        # TODO
        print(self.genome)




        #wharehouseproblemga
        # return uma instancia da class Warehouse individual, com o tamnho dos genes


        #preencher o genoma com valores aleatorios (int vetor individula)
        #fazer print para ver como ele esta feito

        #aceder as distancias problemGA
        #-> distancias goals
        #-> sitancias dos forklifts
        #self.problem.agent_search

        #a distancia do forklift ao primeiro porduto e do primeiro produto aao segundo ate chegar ao ultimo produto
        # somar as distancias todas
        #buscar celulas do forklift
        #buscar a celula do produto 1
        #procurar o par na lista de pares
        #seprar os produtos por forklift


        l_forklifts = self.problem.agent_search.forklifts
        products = self.problem.agent_search.products
        l_products=[]
        aux=[]
        arr_genomas = self.genome
        #PREENCHER A LISTA DE PRODUTOS POR FORKLIFTS
        agent = 0

        breaker_pos = []


        for i in range(arr_genomas.size):
            print(arr_genomas[i])
            if not (arr_genomas[i] <= len(products)):
               breaker_pos.append(i)

        result = []
        prev_position = 0

        for pos in breaker_pos:
            if len(breaker_pos) > 1 and prev_position != 0:
                subarray = arr_genomas[(prev_position+1):pos]
                result.append(subarray)
                prev_position = pos
            else:
                subarray = arr_genomas[prev_position:pos]
                result.append(subarray)
                prev_position = pos

        # Add the remaining portion as the last subarray
        result.append(arr_genomas[(prev_position+1):])
        print("LISTA:")
        print(breaker_pos)
        #recolher os produtos todos
        #recolher os forklifts


        return 0

    def obtain_all_path(self):
        # TODO
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance