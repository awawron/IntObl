import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from ann_visualizer.visualize import ann_viz;
from sklearn import preprocessing
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open('data/SkillCraft.csv') as f:
    lines = (line.replace('"', '') for line in f if not line.startswith('#'))
    dataset = np.loadtxt(lines, delimiter=',', skiprows=1)

x = dataset[:, 2:19]
y = dataset[:, 1]

# print(y)

def dataSwitch(item):
    if item == 1:
        return [1, 0, 0, 0, 0, 0, 0, 0]
    elif item == 2:
        return [0, 1, 0, 0, 0, 0, 0, 0]
    elif item == 3:
        return [0, 0, 1, 0, 0, 0, 0, 0]
    elif item == 4:
        return [0, 0, 0, 1, 0, 0, 0, 0]
    elif item == 5:
        return [0, 0, 0, 0, 1, 0, 0, 0]
    elif item == 6:
        return [0, 0, 0, 0, 0, 1, 0, 0]
    elif item == 7:
        return [0, 0, 0, 0, 0, 0, 1, 0]
    elif item == 8:
        return [0, 0, 0, 0, 0, 0, 0, 1]
    else:
        raise ValueError("Item must be an integer between 1 and 8.")

better_y = np.zeros((len(y), 8))

for i in range(len(y)):
    better_y[i] = (dataSwitch(y[i]))

scaler = preprocessing.StandardScaler().fit(x)
better_x = scaler.transform(x)

# for i in better_x:
#     print(i)

def makeModel(x, y, activation, optimizer):
    model = Sequential()
    model.add(Dense(16, input_dim=17, activation=activation))
    model.add(Dense(4, activation=activation))
    model.add(Dense(8, activation='softmax'))

    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    history = model.fit(x, y, epochs=100, validation_split=0.2, batch_size=8)

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend(['train', 'test'], loc="upper left")
    plt.show()

    # ann_viz(model, view=True, filename='network.gv', title="My graph")

makeModel(better_x, better_y, 'relu', 'adam')
# makeModel(better_x, better_y, 'relu', 'nadam')
# makeModel(better_x, better_y, 'relu', 'sgd')
# makeModel(better_x, better_y, 'sigmoid', 'nadam')
# makeModel(better_x, better_y, 'sigmoid', 'sgd')
# makeModel(better_x, better_y, 'sigmoid', 'adam')
