import pygad
import math

# autopep8: off
#region ---------- INPUTS ----------
# autopep8: on
# 2 stations 3 jobs
import random
input_s1 = [
    [(1, 3)],
    [(0, 1)],
    [(0, 2)]
]
# all solutions are correct for s1

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
    [(0, 2), (1, 9), (2, 14)],
    [(5, 3), (6, 7), (7, 8)],
    [(0, 9), (3, 13), (4, 10)],
    [(1, 6), (5, 5), (6, 6)],
    [(1, 19), (5, 17), (6, 14)],
    [(4, 8), (5, 6), (7, 12)],
    [(1, 11), (4, 10), (5, 12)],
    [(3, 3), (4, 10), (7, 4)],
    [(0, 17), (1, 1), (2, 3)],
    [(3, 13), (5, 2), (6, 1)],
    [(2, 8), (4, 16), (5, 1)],
    [(2, 10), (5, 15), (6, 2)]
]

input_l2 = [
    [(0, 5), (1, 3), (2, 14), (3, 9), (4, 12), (5, 8), (6, 20), (7, 17)],
    [(0, 13), (1, 2), (2, 7), (3, 11), (4, 16), (5, 20), (6, 18), (7, 5)],
    [(0, 10), (1, 1), (2, 8), (3, 12), (4, 4), (5, 19), (6, 6), (7, 16)],
    [(0, 19), (1, 6), (2, 15), (3, 18), (4, 11), (5, 1), (6, 10), (7, 7)],
    [(0, 7), (1, 19), (2, 3), (3, 13), (4, 2), (5, 14), (6, 16), (7, 8)],
    [(0, 12), (1, 8), (2, 17), (3, 5), (4, 1), (5, 6), (6, 13), (7, 19)],
    [(0, 16), (1, 7), (2, 20), (3, 4), (4, 8), (5, 5), (6, 1), (7, 3)],
    [(0, 4), (1, 15), (2, 19), (3, 1), (4, 20), (5, 13), (6, 7), (7, 14)],
    [(0, 9), (1, 10), (2, 12), (3, 17), (4, 6), (5, 18), (6, 14), (7, 2)],
    [(0, 11), (1, 14), (2, 1), (3, 20), (4, 3), (5, 7), (6, 15), (7, 10)],
    [(0, 2), (1, 16), (2, 5), (3, 6), (4, 13), (5, 4), (6, 11), (7, 12)],
    [(0, 18), (1, 11), (2, 13), (3, 7), (4, 19), (5, 3), (6, 2), (7, 15)]
]

input_l3 = [
    [(0, 18), (1, 7), (2, 1), (3, 16), (4, 7), (5, 12), (6, 9), (7, 14)],
    [(3, 10), (5, 3), (6, 16)],
    [(0, 9), (1, 1), (2, 16), (3, 7), (4, 20), (5, 9), (6, 13), (7, 7)],
    [(0, 4), (5, 5), (6, 5), (7, 5)],
    [(0, 11), (1, 10), (2, 11), (3, 13), (4, 3), (5, 2), (6, 8)],
    [(4, 16), (6, 11), (7, 17)],
    [(0, 2), (1, 8), (2, 4), (3, 1), (4, 20), (5, 5), (6, 5), (7, 6)],
    [(0, 7), (5, 2)],
    [(0, 20), (1, 19), (2, 1), (7, 2)],
    [(0, 9), (1, 20), (2, 7), (3, 17), (4, 10), (5, 14), (6, 12), (7, 13)],
    [(0, 5), (1, 14), (2, 3), (3, 12), (4, 1), (5, 7), (6, 18), (7, 3)],
    [(2, 3), (3, 8), (4, 9), (5, 20), (6, 2), (7, 5)]
]
# autopep8: off
#endregion
# autopep8: on

CHOSEN_INPUT = input_l3
MACHINE_COUNT = int(len(CHOSEN_INPUT) - len(CHOSEN_INPUT) / 3)

print(MACHINE_COUNT)

job_count = 0
for i in CHOSEN_INPUT:
    job_count += len(i)

processed_input = []

for i in range(len(CHOSEN_INPUT)):
    for j in range(len(CHOSEN_INPUT[i])):
        processed_input.append(
            (i, CHOSEN_INPUT[i][j][0], CHOSEN_INPUT[i][j][1]))


def process_output(output):
    machines = [[] for i in range(MACHINE_COUNT)]
    deducted_for_idle = 0

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
            deducted_for_idle += fill_amount
            for j in range(fill_amount):
                machine.append('N')

        for j in range(time):
            machine.append(job_number)

    return (deducted_for_idle, machines)


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

    (deducted, machines) = process_output(solution)
    # machines = [[] for i in range(MACHINE_COUNT)]

    # for i in solution:
    #     better_i = int(i)
    #     job_number = str(processed_input[better_i][0])
    #     machine_number = processed_input[better_i][1]
    #     machine = machines[machine_number]
    #     time = processed_input[better_i][2]

    #     # make sure there is no overlap
    #     for k in range(MACHINE_COUNT):
    #         fill_amount = 0
    #         if k == machine_number:
    #             pass
    #         elif len(machines[k]) > len(machine):
    #             idx = len(machine)
    #             for j in range(time):
    #                 if len(machines[k]) > idx + j and machines[k][idx + j] == job_number:
    #                     fill_amount = j + 1

    #         # deduct fitness for idle time
    #         fitness -= fill_amount
    #         for j in range(fill_amount):
    #             machine.append('N')

    #     for j in range(time):
    #         machine.append(job_number)

    # deduct fitness for idle time
    fitness -= deducted
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
print("Machine and job visualization:")
solution_vis = process_output(solution)[1]
for i in solution_vis:
    print(i)

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
