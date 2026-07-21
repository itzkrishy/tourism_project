
import os
data_folder = "tourism_project_local/data"
if os.path.exists(data_folder):
    print(f"Data folder '{data_folder}' exists.")
else:
    print(f"Data folder '{data_folder}' does not exist.")
