import pandas
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats


def std(arr):
    re = []
    for item in arr:
        re.append((item - stats.mean(arr)) / np.std(arr, ddof=1))
    return re


def norm(arr):
    re = []
    max_value = max(arr)
    min_value = min(arr)
    for item in arr:
        re.append((item - min_value) / (max_value - min_value))
    return re


def plot_cities(y, data1, data2, data3):
    plt.cla()

    plt.title('Ludnosc w miastach Polski')
    plt.xlabel('Lata')
    plt.ylabel('Liczba ludnosci [w tys.]')

    plt.plot(y, data1, color='r', marker='o')
    plt.plot(y, data2, color='g', marker='o')
    plt.plot(y, data3, color='b', marker='o')

    plt.legend(['Gdansk', 'Poznan', 'Szczecin'])

    plt.show()


path = "D:\\Studia\\UG\\Sem4\\IntObl\\Lab1\\miasta.csv"

miasta = pandas.read_csv(path)

data = {
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]}
df = pandas.DataFrame(data, index=[10])

new_miasta = pandas.concat([miasta, df])

years = new_miasta.Rok
gdansk_data = new_miasta.Gdansk
poznan_data = new_miasta.Poznan
szczecin_data = new_miasta.Szczecin

plot_cities(years, gdansk_data, poznan_data, szczecin_data)

std_gdansk_data = std(gdansk_data)
std_poznan_data = std(poznan_data)
std_szczecin_data = std(szczecin_data)

plot_cities(years, std_gdansk_data, std_poznan_data, std_szczecin_data)

norm_gdansk_data = norm(gdansk_data)
norm_poznan_data = norm(poznan_data)
norm_szczecin_data = norm(szczecin_data)

plot_cities(years, norm_gdansk_data, norm_poznan_data, norm_szczecin_data)
