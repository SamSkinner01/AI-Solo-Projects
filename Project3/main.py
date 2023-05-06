import sys
import numpy as np
from simulated_annealing import *
import time

TEST_RUNS = 50

def test():
    avg_time = 0
    n = 15
    temperature = 10
    s, f = 0, 0
    for i in range(TEST_RUNS):
        state = create_random_state(n)
        start = time.time()
        goal = simulated_annealing(state, n, temperature)
        end = time.time()
        if not is_solution(goal, n):
            f += 1
            print(f"Run {i}: Failed to find solution", end=", ")
        else:
            s += 1
            print(f"Run {i}: Found solution", end=", ")
        print(f"Run {i}: Time: {end-start:.8f} seconds")
        avg_time += end-start
    print(f"Success rate: {s/TEST_RUNS*100:.2f}%")
    print(f"Average time: {avg_time/TEST_RUNS:.8f} seconds")


def main():
    test()

if __name__ == "__main__":
    main()