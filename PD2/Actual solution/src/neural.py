import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("data/SkillCraft.csv")\

all_inputs = df[['Age', 'HoursPerWeek', 'TotalHours', 'APM', 'SelectByHotkeys', 'UniqueHotkeys', 'MinimapAttacks', 'NumberOfPACs', 'GapBetweenPACs', 'ActionLatency', 'ActionsInPAC', 'TotalMapExplored', 'WorkersMade', 'UniqueUnitsMade', 'ComplexUnitsMade', 'ComplexAbilitiesUsed']].values
all_classes = df['LeagueIndex'].values

label_encoder = LabelEncoder()
all_classes = label_encoder.fit_transform(all_classes)

(train_set, test_set, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=2)

scaler = preprocessing.StandardScaler().fit(train_set)
train_set = scaler.transform(train_set)
test_set = scaler.transform(test_set)

clf = MLPClassifier(activation='relu',
                    alpha=0.0001,
                    max_iter=1500,
                    hidden_layer_sizes=(16, 8, 4), 
                    random_state=1)

clf.fit(train_set, train_classes)     
clf.score(train_set, train_classes)

predictions_train = clf.predict(train_set)
predictions_test = clf.predict(test_set)
train_score = accuracy_score(predictions_train, train_classes)
print("score on train data: ", train_score)
test_score = accuracy_score(predictions_test, test_classes)
print("score on test data: ", test_score)
# print(predictions_train)

confmtx = confusion_matrix(test_classes, predictions_test)
plot = ConfusionMatrixDisplay(confusion_matrix = confmtx)
plot.plot()
plt.show()