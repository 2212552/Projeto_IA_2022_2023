import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()

        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        #self.matrix = np.full([self.rows, self.columns], fill_value=0, dtype=int)

        # for i in range(self.rows):
        #     for j in range(self.columns):
        #         self.matrix[i][j] = matrix[i][j]
        #         if self.matrix[i][j] == constants.FORKLIFT:
        #             self.line_forklift = i
        #             self.column_forklift = j
        #         if self.matrix[i][j] == constants.EXIT:
        #             self.line_exit = i
        #             self.column_exit = j

    def can_move_up(self) -> bool:

        # CONDIÇOES PARA O FORKLIFT SE MOVER PARA CIMA
        # 1 - PODE MOVER CASO ESTEJA A ACIMA DE 0 E FOR MENOR QUE O DO NUMERO DE LINHAS -1
        # 2 - PODE MOVER CASO NÃO SEJA UMA PARTELEIRA (SHELF) OU UM PRODUTO (PRODUCT)

        return self.line_forklift > 0\
            and self.matrix[self.line_forklift -1][self.column_forklift] != constants.SHELF \
            and self.matrix[self.line_forklift - 1][self.column_forklift] != constants.PRODUCT

        #TEM DE SER DIFERENTE DA SELF E DIFERENTE DA PRODUCT




    def can_move_right(self) -> bool:

        #CONDIÇOES PARA O FORKLIFT SE MOVER PARA A DIREITA
        # 1 - PODE MOVER CASO A POSIÇÃO NÃO EXECEDE O NUMERO DE COLUNAS -1
        # 2 - PODE MOVER CASO NÃO SEJA UMA PARTELEIRA (SHELF) OU UM PRODUTO (PRODUCT)

        return self.column_forklift < self.columns-1 \
            and self.matrix[self.line_forklift][self.column_forklift + 1] != constants.SHELF \
            and self.matrix[self.line_forklift][self.column_forklift + 1] != constants.PRODUCT



    def can_move_down(self) -> bool:

        #CONDIÇOES PARA O FORKLIFT SE MOVER PARA BAIXO
        # 1 - PODE MOVER CASO O SEJA > 0
        # 2 - PODE MOVER CASO NÃO SEJA UMA PARTELEIRA (SHELF) OU UM PRODUTO (PRODUCT)

        return self.line_forklift < self.rows - 1 \
            and self.matrix[self.line_forklift + 1][self.column_forklift] != constants.SHELF \
            and self.matrix[self.line_forklift + 1][self.column_forklift] != constants.PRODUCT

    def can_move_left(self) -> bool:

        #CONDIÇOES PARA O FORKLIFT SE MOVER PARA ESQUERDA
        # 1 - PODE MOVER CASO A POSIÇÃO ATUAL DO FORKLIFT > 0
        # 2 - PODE MOVER CASO NÃO SEJA UMA PARTELEIRA (SHELF) OU UM PRODUTO (PRODUCT)

        return self.column_forklift > 0 \
            and self.matrix[self.line_forklift][self.column_forklift - 1] != constants.SHELF \
            and self.matrix[self.line_forklift][self.column_forklift - 1] != constants.PRODUCT

    def move_up(self) -> None:
       # self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift -= 1
        #self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT


    def move_right(self) -> None:
        #self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift += 1
       # self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_down(self) -> None:
       # self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift += 1
        #self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT


    def move_left(self) -> None:
       # self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift -= 1
        #self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT


    def get_cell_color(self, row: int, column: int) -> Color:
        if self.matrix[row][column] == constants.EXIT:
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return self.line_forklift == other.line_forklift and self.column_forklift == other.column_forklift
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
