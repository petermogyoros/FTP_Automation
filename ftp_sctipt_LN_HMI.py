from ftplib import FTP
import fnmatch, sys, os, csv
import pandas as pd


# FTP Section
ftp = FTP('192.168.3.99')  # connect to remote host
ftp.login(user='Admin', passwd='0000')

def get_data() -> str:
    ftp.cwd('/Project1')
    ftp.retrlines('LIST')

get_data()

"""

# 250g Dawn Red P16 prog:025
#try:
ftp.cwd('/SD2/cv-x/result/SD1_025')
root_dir = ftp.nlst()
local_dir = os.chdir('C:\\Users\\mogyorosp\\PycharmProjects\\Keyence_csv\\csv_testing')
pattern = '*.csv'  # choose search pater
for l in root_dir:
    # only find files with the .csv extention
    if fnmatch.fnmatch(l, pattern):

        local_dir = 'C:\\Users\\mogyorosp\\PycharmProjects\\Keyence_csv\\csv_testing'

        if not os.path.exists(local_dir):
            os.mkdir(local_dir)



        # rename file so it won't overwrite an existing file on server
        rename = sys.stderr.write(str(int(time.time())) + '-' + l)  # add secs to the name

        #file_object = open(rename, 'rb')
        pd.read_csv(l, index_col=False) # returns a DataFrame
        #ftp.storlines(write, rename)
        #os.chdir(csv_working_directory)

        #print(l)
       # sys.stderr.write(l+'-' + int(time.time()))
        #dir_files = ftp.nlst(l)
        #print(dir_files)
    #ftp.retrlines('LIST')
#except:
    #pass
"""