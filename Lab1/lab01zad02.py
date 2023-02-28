import pandas
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats


def std(arr):
    re = []
    for item in arr:
        re.append((item - mean(arr)) / np.std(arr, ddof=1))
    return re


def norm(arr):
    re = []
    max_value = max(arr)
    min_value = min(arr)
    for item in arr:
        re.append((item - min_value) / (max_value - min_value))
    return re


path = "D:\\Studia\\UG\\Sem4\\IntObl\\Lab1\\miasta.csv"

miasta = pandas.read_csv(path)
print(miasta)

data = {
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]}
df = pandas.DataFrame(data, index=[10])

new_miasta = pandas.concat([miasta, df])

print(new_miasta)

years = new_miasta.Rok
gdansk_data = new_miasta.Gdansk
poznan_data = new_miasta.Poznan
szczecin_data = new_miasta.Szczecin

plt.title('Ludnosc w miastach Polski')
plt.xlabel('Lata')
plt.ylabel('Liczba ludnosci [w tys.]')

plt.plot(years, gdansk_data, color='r', marker='o')
plt.plot(years, poznan_data, color='g', marker='o')
plt.plot(years, szczecin_data, color='b', marker='o')

plt.legend(['Gdansk', 'Poznan', 'Szczecin'])

plt.show()

std_gdansk_data = std(gdansk_data)
std_poznan_data = std(poznan_data)
std_szczecin_data = std(szczecin_data)

print(stats.mean(std_gdansk_data))
print(stats.stdev(std_gdansk_data))
# print(gdansk_data)
print(std_gdansk_data)

norm_gdansk_data = norm(gdansk_data)
norm_poznan_data = norm(poznan_data)
norm_szczecin_data = norm(szczecin_data)

print(norm_gdansk_data)

plt.cla()

plt.plot(years, std_gdansk_data, color='r', marker='o')
plt.plot(years, std_poznan_data, color='g', marker='o')
plt.plot(years, std_szczecin_data, color='b', marker='o')

plt.legend(['Gdansk', 'Poznan', 'Szczecin'])

plt.show()

plt.cla()

plt.plot(years, norm_gdansk_data, color='r', marker='o')
plt.plot(years, norm_poznan_data, color='g', marker='o')
plt.plot(years, norm_szczecin_data, color='b', marker='o')

plt.legend(['Gdansk', 'Poznan', 'Szczecin'])

plt.show()
