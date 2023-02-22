import pandas
import matplotlib.pyplot as plt

path = '/home/LABPK/awawron/IntObl/IntObl/Lab1/miasta.csv'

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

