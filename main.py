import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def run():
	input = GPIO.input(4)
	if input == True:
		print("Input is true")
	else:
		print("Input is false")

if __name__ == '__main__':
	run()

