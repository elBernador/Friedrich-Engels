'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.01.01
von Mark Rygielski

Nachricht auf Unangemessenes Verhalten Testen
Bedeutung: Geschriebenes mit der Blacklist abgleichen
-----------------------------------------------------------------'''


#Setup:

#importiere Bibliotheken:
import os, re
#------------------------------------------------------------------



def testmessage(content, blacklistname):
    blacklistname

    #import Blacklist
    with open (blacklistname) as data:
        blacklist_raw = data.read()
        blacklist = set (re.sub("[^\w]", " ",  blacklist_raw).split())
    
    #convert content into Word-list
    wordList = set( re.sub("[^\w]", " ",  content).split())
    
    #Prüfe auf überschneudung der Liste
    if len(wordList.intersection(blacklist)) > 0: 
        #haben Überschneidung --> Nachricht nicht OK
        return 'bad'
        
    else:
        #haben keine Übereinstimmung --> Nachricht OK
        return 'good'

