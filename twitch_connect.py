import socket
import os
import time
from dotenv import load_dotenv
load_dotenv()

class twitch_chat_bot:    
    connection_data = ('irc.chat.twitch.tv', 6667)
    token = os.getenv('TOKEN')
    user_name = 'python_bot'
    channel = '#showdownspectator'
    readbuffer = ''
    server = socket.socket()    
    server.connect(connection_data)
    server.send(bytes('PASS '+ token + '\r\n', 'utf-8'))
    server.send(bytes('NICK '+ user_name + '\r\n', 'utf-8'))
    server.send(bytes('JOIN '+ channel + '\r\n', 'utf-8'))

    def post_msg(self, text_to_send):
        try:
            msg = "PRIVMSG " + self.channel + " :" + text_to_send + "\r\n"
            self.server.send(bytes(msg, 'utf-8'))
        except:
            time.sleep(5)
            print("Caught disconnection exception, retrying")
            self.server.connect(self.connection_data)
            self.server.send(bytes('PASS '+ self.token + '\r\n', 'utf-8'))
            self.server.send(bytes('NICK '+ self.user_name + '\r\n', 'utf-8'))
            self.server.send(bytes('JOIN '+ self.channel + '\r\n', 'utf-8'))
            msg = "PRIVMSG " + self.channel + " :" + text_to_send + "\r\n"
            self.server.send(bytes(msg, 'utf-8'))


