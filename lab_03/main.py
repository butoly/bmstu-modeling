import numpy
from numpy.linalg.linalg import LinAlgError


class KolmogorovSolver:
    def __init__(self, matrix):
        self.matrix = matrix

    def times_ceq(self):
        try:
            res = numpy.linalg.solve(self.__coef_matrix(),
                                     self.__init_coef(len(self.matrix)))
            time_res = self.__zero_filling(len(matrix))

            for i in range(len(matrix)):
                lmbd = .0
                for j in range(len(matrix[i])):
                    if (i != j):
                        lmbd += matrix[i][j]
                time_res[i] = (1 - res[i]) / (res[i] * lmbd)
                time_res[i] = round(time_res[i], 4)

            print("\nTimes")
            print(time_res)

        except LinAlgError:
            res = []
        print("\nSolved matrix")
        print(res)

    def __coef_matrix(self):
        self.matrix = numpy.array(self.matrix)
        size = len(matrix)
        res = numpy.zeros((size, size))
        for state in range(size - 1):
            for col in range(size):
                res[state, state] -= self.matrix[state, col]
            for row in range(size):
                res[state, row] += self.matrix[row, state]

        for state in range(size):
            res[size - 1, state] = 1

        print(res)
        return res

    def __init_coef(self, size):
        coef = []
        for i in range(size):
            if (i == size - 1):
                coef.append(1.0)
            else:
                coef.append(0.0)
        return numpy.array(coef)

    def __zero_filling(self, size):
        return [0.0 for i in range(size)]


if __name__ == "__main__":
    # matrix = [
    #     [0, 1, 3],
    #     [1, 0, 2],
    #     [3, 0, 0],
    # ]
    #
    # matrix = [
    #     [0, 2, 1, 0],
    #     [1, 0, 1, 3],
    #     [1, 0, 0, 0],
    #     [3, 1, 1, 0],
    # ]

    matrix = [
        [0, 1, 1, 2, 0],
        [3, 0, 0, 4, 0],
        [1, 0, 0, 0, 3],
        [1, 1, 3, 0, 0],
        [1, 0, 0, 5, 0],
    ]

    solver = KolmogorovSolver(matrix)
    solver.times_ceq()



