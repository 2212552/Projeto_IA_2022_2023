from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # TODO
        # Definir uma heuristica para definir a distancia a que o forklift está do objetivo
        # Calcular a distancia do forklift ao objetivo numPassos = |(linhaForklift - linhaObjetivo)| + |(linhaForklift - linhaObjetivo)|

        return abs(state.line_forklift - self._problem.goal_position.line) + abs(state.column_forklift - self._problem.goal_position.column)
        pass

    def __str__(self):
        return "# TODO"

