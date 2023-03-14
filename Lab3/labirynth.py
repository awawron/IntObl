import pygad

NONE = -1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WALL = 4
PATH = 5
STRT = 6
EXIT = 7

labyrinth = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, STRT, PATH, PATH, WALL, PATH, PATH, PATH, WALL, PATH, PATH, WALL],
    [WALL, WALL, WALL, PATH, PATH, PATH, WALL, PATH, WALL, WALL, PATH, WALL],
    [WALL, PATH, PATH, PATH, WALL, PATH, WALL, PATH, PATH, PATH, PATH, WALL],
    [WALL, PATH, WALL, PATH, WALL, WALL, PATH, PATH, WALL, WALL, PATH, WALL],
    [WALL, PATH, PATH, WALL, WALL, PATH, PATH, PATH, WALL, PATH, PATH, WALL],
    [WALL, PATH, PATH, PATH, PATH, PATH, WALL, PATH, PATH, PATH, WALL, WALL],
    [WALL, PATH, WALL, PATH, PATH, WALL, WALL, PATH, WALL, PATH, PATH, WALL],
    [WALL, PATH, WALL, WALL, WALL, PATH, PATH, PATH, WALL, WALL, PATH, WALL],
    [WALL, PATH, WALL, PATH, WALL, WALL, PATH, WALL, PATH, WALL, PATH, WALL],
    [WALL, PATH, WALL, PATH, PATH, PATH, PATH, PATH, PATH, PATH, EXIT, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]
max_steps = 30

gene_space = [-1, 0, 1, 2, 3]


def find_start_end(labyrinth):
    re = {'start': None, 'end': None}
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == STRT:
                re["start"] = [i, j]
            if labyrinth[i][j] == EXIT:
                re["end"] = [i, j]
            if re["end"] != None and re["start"] != None:
                return re


def check_move(pos, move, nextmove=None):
    if move == NONE:
        return {"new_position": pos, "fitness_change": -1}

    fitness_change = 0

    if move == UP:
        newpos = [pos[0] - 1, pos[1]]
        # if nextmove != None and nextmove == DOWN:
        #     fitness_change -= 5
    elif move == RIGHT:
        newpos = [pos[0], pos[1] + 1]
        # if nextmove != None and nextmove == LEFT:
        #     fitness_change -= 5
    elif move == DOWN:
        newpos = [pos[0] + 1, pos[1]]
        # if nextmove != None and nextmove == UP:
        #     fitness_change -= 5
    elif move == LEFT:
        newpos = [pos[0], pos[1] - 1]
        # if nextmove != None and nextmove == RIGHT:
        #     fitness_change -= 5

    if labyrinth[newpos[0]][newpos[1]] == WALL:
        fitness_change -= 10
        return {"new_position": pos, "fitness_change": fitness_change}
    else:
        return {"new_position": newpos, "fitness_change": fitness_change}


def fitness_func(solution, solution_idx):
    tmp = find_start_end(labyrinth)
    pos = tmp["start"]
    end = tmp["end"]
    ended = False

    fitness = 0

    # For the purpose of checking the next move the last move is made outside the loop
    for i in range(len(solution) - 1):
        if ended == False and solution[i] == NONE:
            fitness -= 2
        elif ended == True and solution[i] != NONE:
            fitness -= 2
        else:
            fitness += 1
        if pos == end:
            ended = True
        move = check_move(pos, solution[i], solution[i + 1])
        pos = move["new_position"]
        fitness += move["fitness_change"]

        distance = abs(pos[0] - end[0]) + abs(pos[1] - end[1])
        fitness -= distance

    last = len(solution) - 1

    if ended == True and solution[last] != NONE:
        fitness -= 1
    elif ended == True and solution[last] != NONE:
        fitness -= 1
    else:
        fitness += 1
    move = check_move(pos, solution[last])
    pos = move["new_position"]
    fitness += move["fitness_change"]

    distance = abs(pos[0] - end[0]) + abs(pos[1] - end[1])
    fitness -= distance

    return fitness


# variables
fitness_function = fitness_func

sol_per_pop = 20
num_genes = max_steps

num_parents_mating = 10
num_generations = 1000
keep_parents = 10

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 4

# init
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

# running the algorithm
ga_instance.run()

# summary
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(
    solution_fitness=solution_fitness))

# chart
ga_instance.plot_fitness()
