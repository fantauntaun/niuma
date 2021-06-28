import numpy as np

class grid:
    def __init__(self, L, H, matrix):
        self.L = L
        self.H = H
        self.matrix = matrix
        self.n = len(self.matrix)  #number of grid each col / row 

    def visit_node(self, coordinate):
        grid_index = self.get_grid_index(coordinate)
        self.matrix[grid_index[0], grid_index[1]] = 1

    def get_grid_index(self, coordinate):  #coordinate, a tuple or list length 2
        x_list = [k*(self.L/self.n) for k in range(self.n+1)]
        y_list = [k*(self.H/self.n) for k in range(self.n+1)]
        normalized_coordinate = [i for i in coordinate] #need to be normalized to the length and width
        x_list = [i-normalized_coordinate[0] for i in x_list]
        y_list = [i-normalized_coordinate[1] for i in y_list]
        x_index = list(map(lambda i: i>0, x_list)).index(True)
        y_index = list(map(lambda i: i>0, y_list)).index(True)
        if x_index == self.n:
            x_index -= 1
        if y_index == self.n:
            y_index -= 1        
        return [x_index, y_index]



    def __iter__(self):
        return self

    def __next__(self):
        return self

    def __repr__(self):
        return f"{self.matrix}"

    def __str__(self) -> str:
        return f"{repr(self.matrix)}"