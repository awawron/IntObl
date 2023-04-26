import pandas as pd
from sklearn import preprocessing

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/SkillCraft.csv')
df_dirty_length = len(df)

# Drop any rows with missing values
df.dropna(inplace=True)

# Drop any rows with incorrect data types or values that do not make sense
df = df[(df['LeagueIndex'] >= 1) & (df['LeagueIndex'] <= 8) &
        (df['Age'] >= 0) & (df['HoursPerWeek'] >= 0) & (df['TotalHours'] >= 0) &
        (df['APM'] >= 0) & (df['SelectByHotkeys'] >= 0) & (df['AssignToHotkeys'] >= 0) &
        (df['UniqueHotkeys'] >= 0) & (df['MinimapAttacks'] >= 0) & (df['MinimapRightClicks'] >= 0) &
        (df['NumberOfPACs'] >= 0) & (df['GapBetweenPACs'] >= 0) & (df['ActionLatency'] >= 0) &
        (df['ActionsInPAC'] >= 0) & (df['TotalMapExplored'] >= 0) & (df['WorkersMade'] >= 0) &
        (df['UniqueUnitsMade'] >= 0) & (df['ComplexUnitsMade'] >= 0) &
        (df['ComplexAbilitiesUsed'] >= 0)]

cols_to_filter = df.columns[2:]

# # Calculate the IQR for each column
# Q1 = df.quantile(0.25)
# Q3 = df.quantile(0.75)
# IQR = Q3 - Q1

# # Set a threshold for outlier removal (e.g., 1.5*IQR)
# threshold = 10

# # Remove any rows with a value outside the range [Q1 - threshold*IQR, Q3 + threshold*IQR]
# df = df[~((df[cols_to_filter] < (Q1 - threshold*IQR)) | (df[cols_to_filter] > (Q3 + threshold*IQR))).any(axis=1)]

scaler = preprocessing.StandardScaler().fit(df[cols_to_filter])
train_set = scaler.transform(df[cols_to_filter])

# Save the cleaned data to a new CSV file
df.to_csv('data/SkillCraft_clean.csv', index=False)

df_clean = pd.read_csv('data/SkillCraft_clean.csv')

print(df_dirty_length)
print(len(df_clean))

