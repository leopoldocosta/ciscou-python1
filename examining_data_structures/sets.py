import netmiko 
 
ip_addrs = [ 
    '10.254.0.1', 
    '10.254.0.2', 
    '10.254.0.1', 
    '10.254.0.3', 
    '10.254.0.2', 
    '10.254.0.3', 
    '10.254.0.3', 
    '10.254.0.2', 
    '10.254.0.3', 
]

ip_addrs_unique = set(ip_addrs)
print(ip_addrs_unique)
print(sorted(ip_addrs_unique))

# student@student-vm:~/lab_work$ python sets.py
# {'10.254.0.3', '10.254.0.2', '10.254.0.1'}
# ['10.254.0.1', '10.254.0.2', '10.254.0.3']