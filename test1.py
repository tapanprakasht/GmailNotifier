__author__ = 'tapan'
#/usr/bin/python3
import os
def main():
    directoryname=os.path.expanduser("~")+"/.gmailnotify/gmail.txt"
    d=os.path.dirname(directoryname)
    if not os.path.exists(d):
        os.mkdir(d)
if __name__=="__main__":main()
