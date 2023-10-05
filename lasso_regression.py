import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import warnings

# Suppress specific warning
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
warnings.filterwarnings("ignore", message="X has feature names, but LassoCV was fitted without feature names")

# Load data
file_path = '/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv'
data = pd.read_csv(file_path)
data.drop(columns=['min','team_name','team_nickname','team_code', 'plusMinus', # 'points',
'team_id','fastBreakPoints','pointsInPaint','biggestLead','secondChancePoints','pointsOffTurnovers','longestRun','turnovers_from_3s','turnovers_from_shots'], inplace=True)
data.dropna(inplace=True)

X = data.drop('outcome', axis=1)
y = data['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# The LassoCV model automatically selects the best alpha using cross-validation.
lasso = LassoCV(max_iter=30000,cv=5).fit(X_train_scaled, y_train)

y_pred_train = lasso.predict(X_train_scaled)
y_pred_test = lasso.predict(X_test_scaled)

mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)

print(f"Training MSE: {mse_train:.4f}")
print(f"Test MSE: {mse_test:.4f}")

importance = pd.DataFrame({'feature': X.columns, 'coef': lasso.coef_})
print(importance.sort_values(by='coef', ascending=False))

----------

result = permutation_importance(lasso, X_test, y_test, n_repeats=30, random_state=0)

# Get importances and their standard deviations
importances = result.importances_mean
std = result.importances_std

# Sort importances
sorted_idx = importances.argsort()

# Training MSE: 0.1282
# Test MSE: 0.1339
#       feature      coef
# 12     totReb  0.242054
# 15     steals  0.129909
# 0      points  0.126827
# 1         fgm  0.111258
# 7         tpm  0.054281
# 17     blocks  0.044351
# 6         ftp  0.038533
# 9         tpp  0.022011
# 11     defReb  0.018504
# 13    assists  0.001599
# 8         tpa  0.000000
# 4         ftm -0.000000
# 10     offReb  0.000000
# 14     pFouls -0.015213
# 3         fgp -0.032929
# 5         fta -0.037032
# 16  turnovers -0.134018
# 2         fga -0.251717

----------

# # Plot
# plt.figure(figsize=(10, X_test.shape[1]))
# plt.boxplot(result.importances[sorted_idx].T, vert=False)
# plt.yticks(range(X_test.shape[1]), X_test.columns[sorted_idx])
# plt.xlabel("Permutation Importance")
# plt.show()
