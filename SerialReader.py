import serial

ser = serial.Serial("COM4", 9600)
while True:
    reading = ser.readline().decode("utf-8")

    if int(reading) <= 10 and int(reading) >= 0:
        print ("in range")
    else:
        print("out of range")
