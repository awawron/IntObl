import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("iris.csv")

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

label_encoder = LabelEncoder()
all_classes = label_encoder.fit_transform(all_classes)

(train_set, test_set, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

clf = MLPClassifier(solver='lbfgs', 
                    alpha=1,
                    hidden_layer_sizes=(3, 3), 
                    random_state=1)

clf.fit(train_set, train_classes)     
clf.score(train_set, train_classes)

predictions_train = clf.predict(train_set)
predictions_test = clf.predict(test_set)
train_score = accuracy_score(predictions_train, train_classes)
print("score on train data: ", train_score)
test_score = accuracy_score(predictions_test, test_classes)
print("score on test data: ", test_score)
# print(predictions_train[:20])


