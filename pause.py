import pygame
from config import *
from menu import create_label
from button import *
from colormap import *

clock = pygame.time.Clock()

def pause():
	run = True
	click = False

	# Banner label
	font = pygame.font.Font('banner_font.ttf', 60)
	pause_label = font.render('Pause', 1, (216,208,208))
	pause_label_width = pause_label.get_width()

	# Lables
	continue_text  = 'CONTINUE'
	stop_text      = 'TO MAIN MENU'
	continue_label = create_label(continue_text)
	stop_label     = create_label(stop_text)

	# Buttons
	continue_button = Button(
			(WIDTH - 250) / 2,   # X coord
			HEIGHT / 2 - 50,     # Y coord
			250, 50,		     # WIDTH, HEIGHT
			button_color,	     # Color of body of the button
			text=continue_label, # Text on the button
		)

	stop_button = Button(
		(WIDTH - 300) / 2, # X coord
		HEIGHT / 2 + 50,   # Y coord
		300, 50,		   # WIDTH, HEIGHT
		button_color,	   # Color of body of the button
		text=stop_label,   # Text on the button
	)

	buttons = ButtonBlock([continue_button, stop_button])

	# New surface for alpha BG
	surf = pygame.Surface((WIDTH, HEIGHT))
	surf.set_alpha(30)
	surf.fill((0,0,0))

	while run:
		# Set FPS
		clock.tick(FPS)

		# Banner blit
		WIN.blit(pause_label, ((WIDTH-pause_label_width)/2, 100))

		# BG blit
		WIN.blit(surf, (0,0))

		# Buttons draw
		buttons.draw(WIN)

		# Display refresh
		pygame.display.update()

		# Event handling
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
						return True
					elif res == 1:
						return False
