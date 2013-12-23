#!/usr/bin/python3
__author__ = 'tapan'

# GmailNotify 1.0
# A Terminal based Gmail notifier
# By Tapan Prakash T

from urllib.request import urlopen,HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener,install_opener
                                              # Import library to do http request
import sys                                    # Import library to do command line arguments
import base64                                 # Library to encode and decoded username and password
from xml.dom.minidom import  parseString      # xml parser library
import os                                     # For creating directory
import getpass                                # library to get password from terminal without echoing to terminal

class GmailNotify:                            # Main class for the gmailnotify
    def __init__(self):
        self.user=dict(                       #Dict to store the username and password
                username='',
                password=''
             )


    def pasrseXml(self):                       # Method to parse the xml file
        try:
            # Get the url with password authentication
            theurl='https://mail.google.com/mail/feed/atom'
            username=self.user['username'].strip()
            password=self.user['password'].strip()

            passman=HTTPPasswordMgrWithDefaultRealm()
            passman.add_password(None,theurl,username,password)
            authhandler=HTTPBasicAuthHandler(passman)
            opener=build_opener(authhandler)
            install_opener(opener)

            xmlfile=urlopen(theurl)               # Fetch xml file
            data=xmlfile.read()                   # read the xml file
            xmlfile.close()
            dom=parseString(data)                 # Parsing the data

            # Print header message and number of unread messages
            xmlTag=dom.getElementsByTagName('title')[0].toxml()
            xmlData=xmlTag.replace('<title>','').replace('</title>','')
            print(xmlData.center(80,' '))
            print("You have {} unread new messages".format(len(dom.getElementsByTagName('title'))-1))
            print("-------------------------------------------------------------------------")

            totalmessages=len(dom.getElementsByTagName('title'))         # Get total number of messages

            # Print the name and title of each messages
            # \033[91m like strings for setting the output text colour
            for k in range(1,totalmessages):
                xmlTagtitle=dom.getElementsByTagName('title')[k].toxml()
                xmlDatatitle=xmlTagtitle.replace('<title>','').replace('</title>','')
                xmlTagname=dom.getElementsByTagName('name')[k-1].toxml()
                xmlDataname=xmlTagname.replace('<name>','').replace('</name>','')
                print("\033[91m",xmlDataname.ljust(25,' '),end=' ')
                print("\033[92m",xmlDatatitle)
                print("\033[0m______________________________________________________________________________________________________________________")
        except:
            print("Error in connection")
    def getUsercredentials(self):                                   # Method to get the username and password from the file
        try:
            credentialfile=open(os.path.expanduser("~")+"/.gmailnotify/gmail.txt")
            credentialfiledata=credentialfile.readlines()
            self.user['username']=str(credentialfiledata[0]).strip()
            self.user['password']=str(credentialfiledata[1]).strip()
            # print(self.user['username'])
            # print(self.user['password'])
            return True
        except:
            print("Your credential file is missing.Use 'python3 gmailnotify.py --config' to reconfigure it.")
            return False

    def createConfig(self):                                           # Method to set the user configuration
        filename=os.path.expanduser("~")+"/.gmailnotify/gmail.txt"
        dirname=os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        configfile=open(filename,'w')
        username=input("Username:")
        password=getpass.getpass('Password:')
        #username=base64.b64encode(bytes(username,"utf_8"))           # Encoding the username and password before writing to file
        #password=base64.b64encode(bytes(password,"utf_8"))
        print(username,file=configfile)
        print(password,file=configfile)
        configfile.close()

    def showHelp(self):                                               # Method to show the help messages
        print("Configure username and password           gmailnotify.py --config")
        print("About                                     gmailnotify.py --about")

    def showAbout(self):                                              #Method to show about messages
        print("GmailNotify 1.0 ")
        print("By Tapan Prakash T")
        print("Email:tapanprakasht@gmail.com")
        print("Gmailnotify is a terminal based Gmail notifier written in python.")

def main():

    g=GmailNotify()                                             # Created GmailNotify class object
    if len(sys.argv)>2:                                         # Checking the the no. of command line arguments
        print("gmailnotify.py takes only one argument.Try ' gmailnotify.py --help' for help")
    elif len(sys.argv)==2:
        if sys.argv[1]=='--help':                               #If commadline arg is --help
            g.showHelp()
        elif sys.argv[1]=='--about':                            #If commadline arg is --about
            g.showAbout()
        elif sys.argv[1]=='--config':                           #If commadline arg is --config
            print("Configuration")
            g.createConfig()
        elif len(sys.argv)==2:                                  #If commadline arg is invalid
            print("Invalid argument")
    else:                                                       # If there is no command line argument
        if g.getUsercredentials():                              # Check whether username and password file exist.
            g.pasrseXml()                                       #Start parsing the data

if __name__=="__main__":main()