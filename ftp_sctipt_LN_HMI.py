from ftplib import FTP
import fnmatch, sys, os, csv
import pandas as pd

# FTP Section
ftp = FTP('192.168.3.99')  # connect to remote host
ftp.login(user='Admin', passwd='0000')

def get_data() -> str:
    ftp.cwd('/Project1/LOG00001')
    root_dir = ftp.nlst()
    local_dir = os.chdir('C:\\Users\petermogyoros\Documents')
    pattern = '*.csv'  # choose search patern
    for l in root_dir:
        # only find files with the .csv extention
        if fnmatch.fnmatch(l, pattern):
            local_dir = 'C:\\Users\petermogyoros\Documents\FTP_LN_HMI'

            # Create directory (local_dir) if it doesn't already exist
            if os.path.exists(local_dir):
                pass
            else:
                os.mkdir(local_dir)

            print(ftp.getwelcome())  # FTP Server returns a welcome message

            return(l)



data = get_data()

with open(data, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        print(', '.join(row))
#pd.DataFrame([x.split(';') for x in data.split('\n')])
#print(df)

# ftp.delete(data)
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