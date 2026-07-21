
# for data manipulation
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# for model training, tuning, and evaluation
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# for model serialization
import joblib
import os

# Define data paths, updated to be relative to the root of the cloned GitHub repository
data_dir = "data"
Xtrain_path = os.path.join(data_dir, "Xtrain.csv")
Xtest_path = os.path.join(data_dir, "Xtest.csv")
ytrain_path = os.path.join(data_dir, "ytrain.csv")
ytest_path = os.path.join(data_dir, "ytest.csv")

Xtrain = pd.read_csv(Xtrain_path)
Xtest = pd.read_csv(Xtest_path)
ytrain = pd.read_csv(ytrain_path)
ytest = pd.read_csv(ytest_path)

# All features are numerical after prep.py's LabelEncoder
# So, we will apply StandardScaler to all of them.
all_features = Xtrain.columns.tolist()

# Preprocessing pipeline (only StandardScaler for all features as categoricals are already encoded)
preprocessor = StandardScaler()

# Define XGBoost Classifier (since ProdTaken is a binary target 0/1)
xgb_model = xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')

# Define hyperparameter grid for classification
param_grid = {
    'xgbclassifier__n_estimators': [50, 100, 150],
    'xgbclassifier__max_depth': [3, 5, 7],
    'xgbclassifier__learning_rate': [0.01, 0.05, 0.1],
    'xgbclassifier__subsample': [0.6, 0.8, 1.0],
    'xgbclassifier__colsample_bytree': [0.6, 0.8, 1.0],
    'xgbclassifier__gamma': [0, 0.1, 0.2]
}

# Create pipeline
model_pipeline = make_pipeline(preprocessor, xgb_model)

# Grid search with cross-validation
grid_search = GridSearchCV(
    model_pipeline, param_grid, cv=5, scoring='roc_auc', n_jobs=-1, verbose=1
)
grid_search.fit(Xtrain, ytrain)

# Best model
best_model = grid_search.best_estimator_
print("Best Params:")
print(grid_search.best_params_)

# Predictions
y_pred_train = best_model.predict(Xtrain)
y_proba_train = best_model.predict_proba(Xtrain)[:, 1]
y_pred_test = best_model.predict(Xtest)
y_proba_test = best_model.predict_proba(Xtest)[:, 1]

# Evaluation
print("\nTraining Performance:")
print("Accuracy:", accuracy_score(ytrain, y_pred_train))
print("Precision:", precision_score(ytrain, y_pred_train))
print("Recall:", recall_score(ytrain, y_pred_train))
print("F1-Score:", f1_score(ytrain, y_pred_train))
print("ROC AUC:", roc_auc_score(ytrain, y_proba_train))

print("\nTest Performance:")
print("Accuracy:", accuracy_score(ytest, y_pred_test))
print("Precision:", precision_score(ytest, y_pred_test))
print("Recall:", recall_score(ytest, y_pred_test))
print("F1-Score:", f1_score(ytest, y_pred_test))
print("ROC AUC:", roc_auc_score(ytest, y_proba_test))

# Save best model locally
model_output_dir = "model" # Updated path
os.makedirs(model_output_dir, exist_ok=True)
model_filename = os.path.join(model_output_dir, "best_tourism_prediction_model.joblib")
joblib.dump(best_model, model_filename)
print(f"Best model saved to: {model_filename}")
