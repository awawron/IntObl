import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from ann_visualizer.visualize import ann_viz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open('diabetes2.csv') as f:
    lines = (line for line in f if not line.startswith('#'))
    dataset = np.loadtxt(lines, delimiter=',', skiprows=1)

X =dataset[:,0:8]
y = dataset[:,8]

model = Sequential()
model.add(Dense(6, input_dim=8, activation='relu'))
model.add(Dense(3, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X, y, epochs=90, validation_split=0.3)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train', 'test'], loc="upper left")
plt.show()

from ann_visualizer.visualize import ann_viz;

ann_viz(model, view=True, filename='network.gv', title="My graph")