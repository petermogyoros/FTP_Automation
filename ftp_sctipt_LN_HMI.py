import fnmatch
import os
from ftplib import FTP
import subprocess

# Define connection variables
ip_win = '192.168.3.99'
ip_linux = '127.1.1.9'

#win_path = 'C:\\Users\petermogyoros\Documents\FTP_LN_HMI'
linux_path = '/home/peter/csv/LN_HMI/fresh_csv'

# Establish FTP Connection
try:
    ftp = FTP(ip_linux)  # connect to remote host
    print(ftp.getwelcome())  # FTP Server returns a welcome message
except:
    print("FTP Server not available. Please check connection!")
    quit()

# Login to FTP Server
try:
    ftp.login(user='Admin', passwd='0000')
    print("Logged in!")
except:
    print("Login failed. Please, check your login details!")
    quit()


def get_data():
    ftp.cwd('/Project1/LOG00001')
    print(linux_path)
    local_dir = linux_path  # win_path for testing and linux_path for production
    os.chdir(local_dir)
    pattern = '*.csv'  # choose search pattern
    print("*" * 50, "LIST", "*" * 50)
    print(ftp.dir())

    #subprocess.run(['ls', '-l'])
    print("before")
    for l in ftp.MLSD():
        print("after")
        # only find files with the .csv extension
        if fnmatch.fnmatch(l, pattern):

            # Create directory (local_dir) if it doesn't already exist
            if os.path.exists(local_dir):
                pass
            else:
                os.mkdir(local_dir)

            # Download file
            with open(l, 'wb') as file:
                try:
                    ftp.retrbinary('RETR %s' % l, file.write)
                    print("File" + " " + l + " " + "downloaded successfully")
                except:
                    print("File" + " " + l + " " + "download failed!")
                    break

            # Delete after downloaded
            try:
                #ftp.delete(l)
                print("Now deleted from device!")
            except:
                print("Could not delete file.")
                break


get_data()
