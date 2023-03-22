import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=13)
sorted_train_set = sorted(train_set, key=lambda x: x[4])
sorted_train_list = [arr.tolist() for arr in sorted_train_set]
# for i in sorted_train_list:
#     print(i)

def classify_iris(sl, sw, pl, pw):
    if sl <= 5.5 and sw > 2 and pl < 2 and pw < 1:
        return("setosa")
    elif sl >= 6 and pl >= 5 and pw < 2.5:
        return("virginica")
    else:
        return("versicolor")

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/len*100, "%")
