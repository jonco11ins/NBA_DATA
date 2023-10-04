import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

data = pd.read_csv('/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv')
# Drop the columns you want to ignore
data.drop(columns=['min','team_name','team_nickname','team_code', 'plusMinus', 'points',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers','longestRun'], inplace=True)
#data.drop(columns=['min', 'plusMinus', 'points','team_name','team_nickname','team_code','team_id'], inplace=True)

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
#                 feature  importance
# 0                    fgm    0.158908
# 10                defReb    0.136269
# 8                    tpp    0.091953
# 17  turnovers_from_shots    0.071004
# 2                    fgp    0.060545
# 11                totReb    0.054743
# 5                    ftp    0.049421
# 3                    ftm    0.045501
# 14                steals    0.042963
# 15             turnovers    0.042450
# 4                    fta    0.037572
# 18     turnovers_from_3s    0.032155
# 7                    tpa    0.031885
# 1                    fga    0.028609
# 16                blocks    0.028257
# 6                    tpm    0.025795
# 13                pFouls    0.025421
# 9                 offReb    0.018907
# 12               assists    0.017643
# Accuracy: 70.04%