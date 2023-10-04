import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

#outcome is binary
# Load data
file_path = '/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv'
data = pd.read_csv(file_path)
data.drop(columns=['min','team_name','team_nickname','team_code', 'plusMinus', # 'points',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers','longestRun'], inplace=True)
data.dropna(inplace=True)

# Split data into train and test sets
X = data.drop('outcome', axis=1)  # Assuming 'outcome' is your target variable
y = data['outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

# Initialize the GBM Classifier
gbm_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train the GBM Classifier
gbm_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = gbm_classifier.predict(X_test)

# Calculate Accuracy and other metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Load new data from CSV
new_data_path = '/Users/jonco11ins/Documents/NBA_data/testdatagame.csv'
new_data = pd.read_csv(new_data_path)
predicted_outcomes = gbm_classifier.predict(new_data)
predicted_probabilities = gbm_classifier.predict_proba(new_data)

print(predicted_outcomes,
predicted_probabilities)

#results:
# Accuracy: 80.77%

# The test data I provided was designed by me to look like data from a team that would lose, the model predicted correctly

# Classification Report:
#                precision    recall  f1-score   support

#            0       0.80      0.82      0.81       243
#            1       0.82      0.80      0.81       251

#     accuracy                           0.81       494
#    macro avg       0.81      0.81      0.81       494
# weighted avg       0.81      0.81      0.81       494

# [0 1] [[0.7408348 0.2591652]
#  [0.1004078 0.8995922]]

# The model is quite confident (with ~74.08% probability) that the first sample belongs to class 0 (a loss).
# The model is even more confident (with ~89.96% probability) that the second sample belongs to class 1 (a win).
