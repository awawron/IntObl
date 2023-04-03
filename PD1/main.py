import pygad
import math


#region ---------- INPUTS ----------
# 2 stations 3 jobs
input_s1 = [
    [(1, 3)],
    [(0, 1)], 
    [(0, 2)]
]
input_s2 = [
    [(0, 2), (1, 2)], 
    [(0, 2), (1, 2)], 
    [(0, 3), (1, 3)]
]
input_s3 = [
    [(0, 2), (1, 3)], 
    [(0, 6)], 
    [(0, 3), (1, 6)]
]

# 4 stations 6 jobs
input_m1 = [
    [(0, 5), (3, 2)],
    [(1, 3), (2, 3)],
    [(2, 7), (3, 10)],
    [(1, 10), (2, 5)],
    [(1, 2), (0, 1)],
    [(3, 10), (0, 1)]
]
input_m2 = [
    [(0, 17), (1, 2), (2, 1), (3, 3)],
    [(0, 11), (1, 7), (2, 5), (3, 5)],
    [(0, 19), (1, 20), (2, 10), (3, 9)],
    [(0, 15), (1, 1), (2, 3), (3, 8)],
    [(0, 14), (1, 7), (2, 7), (3, 7)],
    [(0, 13), (1, 1), (2, 2), (3, 5)]
]
input_m3 = [
    [(1, 5), (2, 10), (3, 12)],
    [(0, 1), (3, 10)],
    [(0, 4), (1, 9), (2, 4), (3, 1)],
    [(0, 7), (1, 1), (2, 9), (3, 2)],
    [(0, 3)],
    [(0, 3), (1, 1), (3, 10)]
]

# 8 stations 12 jobs
input_l1 = [
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()],
    [(), (), ()]
]
input_l2 = [
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)]
]
input_l3 = [
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(), (), ()],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(), (), (), (), ],
    [(), (), (), (), (), (), ()],
    [(), (), ()],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(), ()],
    [(), (), (), ()],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(0), (1), (2), (3), (4), (5), (6), (7)],
    [(), (), (), (), (), ()]
]
#endregion

CHOSEN_INPUT = input_s3
MACHINE_COUNT = int(len(CHOSEN_INPUT) - len(CHOSEN_INPUT) / 3)

print(MACHINE_COUNT)

job_count = 0
for i in CHOSEN_INPUT:
    job_count += len(i)

processed_input = []

for i in range(len(CHOSEN_INPUT)):
    for j in range(len(CHOSEN_INPUT[i])):
        processed_input.append((i, CHOSEN_INPUT[i][j][0], CHOSEN_INPUT[i][j][1]))

def process_output(output):
    machines = [[] for i in MACHINE_COUNT]

    for i in output:
        better_i = int(i)
        job_number = str(processed_input[better_i][0])
        machine_number = processed_input[better_i][1]
        machine = machines[machine_number]
        time = processed_input[better_i][2]

        for k in range(MACHINE_COUNT):
                fill_amount = 0
                if k == machine_number:
                    pass
                elif len(machines[k]) > len(machine):
                    idx = len(machine)
                    for j in range(time):
                        if len(machines[k]) > idx + j and machines[k][idx + j] == job_number:
                            fill_amount = j + 1

                # deduct fitness for idle time
                for j in range(fill_amount):
                    machine.append('N')

gene_space = range(job_count)

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 25
num_genes = job_count

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 10
num_generations = 100
keep_parents = 5

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 20

def fitness_func(solution, solution_idx):
    fitness = 0
    machines = [[] for i in range(MACHINE_COUNT)]

    for i in solution:
        better_i = int(i)
        job_number = str(processed_input[better_i][0])
        machine_number = processed_input[better_i][1]
        machine = machines[machine_number]
        time = processed_input[better_i][2]
        
        # make sure there is no overlap
        for k in range(MACHINE_COUNT):
            fill_amount = 0
            if k == machine_number:
                pass
            elif len(machines[k]) > len(machine):
                idx = len(machine)
                for j in range(time):
                    if len(machines[k]) > idx + j and machines[k][idx + j] == job_number:
                        fill_amount = j + 1

            # deduct fitness for idle time
            fitness -= fill_amount
            for j in range(fill_amount):
                machine.append('N')

        for j in range(time):
            machine.append(job_number)

    # deduct a lot of fitness for the length
    fitness -= 5 * len(max(machines, key=len))
    # for i in machines:
    #     print(i)
    # print(len(max(machines, key=len)))

    print(fitness)

    return fitness

fitness_function = fitness_func

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    allow_duplicate_genes=False
)

# uruchomienie algorytmu
ga_instance.run()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(
    solution_fitness=solution_fitness))

print(best_layout)

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
