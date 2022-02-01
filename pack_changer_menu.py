import pygame
from config import *
from button import *

BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50

BUTTON_X = (WIDTH - BUTTON_WIDTH)//2
HALF_HEIGHT = HEIGHT // 2

def pack_changer(BG):
	run = True
	clock = pygame.time.Clock()


	space_label = create_label("SPACE", font='banner_font.ttf')
	ocean_label = create_label("OCEAN", font='banner_font.ttf')


	space_button = Button(
		BUTTON_X,
		HALF_HEIGHT-50,
		BUTTON_WIDTH, BUTTON_HEIGHT,
		button_color,
		text = space_label,
	)

	ocean_button = Button(
		BUTTON_X,
		HALF_HEIGHT+50,
		BUTTON_WIDTH, BUTTON_HEIGHT,
		button_color,
		text = ocean_label,
	)

	buttons = ButtonBlock([space_button, ocean_button])

	while run:
		clock.tick(FPS)

		# BG blitings
		WIN.blit(BG, (0,0))

		# Button drawing
		buttons.draw(WIN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Close window
				pygame.quit()

			if event.type == pygame.KEYDOWN: # Click
				if event.key == pygame.K_UP:
					buttons.move_up()

				if event.key == pygame.K_DOWN:
					buttons.move_down()

				if event.key == pygame.K_RETURN:
					res = buttons.click()
					if res == 0:
						return "space"
					elif res == 1:
						return "ocean"


		# Display refresh
		pygame.display.update()
