from dolcegusto.models import DolceGusto_table
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import os, fnmatch
import time

import traceback

# loop through folders to find new csv files and update datebase
def loop_through_folders(line):
    def get_values_72_imp_stack_tool(csv1, list_of_results):
        datetime_list = []

        # extract date and time from the log file
        date_of_csv_raw = csv1.loc[[1], 'Date']
        str_date = str(date_of_csv_raw)
        year = str(str_date[5:9])
        month = str(str_date[10:12])
        day = str(str_date[13:15])

        time_of_csv_raw = csv1.loc[[1], 'Time']
        time_of_csv_full = str(time_of_csv_raw)
        time_of_csv = time_of_csv_full[5:13]

        datetime_list.append(year)
        datetime_list.append("-")
        datetime_list.append(month)
        datetime_list.append("-")
        datetime_list.append(day)
        datetime_list.append(" ")
        datetime_list.append(time_of_csv)

        # join strings to create date string
        datetime_of_csv_str = ''.join(datetime_list)
        # create a datetime format from the date string
        datetime_of_csv = datetime.strptime(
        datetime_of_csv_str,'%Y-%m-%d %H:%M:%S'
        )
        # extracting data from *.cvs into Series#
        batch = int(csv1.loc[[1], 'Total'])
        ok = csv1.loc[[148, 296], 'OK']
        rejects = csv1.loc[[148, 296, 149, 297, 150, 298, 151, 299], 'Reject']
        recycles = csv1.loc[[148, 296, 149, 297, 150, 298, 151, 299], 'Recycle']

        # converting Series to dict
        ok_dict_raw = ok.to_dict()
        reject_dict_raw = rejects.to_dict()
        recycle_dict_raw = recycles.to_dict()

        # assigning descriptive dictionary keys
        ok_dict_keys = {148:"side_b", 296:"side_a"}

        ng_dict_keys = {
        148:"combined_side_b_ng", 296:"combined_side_a_ng",
         149:"top_b", 297:"top_a", 150:"bottom_b",
         298:"bottom_a", 151:"side_b", 299:"side_a"
         }

        re_dict_keys = {
        148:"combined_side_b_re", 296:"combined_side_a_re",
        149:"top_b", 297:"top_a", 150:"bottom_b",
        298:"bottom_a", 151:"side_b", 299:"side_a"
        }


        ok_dict = dict((ok_dict_keys[key], int(value)) for (key, value) in ok_dict_raw.items())
        reject_dict = dict((ng_dict_keys[key], int(value)) for (key, value) in reject_dict_raw.items())
        recycle_dict = dict((re_dict_keys[key], int(value)) for (key, value) in recycle_dict_raw.items())

        list_of_results.append(ok_dict)
        list_of_results.append(reject_dict)
        list_of_results.append(recycle_dict)
        list_of_results.append(datetime_of_csv)
        list_of_results.append(batch)

        return list_of_results

    def update_db_72_imp_stack_tool(list_of_results, line):

        #update db
        ok_dict = list_of_results[0]
        reject_dict = list_of_results[1]
        recycle_dict = list_of_results[2]
        datetime_of_csv = list_of_results[3]
        batch = list_of_results[4]

        db_update = DolceGusto_table(
        csv_datetime = datetime_of_csv,
        line = line, batch = batch,
        a_ok = int(ok_dict["side_a"]),
        b_ok = int(ok_dict["side_b"]),
        combined_side_a_ng = int(reject_dict["combined_side_a_ng"]),
        combined_side_b_ng = int(reject_dict["combined_side_b_ng"]),
        a_top_ng = int(reject_dict["top_a"]),
        b_top_ng = int(reject_dict["top_b"]),
        a_bottom_ng = int(reject_dict["bottom_a"]),
        b_bottom_ng = int(reject_dict["bottom_b"]),
        a_side_ng = int(reject_dict["side_a"]),
        b_side_ng = int(reject_dict["side_b"]),
        combined_side_a_re = int(recycle_dict["combined_side_a_re"]),
        combined_side_b_re = int(recycle_dict["combined_side_b_re"]),
        a_top_re = int(recycle_dict["top_a"]),
        b_top_re = int(recycle_dict["top_b"]),
        a_bottom_re = int(recycle_dict["bottom_a"]),
        b_bottom_re = int(recycle_dict["bottom_b"]),
        a_side_re = int(recycle_dict["side_a"]),
        b_side_re = int(recycle_dict["side_b"]),
        product = "Dolce Gusto",
        production_site = "Eaton Socon")

        db_update.save()

        list_of_results = []


    working_directory = '/home/peter/DataBooth_project'

    # set working directory based on line number
    if line == 3:
        csv_working_directory = '/home/peter/csv/line3'
        new_location = '/home/peter/csv/line3/2018/%s'

    elif line == 4:
        csv_working_directory = '/home/peter/csv/line4'
        new_location = '/home/peter/csv/line4/2018/%s'

    elif line == 5:
        csv_working_directory = '/home/peter/csv/line5'
        new_location = '/home/peter/csv/line5/2018/%s'

    elif line == 7:
        csv_working_directory = '/home/peter/csv/line7'
        new_location = '/home/peter/csv/line7/2018/%s'

    elif line == 8:
        csv_working_directory = '/home/peter/csv/line8'
        new_location = '/home/peter/csv/line8/2018/%s'

    elif line == 9:
        csv_working_directory = '/home/peter/csv/line9'
        new_location = '/home/peter/csv/line9/2018/%s'

    elif line == 10:
        csv_working_directory = '/home/peter/csv/line10'
        new_location = '/home/peter/csv/line10/2018/%s'


    # list through each file in the working_directory
    log_folder = os.listdir(csv_working_directory)

    pattern = '*.csv' # choose search pater
    # loop through folders that contain the .csv files
    for entry in log_folder:
        # only find files with the .csv extention
        if fnmatch.fnmatch(entry, pattern):
            # Change working directory to log_folder to be able to ready cvs files
            os.chdir(csv_working_directory)
            csv1 = pd.read_csv(entry, index_col=False) # returns a DataFrame

            # Determine tool cavitation number
            if int(csv1.loc[[149], 'Cavity']) < 0: #72 cavity tool


                list_of_results = []
                get_values_72_imp_stack_tool(csv1, list_of_results)

                if bool(list_of_results) is True:
                    update_db_72_imp_stack_tool(list_of_results, line)
                else:
                    print("Empty list - PROBLEM IN CODE")

            else:
                print("wrong file type")

            move_to = (new_location %(entry))
            os.rename(entry, move_to)

            # completion feedback after every file. Probably can be removed after testing
            print(line, entry)

            # change back working directory to where collector.py is located
            os.chdir(working_directory)

            time.sleep(0.2)


def run_exception(line):
    try:
        loop_through_folders(line)
    except:
        pass

# searches for csv and updates database
class Collector():

    while_counter = 0
    while True:
        while_counter += 1
        print(while_counter)

        # add machine here to update database
        # also update loop_through_folders() function
        run_exception(3)
        run_exception(4)
        run_exception(5)
        run_exception(7)
        run_exception(8)
        run_exception(9)
        run_exception(10)
        time.sleep(5)
        if while_counter == 10:
            quit()
