import unittest
from nQueens import NQueensSolver
from utils import is_valid_assignment
from random import randint
from time import time

N_MIN, N_MAX = 10, 150

def test_case(n):
    print("\nAssigned N: {}".format(n))
    st = time() # start time
    solver = NQueensSolver(n)
    is_valid = is_valid_assignment(solver.solve())
    print("\nSolved in {:.3f} seconds.\n".format(time() - st))
    return is_valid

class TestNQueensSolver(unittest.TestCase):

    def test_random_1(self):
        n = randint(N_MIN, N_MAX)
        self.assertTrue(test_case(n))

    def test_random_2(self):
        n = randint(N_MIN, N_MAX)
        self.assertTrue(test_case(n))
    
    def test_random_3(self):
        n = randint(N_MIN, N_MAX)
        self.assertTrue(test_case(n))
    

if __name__ == '__main__':
    unittest.main() 