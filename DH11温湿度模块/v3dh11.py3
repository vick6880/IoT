#!/usr/bin/python3
#coding=GB2312
#多行注释说明
#coding=GB2312解决中文输入和注释的问题
#ruler可以作为全局变量来调节判断信号高电平的长度从而
#用来分辨信号是1还是0，ruler可以变动（注释掉）
import RPi.GPIO as GPIO
import time
data = []
ruler = 10

def driver():
	pin = 16
	j = 0

	GPIO.setmode(GPIO.BCM)
	time.sleep(1)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.02)
	GPIO.output(pin, GPIO.HIGH)
	GPIO.setup(pin, GPIO.IN)
	while (GPIO.input(pin) == GPIO.LOW) :
		continue
	while (GPIO.input(pin) == GPIO.HIGH) :
		continue
	while j < 40:
		k = 0
		while (GPIO.input(pin) == GPIO.LOW) :
			continue
#reading 0 or 1 via the counts of while loops
#每一位的数值信号，高电平的长短决定了数据位是0还是1。
		while (GPIO.input(pin) == GPIO.HIGH) :
			k += 1
			if (k > 100) :
				break
		if (k < ruler) :
			data.append(0)
		else:
			data.append(1)
		j += 1
#	print ("Raw data Vick1:\n", data)
	return 

def compute():
	driver()
	humidity_bit = data[0:8]
	humidity_point_bit = data[8:16]
	temperature_bit = data[16:24]
	temperature_point_bit = data[24:32]
	check_bit = data[32:40]
	humidity_point = 0
	temperature_point = 0
	check = 0
	global temperature
	global humidity
	global ruler
	humidity = 0
	temperature = 0
	output = []
	
	for i in range(8):
		humidity += humidity_bit[i] * 2 ** (7-i)
		humidity_point += humidity_point_bit[i] * 2 ** (7-i)
		temperature += temperature_bit[i] * 2 ** (7-i)
		temperature_point += temperature_point_bit[i] * 2 ** (7-i)
		check += check_bit[i] * 2 ** (7-i)

	tmp = humidity + humidity_point + temperature + temperature_point
	if (check == tmp) :
		right = 1
#		print ("温度temperature:", temperature, "*C, 湿度humidity:", humidity, "%")
#		output = [temperature, humidity]
#		print (output)
#		print(temperature)
#		print(humidity)
		return (right)
#		return [temperature, humidity]
	else:
		right = 0
		#conjust the ruler index
#		if (check > tmp) :
#			ruler -= 1
#		else :
#			ruler += 1
#		print ("温度temperature:", temperature, "*C, 湿度humidity:", humidity, "% check:", check, ", tmp:", tmp)
#		print ("Ivalid reading, perform another reading ......")
		return (right)
		

def perform():
	while compute() != 1 :
		GPIO.cleanup()
		time.sleep(0.12)
#		print ("ruler index = ", ruler)
		data = []
	return [temperature, humidity]
	
if __name__ == "__main__":
	perform()
GPIO.cleanup()
