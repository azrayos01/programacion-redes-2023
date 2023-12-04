"""
Autor: Rincon Ulloa Yazmin Elizabeth
Descripcion: YANG models
Fecha: Viernes 04 de Diciembre del 2023
"""

import xml.dom.minidom
import ncclient
from ncclient import manager

m = manager.connect(
    host = "10.10.20.48",
    port = 830,
    username = "developer",
    password = "C1sco12345",
    hostkey_verify = False
)

netconf_reply = m.get_config(source="running")
print(netconf_reply)

print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
