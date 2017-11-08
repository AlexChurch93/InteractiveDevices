import serial
import subprocess
#from subprocess import Popen, PIPE

ser = serial.Serial("COM4", 9600)
while True:
    reading = ser.readline().decode("utf-8")

    if int(reading) <= 10 and int(reading) >= 0:
        print ("in range")

        print (subprocess.check_output('git add .', shell=True))
        print(subprocess.check_output('git commit -m \"Through Python Commit\"', shell=True))
        print(subprocess.check_output('git push', shell=True))
        #print(Popen('dir',shell=True))
        break
    else:
        print("out of range")
