import paramiko, time, getpass, json

# na potrzeby serwerów
#key = paramiko.RSAKey.from_private_key_file("home/user/.ssh/id_rsa")

username = input("Username: ")
password = getpass.getpass("Password: ")

max_buffer = 65535

# piliki zewnetrzne
with open("commands.txt", 'r') as f:
    commands = f.readlines()

with open("devices.json", 'r') as f:b
    devices = json.load(f)

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


for device in devices.keys():
    outputFileName = device + "_output.txt"
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open("outputFileName", 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)
    new_connection.close()