#!/usr/bin/env python

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitions:
left_pwmPin = 12
left_Pin1 = 17
left_Pin2 = 27

right_pwmPin = 18
right_Pin1 = 14
right_Pin2 = 15

speed = 80
freq = 500

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_Pin1, GPIO.OUT)
GPIO.setup(left_Pin2, GPIO.OUT)
GPIO.setup(right_Pin1, GPIO.OUT)
GPIO.setup(right_Pin2, GPIO.OUT)

GPIO.setup(left_pwmPin, GPIO.OUT)
GPIO.setup(right_pwmPin, GPIO.OUT)

pwm1 = GPIO.PWM(left_pwmPin, freq)
pwm2 = GPIO.PWM(right_pwmPin, freq)

GPIO.output(left_Pin1, GPIO.LOW)
GPIO.output(right_Pin1, GPIO.LOW)
GPIO.output(left_Pin2, GPIO.HIGH)
GPIO.output(right_Pin2, GPIO.HIGH)

pwm1.start(0)
pwm2.start(0)

print("Press CTRL+C to exit!")

try:
	while 1:
		pwm1.ChangeDutyCycle(speed)
                pwm2.ChangeDutyCycle(speed)

except KeyboardInterrupt:
	pwm1.stop()
        pwm2.stop()
	GPIO.cleanup()

