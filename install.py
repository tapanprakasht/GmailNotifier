__author__ = 'tapan'
# Gmailnotify installer
import os
import shutil

def main():
    try:
        pwd=os.path.dirname(os.path.realpath(__file__))                                        # Get the the current path
        # print(pwd)
        shutil.copyfile(pwd+"/gmailnotify.py",os.path.expanduser("~")+"/.gmailnotify.py")      #Copy the file to home directory
        bashrc=open(os.path.expanduser("~")+"/.bashrc",'a')                                    #Open .bashrc file in append mode
        bashrc.write("alias gmailnotify=\"/usr/bin/python3 ~/.gmailnotify.py\"")                  # Write alias to .bashrc file
        print("Installation finished")
        print("Restart terminal before using below commands")
        print("Use \'gmailnotify --config\' to configure username and password for your account")
        print("Use \'gmailnotify\' to run Gmailnotify")
    except:
        print("Error occured!")
if __name__=="__main__":main()

