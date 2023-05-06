"""
Implementation of simulated annealing for the n-queens problem
"""

import numpy as np
import random

def print_board(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[j] == i:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()

def is_solution(state, n):
    return eval(state, n) == 0


def create_random_state(n):
    # Every index represents the row the queen is in
    # ex) [3. 1. 0. 2.]
    # index 0 is column 1. Column 1 has a queen in row 3 (index 0 is row 0)
    state = np.zeros(n)
    for i in range(len(state)):
        state[i] = random.randint(0,n-1)
    return state


def eval(state, n):
    # Check for horizontal conflicts
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                conflicts += 1
    # Check for diagonal conflicts
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if abs(i-j) == abs(state[i]-state[j]):
                conflicts += 1
    return conflicts

def temperature_scheduler(t):
    return t*0.999

def acceptance_probability(delta_e, t):
    return np.exp(-delta_e/t)

def random_neighbor(state):
    neighbor = np.copy(state)
    i = random.randint(0,len(state)-1)
    neighbor[i] = random.randint(0,len(state)-1)
    return neighbor

def simulated_annealing(state, n, temperature=1_000_000):
    current = state
    t = temperature
    while t > 0.01:
        t = temperature_scheduler(t)
        neighbor = random_neighbor(current)
        epsilon = eval(neighbor, n) - eval(current, n)
        if epsilon < 0:
            current = neighbor
        else:
            if random.random() < acceptance_probability(epsilon, t):
                current = neighbor
    return current


        
