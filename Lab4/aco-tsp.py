import matplotlib.pyplot as plt
import random
from aco import AntColony

plt.style.use("dark_background")

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (86, 20),
    (15, 26),
    (70, 7),
    (12, 12),
    (89, 99),
    (8, 11),
    (83, 37),
)

def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

colony = AntColony(COORDS, ant_count=50, alpha=0.9, beta=1.2, 
                    pheromone_evaporation_rate=0.10, pheromone_constant=1000.0,
                    iterations=50)

# Wyniki:
# a_c=100 a=0.5 b=1.2 p_e_r=0.7 p_c=1000 i=100
# 409.5
# a_c=100 a=0.5 b=1.2 p_e_r=0.1 p_c=1000 i=100
# 403.1
# a_c=100 a=0.9 b=1.2 p_e_r=0.5 p_c=1000 i=100
# 362.6
# a_c=100 a=0.9 b=0.1 p_e_r=0.5 p_c=1000 i=100
# 401.5
# a_c=100 a=0.9 b=0.1 p_e_r=0.5 p_c=1000 i=100
# 362.7
# a_c=100 a=0.9 b=0.9 p_e_r=0.5 p_c=1000 i=100
# 408.8
# a_c=100 a=0.9 b=0.1 p_e_r=0.5 p_c=2000 i=100
# 362.6
# a_c=50 a=0.9 b=0.1 p_e_r=0.5 p_c=2000 i=50
# 394.5
# a_c=50 a=0.9 b=0.1 p_e_r=0.5 p_c=500 i=50
# 387.1
# a_c=50 a=0.9 b=0.1 p_e_r=0.5 p_c=500 i=50
# 409.5
# a_c=50 a=0.9 b=0.1 p_e_r=0.5 p_c=500 i=50
# 362.6
# a_c=20 a=0.9 b=0.1 p_e_r=0.5 p_c=500 i=50
# 405.9
# a_c=50 a=0.9 b=0.1 p_e_r=0.5 p_c=500 i=20
# 361.3
# Z moich wyników wychodzi na to, że wysokie alpha i beta,
# niska ewaporacja i duży pheromone_constant daje dość szybkie rozwiązanie

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.show()