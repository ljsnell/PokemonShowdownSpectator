import socket
import os
from dotenv import load_dotenv
load_dotenv()

class twitch_chat_bot:    
    connection_data = ('irc.chat.twitch.tv', 6667)
    token = os.getenv('TOKEN')
    user_name = 'python_bot'
    channel = '#showdownspectator'
    readbuffer = ''
    server = socket.socket()
    authenticate(server)

    def post_msg(self, text_to_send):
        try:
            msg = "PRIVMSG " + self.channel + " :" + text_to_send + "\r\n"
            self.server.send(bytes(msg, 'utf-8'))
        except:
            print("Caught disconnection exception, retrying")
            authenticate(self.server)
            post_msg(text_to_send)

    def authenticate(self, server):
        self.server.connect(connection_data)
        self.server.send(bytes('PASS '+ token + '\r\n', 'utf-8'))
        self.server.send(bytes('NICK '+ user_name + '\r\n', 'utf-8'))
        self.server.send(bytes('JOIN '+ channel + '\r\n', 'utf-8'))
