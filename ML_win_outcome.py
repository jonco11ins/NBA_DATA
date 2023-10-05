import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

data = pd.read_csv('/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv')
# Drop the columns you want to ignore
data.drop(columns=['min','team_name','team_nickname','team_code', 'plusMinus', 'points',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers',
'longestRun','turnovers_from_3s','turnovers_from_shots'], inplace=True)
data.dropna(inplace=True)

# Separate the features and the target
X = data.drop(columns='outcome')
y = data['outcome']

#we will change randon state another time
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=101)


clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

importances = clf.feature_importances_
features = X.columns
feature_importances = pd.DataFrame({'feature': features, 'importance': importances})
print(feature_importances.sort_values(by='importance', ascending=False))

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# results:
#       feature  importance
# 0         fgm    0.171212
# 10     defReb    0.152825
# 8         tpp    0.112623
# 1         fga    0.060604
# 2         fgp    0.058229
# 3         ftm    0.052569
# 15  turnovers    0.051816
# 4         fta    0.046795
# 14     steals    0.045902
# 13     pFouls    0.036223
# 12    assists    0.036104
# 6         tpm    0.035126
# 11     totReb    0.034224
# 5         ftp    0.030714
# 16     blocks    0.028928
# 9      offReb    0.023075
# 7         tpa    0.023030
# Accuracy: 69.03%
