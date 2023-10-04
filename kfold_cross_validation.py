import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

data = pd.read_csv('/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv')
data.drop(columns=['min','team_name','team_nickname','team_code', 'plusMinus', 'points',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers','longestRun'], inplace=True)
X = data.drop('outcome', axis=1)
y = data['outcome']

gbm_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Perform 5-fold cross validation (common choice)
scores = cross_val_score(gbm_classifier, X, y, cv=5, scoring='accuracy')

print(f"Accuracy: {np.mean(scores) * 100:.2f}% (+/- {np.std(scores) * 100:.2f}%)")

#result: 80.97% (+/- 0.81%)