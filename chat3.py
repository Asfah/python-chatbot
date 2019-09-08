from fbchat import Client
from getpass import getpass
from fbchat.models import *


username = str(input("Username: "))
client = Client(username, getpass())

n = int(input("Enter number of bulk message: "))

name = str(input("Enter frind name: "))
friend = client.searchForUsers(name)[0]

if friend.name == name:
  print(friend.name)

msg = str(input("Enter message to send: "))

for i in range (n+1):
 sent = client.send(Message(text=msg), friend.uid)

 if sent:
  print("Message sent succesfully...")

