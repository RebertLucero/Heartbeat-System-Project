from pulsesensor import Pulsesensor
import time, os
import serial
import RPi.GPIO as GPIO
import yagmail

p = Pulsesensor()
p.startAsyncBPM()

yag = yagmail.SMTP('heartratesensor69@gmail.com', 'raspberry123456')
contents = ("Name: ", f"Age: 30", "Patient is experiencing slow heart beat (Bradycardia). \r\nBPM: {r}".format(r = bpmlow))
contents2 = ("Name: ", f"Age: 30", "Patient is experiencing rapid heart beat (Tachycardia). \r\nBPM: {r}".format(r = bpmHigh))


def sendEmail():
    yag.send('b@gmail.com', 'Heart Rate Sensor', Contents)
    
def sendEmail2():
    yag.send('b@gmail.com', 'Heart Rate Sensor', Contents2)
    
def sendSMS():
    GPIO.setmode(GPIO.BOARD)
    port = serial.Serial("/dev/ttySO", baudrate=9600, timeout=1)
    port.write(b'AT+CMGS="091833748369"'+b'\r\n')
    rcv = port.read(10)
    print(rcv)
    time.sleep(1)
    port.write(b'Name: '+b'r\n')
    port.write(b'Age: 30 '+b'r\n')
    port.write(b'Patient is experiencing slow heart beat (Bradycardia). \r\nBPM: '+b'')
    port.write(str(bpmLow).encode('utf-8'))
    rcv = port.read(10)
    print (rcv)
    
    for i in range(10):
        rcv = port.read(10)
        print (rcv)

def sendSMS2():
    GPIO.setmode(GPIO.BOARD)
    port = serial.Serial("/dev/ttySO", baudrate=9600, timeout=1)
    port.write(b'AT+CMGS="091833748369"'+b'\r\n')
    rcv = port.read(10)
    print(rcv)
    time.sleep(1)
    port.write(b'Name: '+b'r\n')
    port.write(b'Age: 30 '+b'r\n')
    port.write(b'Patient is experiencing rapid heart beat (Tachycardiacardia). \r\nBPM: '+b'')
    port.write(str(bpmHigh).encode('utf-8'))
    rcv = port.read(10)
    print (rcv)
    port.write(b"\x1A")
    
    for i in range(10):
        rcv = port.read(10)
        print(rcv)

try:
    while True:
        
        bpm p.BPM
        
        if bpm >=1 and bpm <= 45:
            print("Place the patient's finger properly")
            
        elif bpm >=46 and bpm <=54:
            sendEmail()
            sendSMS()
            break
        
        elif bpm >=55 and bpm <= 118:
            print("BPM: %d" % bpm)
            
        elif bpm >= 119 and bpm <= 130:
            sendEmail2()
            sendSMS2()
            break
        
        else
            print("Place the patient's finger properly")
        time.sleep(1)
except:
    p.stopAsyncBPM()
            


    
    