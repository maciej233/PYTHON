import pyexpect

commands = ['term length 0', 'show version | i V']

# wersja telnet
def show_version_telnet(device_name, prompt, ip, username, password):
    device_prompt = prompt
    child = pyexpect.spawn('telnet', ip)
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    for command in commands:
        child.sendline(command)
        child.expect(device_prompt)
    result = child.before
    child.sendline('Exit')
    return device_name, result


#wersja ssh + zapis wyniku do pliku, niewykorzystano
def save_version_ssh(device_name, prompt, ip, username, password):
    device_prompt = prompt
    child = pyexpect.pxssh.pxssh()
    child.login(ip, username.strip(), password.strip(), auto_prompt_reset=False)
    outPutFileName = device_name + '_output.txt'
    with open(outPutFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)
        child.logout()

    