import RPi.GPIO as GPIO
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def run():
	input = GPIO.input(4)
	if input == True:
		print("Input is true")
	else:
		print("Input is false")

if __name__ == '__main__':
	quit = False
	while quit == False:
		run()
		events = pygame.event.get()
		for event in events:
			if event.key == pygame.K_q:
				quit=True
			if event.type == QUIT:
				quit = True

	pygame.quit()
	sys.exit()
