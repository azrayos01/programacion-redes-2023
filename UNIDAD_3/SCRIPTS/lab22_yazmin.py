"""
Conexion
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 06 de Diciembre del 2023
"""

import netmiko
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.10.20.48',
    port = 22,
    username = "developer",
    password = 'C1sco12345'
)

output = sshCli.send_command("show ip int brief")
print ("Show ip int brief:\n{}\n".format (output))

config_commands = [
    'int loopback 2', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description WHATEVER'
                  ] 

output = sshCli.send_config_set(config_commands)


