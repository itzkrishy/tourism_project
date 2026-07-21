
data_folder = "tourism_project/data"
if os.path.exists(data_folder):
    print(f"Data folder '{data_folder}' exists. Data is expected to be here for GitHub integration.")
else:
    print(f"Data folder '{data_folder}' does not exist. Please ensure data is placed here.")
