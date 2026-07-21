
import os

# The data folder should be relative to the script's execution context (which is the root of the cloned repo)
data_folder = "data"
if os.path.exists(data_folder):
    print(f"Data folder '{data_folder}' exists. Data is expected to be here for GitHub integration.")
else:
    print(f"Data folder '{data_folder}' does not exist. Please ensure data is placed here.")
