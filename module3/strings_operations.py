connection_info = '10.254.0.1,cisco,cisco'

# print(connection_info)
connection_info_list = connection_info.split(',')
# print(connection_info_list)

n = 1
ip_three_octets = '10.254.0.'
# print(ip_three_octets + str(n))
# print(ip_three_octets + str(n + 1))
# print(ip_three_octets + str(n + 2)) 

ip = '10.254.0.1'
device_type = 'cisco_ios'
print(f'The router at {ip} is running {device_type}')