from ftplib import FTP
import time, fnmatch, sys, os, csv
import pandas as pd


# Time Section for file renaming
secs = int(time.time())  # convert time secs to integer

# FTP Section
ftp = FTP('10.0.0.2')  # connect to remote host
ftp.login(user='admin', passwd='0000')


# 50g Beanies Gold prog:000

ftp.cwd("/SD2/cv-x/result/")
ftp.retrlines('LIST')

"""
except:
    pass

# 100g Yoda Red prog:007
try:
    ftp.cwd('/SD2/cv-x/result/SD1_007')
    ftp.retrlines('LIST')
except:
    pass

# 150g Dawn Brown P45 prog:014
try:
    ftp.cwd('/SD2/cv-x/result/SD1_014')
    ftp.retrlines('LIST')
except:
    pass

# 250g Dawn Brown P45 prog:020
try:
    ftp.cwd('/SD2/cv-x/result/SD1_020')
    ftp.retrlines('LIST')
except:
    pass

# 250g Dawn Brown P46 prog:021
try:
    ftp.cwd('/SD2/cv-x/result/SD1_021')
    ftp.retrlines('LIST')
except:
    pass

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