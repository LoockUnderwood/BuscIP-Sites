#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

print('''


 ██████╗ ██╗   ██╗███████╗ ██████╗██╗██████╗               ███████╗██╗████████╗███████╗███████╗
 ██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗              ██╔════╝██║╚══██╔══╝██╔════╝██╔════╝
 ██████╔╝██║   ██║███████╗██║     ██║██████╔╝    █████╗    ███████╗██║   ██║   █████╗  ███████╗
 ██╔══██╗██║   ██║╚════██║██║     ██║██╔═══╝     ╚════╝    ╚════██║██║   ██║   ██╔══╝  ╚════██║
 ██████╔╝╚██████╔╝███████║╚██████╗██║██║                   ███████║██║   ██║   ███████╗███████║
 ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝                   ╚══════╝╚═╝   ╚═╝   ╚══════╝╚══════╝

 X--------------------------------X
 |       BY: Gabriel Santos       |                   
 X--------------------------------X
  ''')

print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

url = input('\n [!] - Edereço do site: ')

print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print('\n [!] - IP: '+socket.gethostbyname(url))

print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

time.sleep(10)








