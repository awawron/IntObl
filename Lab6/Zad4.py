import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from ann_visualizer.visualize import ann_viz;
from sklearn import preprocessing
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open('diabetes2.csv') as f:
    lines = (line for line in f if not line.startswith('#'))
    dataset = np.loadtxt(lines, delimiter=',', skiprows=1)

x =dataset[:,0:8]
y = dataset[:,8]
scaler = preprocessing.StandardScaler().fit(x)
better_x = scaler.transform(x)

def makeModel(x, y, activation, optimizer):
    model = Sequential()
    model.add(Dense(6, input_dim=8, activation=activation))
    model.add(Dense(3, activation=activation))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    history = model.fit(better_x, y, epochs=90, validation_split=0.3)

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend(['train', 'test'], loc="upper left")
    plt.show()

    ann_viz(model, view=True, filename='network.gv', title="My graph")

makeModel(better_x, y, 'relu', 'adam')
makeModel(better_x, y, 'relu', 'sgd')
makeModel(better_x, y, 'sigmoid', 'nadam')
makeModel(better_x, y, 'sigmoid', 'sgd')
