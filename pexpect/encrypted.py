#!usr/bin/env/python python3
from pexpect import pxssh
import getpass

devices = {'r1': {'prompt': 'R1#', 'ip': '172.26.1.1'},
           'r2': {'prompt': 'R2#', 'ip': '172.26.2.1'}}

commands = ['term length 0', 'show version', 'show run']

username = input("Username: ")
password = getpass.getpass("Password: ")

for device in devices.keys():
    outputFileName = device + "_output.txt"
    device_prompt = devices[device]['prompt']
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)    
    
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)
        child.logout()
    
    