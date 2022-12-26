# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import paramiko


host = "hemalatha-virtual-machine"
username= "hemalatha"
password = "Kumar@1234"
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=host, username=username, password=password)
sftp_client=session.open_sftp()
sftp_client.put('main.py','/home/hemalatha/main.py'
                          '')
sftp_client.close()
session.close()



