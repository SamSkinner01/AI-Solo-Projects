import random
import copy 

def generate_random_state(n):
    """
    Generates a random state for the N Queens Problem.
    """
    state = []
    for i in range(n):
        state.append(random.randint(0, n-1))
    return state

def get_value(state, n):
    """
    Given a state, returns the number of pairs of queens that are not attacking each other.
    """
    # First we will count the number of pairs of queens that are attacking each other.
    attacking_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                attacking_pairs += 1
    # Now we will subtract this number from the total number of pairs of queens.
    total_pairs = n*(n-1)/2
    return total_pairs - attacking_pairs
    

def get_best_neighbor(state, n):
    """
    Given a state, returns the neighbor with the highest number of non-attacking pairs of queens.
    """
    best_neighbor = None
    best_neighbor_value = -1
    for i in range(n):
        for j in range(n):
            if i != j:
                neighbor = copy.deepcopy(state)
                neighbor[i] = j
                neighbor_value = get_value(neighbor, n)
                if neighbor_value > best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value
    return best_neighbor, best_neighbor_value

def hill_climbing(state, n):
    """
    Given an initial state, returns a local maximum.
    """
    current = state
    while True:
        neighbor, neighbor_value = get_best_neighbor(current, n)
        if neighbor_value <= get_value(current, n):
            return current
        current = neighbor

def print_board(state):
    """
    Given a state, prints the board.
    """
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()       

def is_valid_solution(state, n):
    """
    Given a state, returns True if it is a valid solution.
    """
    return get_value(state, n) == n*(n-1)/2

def main():
    # We will create an initial state for the N Queens Problem.
    n = 8
    initial_state = generate_random_state(n)
    solution = hill_climbing(initial_state, n)
    failure = 0
    success = 0
    i = 0
    j = 0
    while j < 10:
        success = 0
        failure = 0
        i = 0
        while i < 100:
            initial_state = generate_random_state(n)
            solution = hill_climbing(initial_state, n)
            if is_valid_solution(solution, n):
                success += 1
            else:
                failure += 1
            i += 1
        j+= 1
        print(f"Success rate is: {success/100 * 100:.0f} ")



    

if __name__ == "__main__":
    main()
