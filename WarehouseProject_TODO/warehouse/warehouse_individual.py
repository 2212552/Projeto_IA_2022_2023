import numpy as np

from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO (VER COM A PROF)
        self.fitness = 0
        self.result = []

     #   print(self.genome)


    def compute_fitness(self) -> float:
        # TODO (VER COM A PROF)
        #print(self.genome)

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

        self.fitness = 0

        l_forklifts = self.problem.agent_search.forklifts
        self.agents = len(l_forklifts)
        l_products = self.problem.agent_search.products

        arr_genomas = self.genome

        #PROCURAR ONDE ESTAO OS BREAKPOINTS NO GENOMA
        breaker_pos = []

        for i in range(len(arr_genomas)):
            #print(arr_genomas[i])
            if not (arr_genomas[i] <= len(l_products)):
               breaker_pos.append(i)

        result = []
        prev_position = 0
        firstTime = True

        #PARA TESTAR
        # if breaker_pos[0] == 0:
        #     print("ERRO")

        #CONSTRUIR A LISTA DE PRODUTOS POR FORKLIFTS
        for pos in breaker_pos:
            #if len(breaker_pos) > 1 and not firstTime:
            if firstTime:
                #[2,1,3]
                subarray = arr_genomas[prev_position:pos]
                result.append(subarray)

                firstTime = False
            else:
                subarray = arr_genomas[(prev_position):pos]
                result.append(subarray)
            prev_position = pos + 1

        # Add the remaining portion as the last subarray
        if len(breaker_pos) >= 1:
            #o prev_position so é definido no for
            result.append(arr_genomas[prev_position:])
        else:
            result.append(arr_genomas.copy())
        #print("LISTA:")
        #print(breaker_pos)

        self.result= result
        self.distanceForklift=np.zeros(len(result))

        #CALCULAR O FITNESS-> SOMAR AS DISTANCIAS
        #print(range(result.__len__()))
        for i in range(result.__len__()):
            start = l_forklifts[i]
            #Agent que não tem nada para fazer (VAZIO)
            if result[i].__len__() == 0:
                self.fitness+=self.calculate_distance(start, self.problem.agent_search.exit)
                self.distanceForklift[i]+=self.calculate_distance(start, self.problem.agent_search.exit)

                continue
            for k in range(result[i].__len__()+1):
                #CASO SEJA IGUAL AO TAMANHO DO RESULT, É O EXIT
                if result[i].__len__() == k:
                    end = self.problem.agent_search.exit
                else:
                    end = l_products[result[i][k]-1]

                self.fitness += self.calculate_distance(start, end)
                self.distanceForklift[i]+=self.calculate_distance(start, end)
                start = end

        self.fitness+=np.max(self.distanceForklift)
        #self.show_agents()

        return self.fitness

    def calculate_distance(self, start, end):
        pairs = self.problem.agent_search.pairs

        for pair in pairs:
            if ((pair.cell1 == start and pair.cell2 == end) or (pair.cell1 == end and pair.cell2 == start)):
                return pair.value

    # def show_agents(self):
    #     agent_counter = 0
    #     print("-------------------------------------")
    #     for products in self.result:
    #         agent_counter += 1
    #         print(f"Agent: {agent_counter}")
    #         print(f"{products}" + "\n")
    #         # for item in products:
    #         #     string += str(item) + " "
    #     print("-------------------------------------")

    def obtain_all_path(self):

           pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genoma: ' + f'{self.genome}' + "\n\n"
        #string += 'Agents: ' + f'{self.result}' + "\n\n"

        agent_counter = 0
        for i, products in enumerate(self.result):
            agent_counter += 1
            string += "\nAgent: " + str(agent_counter) + "\nProducts:"

            for item in products:
                string += str(item) + " "
            string+="\n" + "distance: " + str(self.distanceForklift[i]) + "\n"
        # TODO (VER COM A PROF)
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.result = self.result
        new_instance.distanceForklift = self.distanceForklift
        # TODO (VER COM A PROF)
        return new_instance