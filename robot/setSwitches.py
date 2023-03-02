import RPi.GPIO as GPIO
 
def init():
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

def set(port, status):
    print (port)
    print (status)
    if port == 1:
        if status == 1:
            GPIO.output(5, GPIO.HIGH)
        elif status == 0:
            GPIO.output(5,GPIO.LOW)
        else:
            pass
    elif port == 2:
        if status == 1:
            GPIO.output(6, GPIO.HIGH)
        elif status == 0:
            GPIO.output(6,GPIO.LOW)
        else:
            pass
    elif port == 3:
        if status == 1:
            GPIO.output(13, GPIO.HIGH)
        elif status == 0:
            GPIO.output(13,GPIO.LOW)
        else:
            pass
    else:
        print('Wrong Command: Example--switch(3, 1)->to switch on port3')