import unittest
from nQueens import NQueensSolver
from utils import is_valid_assignment
from random import randint

N_MIN, N_MAX = 10, 1000

class TestNQueensSolver(unittest.TestCase):

    def random_test_1(self):
        solver = NQueensSolver(randint(N_MIN, N_MAX))
        self.assertFalse(is_valid_assignment(solver.solve()))

    def random_test_2(self):
        solver = NQueensSolver(randint(N_MIN, N_MAX))
        self.assertFalse(is_valid_assignment(solver.solve()))
    
    def random_test_3(self):
        solver = NQueensSolver(randint(N_MIN, N_MAX))
        self.assertFalse(is_valid_assignment(solver.solve()))
    
    def random_test_4(self):
        solver = NQueensSolver(randint(N_MIN, N_MAX))
        self.assertFalse(is_valid_assignment(solver.solve()))
    
    def random_test_5(self):
        solver = NQueensSolver(randint(N_MIN, N_MAX))
        self.assertFalse(is_valid_assignment(solver.solve()))

if __name__ == '__main__':
    unittest.main() 