from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

    def generate_individual(self) -> "WarehouseIndividual":
        # TODO
        #
        # 4 produtos
        # 2 agetns
        #
        # 1 x 3 agent
        # 2 x 4 agent
        #

        # pensar num vetor que iria organizar isso
        #
        # genome tem de ser valores sequenciais
        new_individual = WarehouseIndividual(self, len(self.products) + len(self.forklifts) - 1)
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

