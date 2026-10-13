import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import numpy as np
from joblib import dump
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import cross_val_score



df = pd.read_csv("cleaned_crop_data.csv")
df_encoded = pd.get_dummies(df, columns=['Crop', 'Season', 'State'])

# X = df_encoded.drop(columns=['Crop_Year','Production','Yield'])  # Replace with your target column
# y = df_encoded['Yield']


# X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


# model = XGBRegressor(
#     n_estimators=200,
#     learning_rate=0.05,
#     max_depth=4,
#     subsample=0.8,
#     colsample_bytree=0.7,
#     gamma=1,
#     reg_alpha=0.5,
#     reg_lambda=1,
#     early_stopping_rounds=10,
#     random_state=42
# )

# model.fit(
#     X_train, y_train,
#     eval_set=[(X_val, y_val)],
#     verbose=True
# )

# y_pred = model.predict(X_val)
# print("RMSE:", np.sqrt(mean_squared_error(y_val, y_pred)))
# print("R² Score:", r2_score(y_val, y_pred))

# dump(model, "pred_model.pkl")




# Define RMSE scorer
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

rmse_scorer = make_scorer(rmse, greater_is_better=False)

# Define parameter grid for tuning
param_grid = {
    'max_depth': [3, 4, 5],
    'min_child_weight': [1, 3, 5],
    'gamma': [0, 0.5, 1],
    'subsample': [0.7, 0.8],
    'colsample_bytree': [0.6, 0.8],
    'learning_rate': [0.05, 0.1],
    'n_estimators': [100, 200]
}

# Initialize model
xgb_model = XGBRegressor(
    objective='reg:squarederror',
    random_state=42
)

# Set up K-Fold cross-validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Grid search with cross-validation
grid_search = GridSearchCV(
    estimator=xgb_model,
    param_grid=param_grid,
    scoring=rmse_scorer,
    cv=cv,
    verbose=1,
    n_jobs=-1
)

X = df_encoded.drop(columns=['Crop_Year','Production','Yield'])  
y = df_encoded['Yield']

# Fit model
grid_search.fit(X, y)

# Best model and parameters
best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)
print("Best RMSE:", -grid_search.best_score_)
r2_scores = cross_val_score(best_model, X, y, cv=5, scoring='r2')
print("Cross-validated R² scores:", r2_scores)
print("Mean R² score:", r2_scores.mean())


dump(best_model, "2pred_model.pkl")