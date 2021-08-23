#!/home/maciej/environments/networking/bin/python python3

from netmiko import ConnectHandler

r1 = {'device_type': 'cisco_ios', 'host': '172.26.1.1', 'username': 'cisco', 'password': 'cisco'}
net_connect = ConnectHandler(**r1)
prompt = net_connect.find_prompt()
output_int = net_connect.send_command('show ip int brief')

print(prompt)

print(output_int)

r2 = {'device_type': 'cisco_ios', 'host': '172.26.2.1', 'username': 'cisco', 'password': 'cisco'}
net_connect2 = ConnectHandler(**r2)
output_r2 = net_connect.send_config_set(['logging buffer 19999'])
print(output_r2)
