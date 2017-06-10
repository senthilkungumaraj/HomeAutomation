# Balon Coding, 29 November 2013
# Map network drive using subprocess.Popen
# Drive letter: Q
# Shared drive path: \\192.168.51.1\balon$
# Username: balon
# Password: coding

import subprocess

# initialize
driveLetter = 'Q:'
networkPath = r'\\192.168.0.11\GoFlex Home Public'
user = 'senthilkungumaraj'
password = 'Deso1986'

print('map network drive using subprocess.Popen')

# Disconnect anything on drive letter Q
#winCMD = 'NET USE ' + driveLetter + ' /delete'
#print(winCMD)
#subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)