import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_set, test_set, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

# print(train_set)
# print(test_set)
# print(train_classes)
# print(test_classes)

dtc = DecisionTreeClassifier()
dtc.fit(train_set, train_classes)

extree = tree.export_text(dtc)
print(extree)
plotree = tree.plot_tree(dtc)

pred = dtc.predict(test_set)
confmtx = confusion_matrix(test_classes, pred)
plot = ConfusionMatrixDisplay(confusion_matrix=confmtx, display_labels=["setosa", "virginica", "verticolor"])

plot.plot()
plt.show()

print(dtc.score(test_set, test_classes))

