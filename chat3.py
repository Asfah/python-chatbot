from fbchat import Client
from getpass import getpass
from fbchat.models import *


username = str(input("Username: "))   #Enter phone number or username
client = Client(username, getpass())   #Enter the password

n = int(input("Enter number of bulk message: ")) #Entre the number of messages you want to send

name = str(input("Enter frind name: "))     #Entr name of the friend ou want to send the message to
friend = client.searchForUsers(name)[0]

if friend.name == name:
  print(friend.name)

msg = str(input("Enter message to send: "))     #Enter the message

for i in range (n+1):
 sent = client.send(Message(text=msg), friend.uid)

 if sent:
  print("Message sent succesfully...")

