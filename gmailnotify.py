__author__ = 'tapan'
#!/usr/bin/python3

from xml.dom.minidom import  parseString

class GmailNotify:
    def __init__(self):
        pass
    def readFile(self):
        xmlfile=open('gmail.xml')
        data=xmlfile.read()
        xmlfile.close()
        dom=parseString(data)


        for k in range(0,len(dom.getElementsByTagName('title'))):
           xmlTag=dom.getElementsByTagName('title')[k].toxml()
           xmlData=xmlTag.replace('<title>','').replace('</title>','')
           print(xmlData,end='\n\n')



def main():
    g=GmailNotify()
    g.readFile()

if __name__=="__main__":main()