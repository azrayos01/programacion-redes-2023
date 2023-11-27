"""
Conexion
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha; 24 de Noviembre del 2023
"""

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='10.10.20.48',
    port=22,
    username = 'developer',
    password = 'C1sco12345'
)

salida = sshCli.send_command('show ip int brief')
print(salida)