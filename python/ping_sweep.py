#!/usr/bin/python

import os
import sys

octet=sys.argv[1]
firstip=int(sys.argv[2])
lastip=int(sys.argv[3])

for ip in range(firstip,lastip+1):
    host=octet+"."+str(ip)
    response=os.system("ping -c 1 -w 1 "+host+" >/dev/null")
    if response == 0:
        print(host)

# print(octet)
# subprocess.run('ping -c 1 8.8.8.8') 
# # os.system('for ip in $(seq $2 $3) ; do')
# # os.system('ping -c 1 $1.$ip | grep -q "64 bytes" && echo $1.$ip')
# # os.system('done')

