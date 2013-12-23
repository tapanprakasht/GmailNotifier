__author__ = 'tapan'
# Gmailnotify installer
import os
import shutil

def main():
    try:
        pwd=os.path.dirname(os.path.realpath(__file__))
        # print(pwd)
        shutil.copyfile(pwd+"/gmailnotify.py",os.path.expanduser("~")+"/.gmailnotify.py")
        bashrc=open(os.path.expanduser("~")+"/.bashrc",'a')
        bashrc.write("alias gmailnotify=\"/usr/bin/python3 ~/.gmailnotify\"")
        print("Installation finished")
        print("Use \'gmailnotify --config\' to configure username and password for your account")
        print("Use \'gmailnotify\' to run Gmailnotify")
    except:
        print("Error occured!")
if __name__=="__main__":main()

