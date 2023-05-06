import random
import copy
import time
def create_initial_board(n):
    """
    Generates N-Queens board with random initial state
    """
    board = []
    for i in range(n):
        board.append(random.randint(0, n-1))
    return board

def print_board(board):
    """
    Prints the board. The input should contain 
    an array that contains the row number for the column index
    """
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def columns_with_conflicts(board):
    """
    Returns a list of columns with conflicts
    """
    n = len(board)
    conflicts = []
    for i in range(n):
        for j in range(i+1, n):
            # If the two queens are in the same row
            if board[i] == board[j]:
                conflicts.append(i)
                conflicts.append(j)
            # If the two queens are in the same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts.append(i)
                conflicts.append(j)

    return conflicts
    
def find_min_conflicts(board, column):
    """
    Finds the row with the minimum conflicts for a given column
    """
    n = len(board)
    min_conflicts = float("inf")
    min_row = board[column]

    for i in range(n):
        # If the row is not the same as the current row
        if i != board[column]:
            temp_board = copy.deepcopy(board)
            temp_board[column] = i
            # Find the number of conflicts for the new board
            conflicts = len(columns_with_conflicts(temp_board))
            # If conflicts is smaller than the current minimum conflicts
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_row = i

    return min_row


def get_new_board(board, column, row):
    """
    Returns a new board with the new row for the given column
    """
    new_board = copy.deepcopy(board)
    new_board[column] = row
    return new_board

def min_conflicts(board, max_steps):
    current = copy.deepcopy(board)
    i = 0
    while i < max_steps:
        if current is not None and columns_with_conflicts(current) == []:
            return current, i
        
        var = random.choice(columns_with_conflicts(current))
        value = find_min_conflicts(current, var)
        current = get_new_board(current, var, value)
        
        i+=1
    return None, i


def test(max_steps):
    n = int(input("Enter number of queens: "))
    #print("Initial board:")
    #print_board(board)

    # solution = min_conflicts(board, 50)
    # if solution is None:
    #     print("No solution found")
    # else:
    #     print_board(solution)


    found_sol = 0
    didnt_find_sol = 0
    avg = 0
    avg_time = 0
    while found_sol < 50:
        board = create_initial_board(n)
        start = time.time()
        solution, steps = min_conflicts(board, max_steps)
        end = time.time()
        if solution is not None:
            print(f"Found Solution #{found_sol+1} in {steps} steps")
            #print_board(solution)
            found_sol += 1
            avg += steps
            avg_time += end - start
        else:
            didnt_find_sol += 1

    print(f"Average steps: {avg/50}")
    print(f"Percentage of times a solution was found: {found_sol/(found_sol + didnt_find_sol) * 100:.2f}%")
    print(f"Average time: {avg_time/50:.5f} seconds")


def main():
    test(1000)
    



if __name__ == "__main__":
    main()
