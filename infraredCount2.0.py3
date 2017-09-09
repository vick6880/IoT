#!/usr/bin/python3
#coding=UTF-8
import RPi.GPIO as GPIO
import time
pin = 20
GPIO.setmode(GPIO.BCM)

def watch() :
	counter = 0
	
	GPIO.setup(pin, GPIO.IN)
	while True :
		if (GPIO.input(pin) == GPIO.HIGH) :
			counter += 1
			print(counter)
			time.sleep(10) 
		else :
			time.sleep(1)

if __name__ == "__main__" :
	watch()