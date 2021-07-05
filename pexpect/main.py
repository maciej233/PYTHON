#!usr/bin/env/python python3
import pexpect
import getpass

devices = {'r1': {'prompt': 'r1#', 'ip': '172.26.1.1'},
           'r2': {'prompt': 'r2#', 'ip': '172.26.1.2'}}

username = input("Username: ")
password = getpass.getpass("Password: ")

for device in devices.keys():
    child = pexpect.spawn('telnet', devices[device]['ip'])
    device_prompt = devices[device]['prompt']
    child.expect('[Uu]sername:')
    child.sendline(username)
    child.expect('[Pp]assword:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline("show version | include V")
    result = child.before()
    child.sendline('exit')
    print(result)