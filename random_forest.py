import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # or RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error       # or accuracy_score for classification
from sklearn.preprocessing import LabelEncoder

# Load the data
data = pd.read_csv('/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv')
data.drop(columns=['min', 'plusMinus', 'points','team_name','team_nickname','team_code',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers','longestRun'], inplace=True)
data.dropna(inplace=True)
# Preprocessing (this is a basic example; you might need more preprocessing steps)
# Encoding categorical variables if any
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Assume 'Outcome' is your target variable
X = data.drop('outcome', axis=1)
y = data['outcome']

# Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=50)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)  # or RandomForestClassifier
model.fit(X_train, y_train)

# Predict on test set
predictions = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
