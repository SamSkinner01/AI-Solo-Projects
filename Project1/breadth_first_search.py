import random
import time
from collections import deque

TIME_LIMIT_IN_SECONDS = 10
TEST_RUNS = 20

class Node:
    """
    A Node consists of a parent, a stateful representation of the 8-puzzle,
    and action taken to reach the state, and the path cost to reach the state.
    """
    def __init__(self, parent, state, action, path_cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.path_cost = path_cost

class EightPuzzle:
    def __init__(self):
        self.goal_state = [[0,1,2], [3,4,5], [6,7,8]]

        # Generate a random initial state. Not all initial states are solvable.
        self.init_state = self.generate_random_state()
        self.init_node = Node(parent=None, state=self.init_state, action=None, path_cost=0)

    def print_state(self, state):
        for i in range(3):
            for j in range(3):
                print(state[i][j], end=" ")
            print()
        print()

    def test(self):
        success, failure = 0, 0

        for i in range(TEST_RUNS):
            print("Test run", i+1)
            self.init_state = self.generate_random_state()
            goal_node = self.breadth_first_search()
            if goal_node is not None:
                print("Solution found!")
                print("Path cost:", goal_node.path_cost)
                print("Actions:")
                actions = []
                node = goal_node
                while node.parent is not None:
                    actions.append(node.action)
                    node = node.parent
                actions.reverse()
                print(actions)
                success += 1
            else:
                print("Solution not found.")
                failure += 1
            print()
        print(f"Sucess Rate is: {success/TEST_RUNS}")

    def one_solution(self):
        self.init_state = [
            [3,0,1],
            [6,4,2],
            [7,8,5]
        ]
        self.init_node = Node(parent=None, state=self.init_state, action=None, path_cost=0)
        goal_node = self.breadth_first_search()
        if goal_node is not None:
            print("Solution found!")
            self.print_state(goal_node.state)
            print("Path cost:", goal_node.path_cost)
            print("Actions:")
            actions = []
            node = goal_node
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent
            actions.reverse()
            print(actions)
        else:
            print("Solution not found.")
        

    def generate_random_state(self):
        """
        Generates a random state by shuffling the list [0,1,2,3,4,5,6,7,8] 
        """
        n = [0,1,2,3,4,5,6,7,8]
        random.shuffle(n)
        state = []
        for i in range(0, 9, 3):
            state.append(n[i:i+3])
        return state    

    def goal_test(self, state):
        return state == self.goal_state
    
    def find_blank_square(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    
    def move(self, state, blank_i, blank_j, action):
        """
        Given a current state, the location of the blank square, and an action,
        returns a new state if the action is valid. Otherwise, returns None.
        """
        new_state = [row[:] for row in state]
        if action == "up":
            if blank_i == 0:
                return None
            new_state[blank_i][blank_j] = new_state[blank_i-1][blank_j]
            new_state[blank_i-1][blank_j] = 0
        elif action == "down":
            if blank_i == 2:
                return None
            new_state[blank_i][blank_j] = new_state[blank_i+1][blank_j]
            new_state[blank_i+1][blank_j] = 0
        elif action == "left":
            if blank_j == 0:
                return None
            new_state[blank_i][blank_j] = new_state[blank_i][blank_j-1]
            new_state[blank_i][blank_j-1] = 0
        elif action == "right":
            if blank_j == 2:
                return None
            new_state[blank_i][blank_j] = new_state[blank_i][blank_j+1]
            new_state[blank_i][blank_j+1] = 0
        return new_state
    

    
    def expand(self, node):
        """
        Given a node, return all the children of that node
        """
        children = []
        i, j = self.find_blank_square(node.state)
        for action in ["up", "down", "left", "right"]:
            new_state = self.move(node.state, i, j, action)
            if new_state is not None:   
                child = Node(parent=node, state=new_state, action=action, path_cost=node.path_cost+1)
                children.append(child)
        return children
    
    def breadth_first_search(self):
        """
        Breadth-first search algorithm

        Returns the goal node if the goal state is reached, other wise returns None.

        Runs for TIME_LIMIT_IN_SECONDS seconds before returning None.
        """
        start = time.time()

        if self.goal_test(self.init_state):
            print(f'The length of reached for this solution is: {len(reached)}')
            return self.init_node
        
        frontier = deque()
        frontier.append(self.init_node)

        reached = [self.init_state]

        while frontier:
            node = frontier.popleft()
            #print(f'The path cost for this solution is: {node.path_cost}')
            
            for child in self.expand(node):
                s = child.state
                if self.goal_test(s):
                        print(f'The length of reached for this solution is: {len(reached)}')
                        return child
                if s not in reached:
                    reached.append(s)
                    frontier.append(child)

            end = time.time()
            if end - start > TIME_LIMIT_IN_SECONDS:
                print("Time limit reached")
                return None        
            # if node.path_cost > 31:
            #     print("Path cost limit reached")
            #     print(len(reached))
            #     return None
        return None