import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import os
import fnmatch

linux_work_dir = '/home/peter/csv/LN_HMI/fresh_csv'
win_work_dir = "C:\\Users\\petermogyoros\\PycharmProjects\\DG_stoppage_processinG"

win_new_location = "C:\\Users\\petermogyoros\\PycharmProjects\\DG_stoppage_processing\\processed\\%s"
linux_new_location = "/home/peter/csv/LN_HMI/processed"

csv_working_directory = linux_work_dir
csv_new_location = linux_new_location

# list through each file in the working_directory
log_folder = os.listdir(csv_working_directory)

pattern = '*.CSV'  # choose search pater
# loop through folders that contain the .csv files
for entry in log_folder:
    # only find files with the .csv extention
    if fnmatch.fnmatch(entry, pattern):
        # Change working directory to log_folder to be able to ready cvs files
        os.chdir(csv_working_directory)
        df = pd.read_csv(entry, index_col=False)  # returns a DataFrame
        print(df)
        quit()
