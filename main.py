from argparse import ArgumentParser
from nQueens import NQueensSolver
from utils import print_board_representation
import time

parser = ArgumentParser()

parser.add_argument("--n", type=int, default=16, 
                    help="The shape of the rectangular board.")
parser.add_argument("--dont_print_result", action="store_true", 
                    help="If set, does not print the output of the N-Queens solver directly.")
parser.add_argument("--dont_print_representation", action="store_true", 
                    help="If set, does not print the simple view of the output on a 2D board with dots for empty places and 'Q' letters for queens")
parser.add_argument("--dont_print_timing", action="store_true", 
                    help="If set, does not print the ellapsed processing time.")

args = parser.parse_args()

solver = NQueensSolver(args.n)

start_time = time.time()

result_assignment = solver.solve()

if not args.dont_print_timing:
    print(f"Ellapsed time : {time.time() - start_time} seconds.")

if not args.dont_print_result:
    print("Solver's output:")
    print(result_assignment)

if not args.dont_print_representation:
    print(f"Result of {args.n}-Queens problem: ")
    print_board_representation(result_assignment)