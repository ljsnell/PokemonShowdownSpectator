# # `twitch_connect.py`
# A class for posting messages to a specified Twitch `channel` using a specified `token` and `user_name`. Modify the relevant variables in the class definition to suit project requirements.

import socket
import os
import time
from dotenv import load_dotenv
load_dotenv()

class twitch_chat_bot:
    
    # connection information
    connection_data = ('irc.chat.twitch.tv', 6667)
    token = os.getenv('TOKEN')
    user_name = 'python_bot'
    channel = '#showdownspectator'

    # initiate connection
    server = socket.socket()    
    server.connect(connection_data)
    server.send(bytes('PASS '+ token + '\r\n', 'utf-8'))
    server.send(bytes('NICK '+ user_name + '\r\n', 'utf-8'))
    server.send(bytes('JOIN '+ channel + '\r\n', 'utf-8'))

    def post_msg(self, text_to_send):
        "Attempt to post message to channel, restarting server connection upon first failure."
        msg = "PRIVMSG " + self.channel + " :" + text_to_send + "\r\n"
        self.server.send(bytes(msg, 'utf-8'))

    def respond_to_pings(self):
        text = self.server.recv(2040)
        print(text)
        if 'PING' in str(text):
            print("Sending the pong!")
            self.server.send(bytes('PONG :tmi.twitch.tv', 'utf-8'))