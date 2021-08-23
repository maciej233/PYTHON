#!usr/bin/env/python python3
import pexpect
import getpass

devices = {'r1': {'prompt': 'R1#', 'ip': '172.26.1.1'},
           'r2': {'prompt': 'R2#', 'ip': '172.26.2.1'}}

username = input("Username: ")
password = getpass.getpass("Password: ")

for device in devices.keys():
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    device_prompt = devices[device]['prompt']
    child.expect('[Uu]sername:')
    child.sendline(username)
    child.expect('[Pp]assword:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline("show version | include V")
    child.expect(device_prompt)
    print(child.before) 
    child.sendline('exit')
    
    