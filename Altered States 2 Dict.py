import random
import string

# Function to generate a 5x5 matrix with random letters from A-Z, excluding 'Q'
def generate_letter_matrix(size=5):
    letters = [letter for letter in string.ascii_uppercase if letter != 'Q']
    return [[random.choice(letters) for _ in range(size)] for _ in range(size)]

# Function to print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

# Check if position is valid within the matrix
def is_valid_position(x, y, size):
    return 0 <= x < size and 0 <= y < size

# DFS to explore paths using King's moves and check for valid state names
def explore_from_cell(matrix, x, y, state_population):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    found_states = set()
    size = len(matrix)
    
    def dfs(cx, cy, path):
        word = ''.join(path)
        if word in state_population:
            found_states.add(word)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid_position(nx, ny, size):
                path.append(matrix[nx][ny])
                dfs(nx, ny, path)
                path.pop()

    dfs(x, y, [matrix[x][y]])
    return found_states

# Dictionary with state names and populations
state_population = {
    "California": 39538223,
    "Texas": 29145505,
    "Florida": 21538187,
    "New York": 20201249,
    "Pennsylvania": 13002700,
    "Illinois": 12812508,
    "Ohio": 11799448,
    "Georgia": 10711908,
    "North Carolina": 10439388,
    "Michigan": 10077331,
    "New Jersey": 9288994,
    "Virginia": 8631393,
    "Washington": 7705281,
    "Arizona": 7151502,
    "Massachusetts": 7029917,
    "Tennessee": 6910840,
    "Indiana": 6785528,
    "Maryland": 6177224,
    "Missouri": 6154913,
    "Wisconsin": 5893718,
    "Colorado": 5773714,
    "Minnesota": 5706494,
    "South Carolina": 5118425,
    "Alabama": 5024279,
    "Louisiana": 4657757,
    "Kentucky": 4505836,
    "Oregon": 4237256,
    "Oklahoma": 3959353,
    "Connecticut": 3605944,
    "Utah": 3271616,
    "Iowa": 3190369,
    "Nevada": 3104614,
    "Arkansas": 3011524,
    "Mississippi": 2961279,
    "Kansas": 2937880,
    "New Mexico": 2117522,
    "Nebraska": 1961504,
    "Idaho": 1839106,
    "West Virginia": 1793716,
    "Hawaii": 1455271,
    "New Hampshire": 1377529,
    "Maine": 1362359,
    "Rhode Island": 1097379,
    "Montana": 1084225,
    "Delaware": 989948,
    "South Dakota": 886667,
    "North Dakota": 779094,
    "Alaska": 733391,
    "Vermont": 643077,
    "Wyoming": 576851,
}


matrix = generate_letter_matrix()
print("Original matrix:")
print_matrix(matrix)

starting_x, starting_y = 0, 0
found_states = explore_from_cell(matrix, starting_x, starting_y, state_population)
print("\nFound state names from (0,0):")
for state in found_states:
    print(f"{state}: {state_population[state]}")

