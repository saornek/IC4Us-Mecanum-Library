import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Motor:
        in1 = ""
        in2 = ""
        pwm = ""
        standbyPin = ""

        #Defaults
        hertz = 1000
        reverse = False #Reverse flips the direction of the motor

        #Constructor
        def __init__(self, in1, in2, pwm, standbyPin, reverse):
                self.in1 = in1
                self.in2 = in2
                self.pwm = pwm
                self.standbyPin = standbyPin
                self.reverse = reverse

                GPIO.setup(in1,GPIO.OUT)
                GPIO.setup(in2,GPIO.OUT)
                GPIO.setup(pwm,GPIO.OUT)
                GPIO.setup(standbyPin,GPIO.OUT)
                GPIO.output(standbyPin,GPIO.HIGH)
                self.p = GPIO.PWM(pwm, self.hertz)
                self.p.start(0)

        def forward(self, speed):
            if speed > 0:
                dutyCycle = speed
                if(self.reverse):
                        speed = speed * -1
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
            else:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(dutyCycle)

        def backward(self, speed):
            if speed > 0:
                dutyCycle = speed
                if(self.reverse):
                        speed = speed * -1
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
            else:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(dutyCycle)

        def brake(self):
            self.p.ChangeDutyCycle(0)
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.HIGH)

        def standby(self, value):
            self.p.ChangeDutyCycle(0)
            GPIO.output(self.standbyPin,value)
