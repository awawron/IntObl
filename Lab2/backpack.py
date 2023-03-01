import pygad
import numpy
import time

items = [
    {"name": "zegar", "value": 100, "weight": 7}, 
    {"name": "obraz-pejzaz", "value": 300, "weight": 7}, 
    {"name": "obraz-portrt", "value": 200, "weight": 6}, 
    {"name": "radio", "value": 40, "weight": 2}, 
    {"name": "laptop", "value": 500, "weight": 5}, 
    {"name": "lampka nocna", "value": 70, "weight": 6}, 
    {"name": "srebrne sztucce", "value": 100, "weight": 1}, 
    {"name": "porcelana", "value": 250, "weight": 3}, 
    {"name": "figura z brazu", "value": 300, "weight": 10}, 
    {"name": "skorzana torebka", "value": 280, "weight": 3}, 
    {"name": "odkurzacz", "value": 300, "weight": 15}, 
]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness
# after testing it turned out that omitting weight (aside from going over max weight) in the fitness function gives better results
def fitness_func(solution, solution_idx):
    # check how much value we get and how much weight we used
    value = 0
    weight = 0
    for i in range(len(items)):
        if solution[i] == 1:
            value += items[i]["value"]
            weight += items[i]["weight"]

    # if we go over the max weight we return 0 points
    if weight > 25:
        return 0

    #normally return the value (more important) and deduce points for unused weight (less important)
    # fitness = value - (25 - weight)
    fitness = value
    print(fitness)

    return fitness

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(items)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 50
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

start_time = time.time()

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
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

end_time = time.time()
inittime = end_time - start_time
print("Initialization time: " + str(inittime))
# reset timer                       
start_time = time.time()

#uruchomienie algorytmu
ga_instance.run()

end_time = time.time()
runtime = end_time - start_time
print("Runtime: " + str(runtime))

with open("log.txt", "a") as file:
    entry = "Inittime: " + str(inittime) + " Runtime: " + str(runtime)
    file.write(entry)

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()