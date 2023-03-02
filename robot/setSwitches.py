import RPi.GPIO as GPIO
 
def init():
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

def set(port, status):
    print (status)
    
    port = int(port)
    print (port)
    print (status == 'True')
    if port == 1:
        if status == 'True':
            GPIO.output(5, GPIO.HIGH)
        elif status == 0:
            GPIO.output(5,GPIO.LOW)
        else:
            pass
    elif port == 2:
        if status == 'True':
            GPIO.output(6, GPIO.HIGH)
        elif status == 0:
            GPIO.output(6,GPIO.LOW)
        else:
            pass
    elif port == 3:
        if status == 'True':
            GPIO.output(13, GPIO.HIGH)
        elif status == 0:
            GPIO.output(13,GPIO.LOW)
        else:
            pass
    else:
        print('Wrong Command: Example--switch(3, true)->to switch on port3')

    return 0