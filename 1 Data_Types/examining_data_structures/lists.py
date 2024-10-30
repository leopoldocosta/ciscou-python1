import netmiko

ip_list = [
    '10.254.0.1',
    '10.254.0.2',
    '10.254.0.3',
]
# print(ip_list[0])
# print(ip_list[-1])

username = 'cisco' 
password = 'cisco' 
device_type = 'cisco_ios' 
port = 22 

output_list = []  
for ip in ip_list:
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, 
        username=username, password=password, port=port)
    output = net_connect.send_command('show ip interface brief')
    output_list.append(output)

    for output in output_list:
        print(output)
        
# student@student-vm:~/lab_work$ python lists.py
# 10.254.0.1
# 10.254.0.3
# student@student-vm:~/lab_work$ 
# student@student-vm:~/lab_work$ python lists.py
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       unassigned      YES NVRAM  up                    up      
# GigabitEthernet2       10.12.0.1       YES NVRAM  up                    up      
# GigabitEthernet3       10.13.0.1       YES NVRAM  up                    up      
# GigabitEthernet4       10.254.0.1      YES NVRAM  up                    up      
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       unassigned      YES NVRAM  up                    up      
# GigabitEthernet2       10.12.0.1       YES NVRAM  up                    up      
# GigabitEthernet3       10.13.0.1       YES NVRAM  up                    up      
# GigabitEthernet4       10.254.0.1      YES NVRAM  up                    up      
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       10.12.0.2       YES NVRAM  up                    up      
# GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
# GigabitEthernet3       10.23.0.2       YES NVRAM  up                    up      
# GigabitEthernet4       10.254.0.2      YES NVRAM  up                    up      
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       unassigned      YES NVRAM  up                    up      
# GigabitEthernet2       10.12.0.1       YES NVRAM  up                    up      
# GigabitEthernet3       10.13.0.1       YES NVRAM  up                    up      
# GigabitEthernet4       10.254.0.1      YES NVRAM  up                    up      
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       10.12.0.2       YES NVRAM  up                    up      
# GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
# GigabitEthernet3       10.23.0.2       YES NVRAM  up                    up      
# GigabitEthernet4       10.254.0.2      YES NVRAM  up                    up      
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       10.13.0.3       YES NVRAM  up                    up      
# GigabitEthernet2       10.23.0.3       YES NVRAM  up                    up      
# GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
# GigabitEthernet4       10.254.0.3      YES NVRAM  up                    up      
#     student@student-vm:~/lab_work$ ^C