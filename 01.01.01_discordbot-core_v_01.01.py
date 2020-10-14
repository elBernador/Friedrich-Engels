'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.01.01
von Mark Rygielski

Aufgabe:
Unangemessenes Verhalten im Chat erkennen und bestrafen
Bedeutung der Aufgabe in dieser Version
Unangemessenes Verhalten: ein geschriebenes Wort ist auf einer Liste
Bestrafen: im Chat aufmerksam machen

Externe Datein (im selben Ordner):
- .ent mit dem Token
- Liste mit gebannten Wörtern
-----------------------------------------------------------------'''


#Setup
#------------------------------------------------------------------

#Globale Variablen
_command_prefix_ = '~'
_blacklist_ = ['xxx', 'yyy']

#importiere Bibliotheken:
import discord, os, re
from dotenv import load_dotenv

#importiere Token mithilfe von dotenv:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#------------------------------------------------------------------



#Testet, ob content (liste von Wörtern) ein wort der Blacklist enthält    
def checkContent(content):
    blacklist=_blacklist_
    if (str((set(content) & set(blacklist))) == str('set()')):
        #haben keine überschneidung --> Nachricht OK
        return True
        
    else:
        #haben Übereinstimmung --> Nachricht nicht OK
        return False
    


def main():

    #client instanz erzeugen:
    client = discord.Client()


    @client.event
    async def on_ready():
        '''
        Läuft, wenn Bot startet / die Verbindung zu Discord herstellt
        @client.event wird ausgelöst, wenn dass darunter benannte Event eintritt
        '''
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_disconnect():
        #Läuft, die Verbindung zum Server abbricht
        print("Bot has logged off")

        
    @client.event
    async def on_message(message):
        #läuft, wenn der Bot eine Nachricht erhält
        if message.author == client.user:
            #testet, ob der Bot die Nachricht selber gesendet hat
            return
        
        if message.content.startswith(_command_prefix_):
            #prüft, ob ein Befehl gegeben wurde
            print ('command')
        
        #nimmt den Nachrichteninhalt als Liste der Wörter
        content = message.content
        wordList = re.sub("[^\w]", " ",  content).split()

        #prüft Nachricht
        if checkContent(wordList) == True:
            return
        else:
            await message.channel.send('Bad')
    #------------------------------------------------------------------

       
    #lässt den Client mit dem TOKEN laufen
    client.run(TOKEN)



if __name__ == "__main__":
    main()
