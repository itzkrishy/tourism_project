
# for data manipulation
import pandas as pd
# for creating a folder
import os
# for data preprocessing and pipeline creation
from sklearn.model_selection import train_test_split
# for converting text data in to numerical representation
from sklearn.preprocessing import LabelEncoder

# Define constants for the dataset and output paths
# When run from /content/tourism_project_local/model_building, data is at ../data
DATASET_PATH = "data/tourism.csv"
output_dir = "data" # This is now relative to the script's CWD
os.makedirs(output_dir, exist_ok=True) # Ensure output directory exists

df = pd.read_csv(DATASET_PATH)
print("Dataset loaded successfully.")

# Encode categorical columns
label_encoder = LabelEncoder()
for col in ['TypeofContact', 'Occupation', 'Gender', 'MaritalStatus', 'ProductPitched', 'Designation']:
    df[col] = label_encoder.fit_transform(df[col])

# Target column
target_col = 'ProdTaken'

# Split into X (features) and y (target)
X = df.drop(columns=[target_col, 'CustomerID'])
y = df[target_col]

# Perform train-test split
Xtrain, Xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Save the processed dataframes to CSV files in the data directory
Xtrain.to_csv(os.path.join(output_dir, "Xtrain.csv"), index=False)
Xtest.to_csv(os.path.join(output_dir, "Xtest.csv"), index=False)
ytrain.to_csv(os.path.join(output_dir, "ytrain.csv"), index=False)
ytest.to_csv(os.path.join(output_dir, "ytest.csv"), index=False)

print("Processed data saved to: ", output_dir)
