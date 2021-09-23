import fnmatch
import os
from ftplib import FTP

# Establish FTP Connection
try:
    ftp = FTP('127.1.1.9')  # connect to remote host
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


def get_data() -> str:
    ftp.cwd('/Project1/LOG00001')
    root_dir = ftp.nlst()
    local_dir = '/home/peter/csv/LN_HMI/fresh_csv'
    os.chdir(local_dir)
    pattern = '*.csv'  # choose search pattern
    for l in root_dir:
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
                ftp.delete(l)
                print("Now deleted from device!")
            except:
                print("Could not delete file.")
                break


data = get_data()
