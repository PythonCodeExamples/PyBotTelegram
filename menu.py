import pygame
from time import sleep
from config import *
from pack_changer_menu import pack_changer
from button import *
from colormap import *

clock = pygame.time.Clock()

def main_menu(textures):
	# Banner
	banner_font = pygame.font.Font('banner_font.ttf', 80)
	banner_first = banner_font.render("Space", 1, (128,128,128))
	banner_second = banner_font.render("War", 1, (220,220,220))
	banner_first_width = banner_first.get_width()
	banner_second_width = banner_second.get_width()
	banner_second_height = banner_second.get_height()
	banner_width = banner_first_width + banner_second_width
	banner_first_coord = [0-banner_first_width, 20] 
	banner_second_coord = [WIDTH/2+48, 0-banner_second_height]

	# Createing lables of buttons
	start_text = 'PLAY'
	change_pack_text = 'PACK'
	exit_text = 'EXIT'
	start_label = create_label(start_text)
	change_pack_label = create_label(change_pack_text)
	exit_label = create_label(exit_text)

	run = True # Run main menu cycle condition
	click = False # Click mouse condition

	# Movement on button const
	scale = 2
	scale_time_counter = 2
	counter = 0

	# Buttons
	run_button = Button(
		WIDTH/2-75,
		HEIGHT/2-125,
		150, 50,
		button_color,
		text=start_label,
		border_color=(0,0,0)
		)

	change_pack_button = Button(
		WIDTH/2-75,
		HEIGHT/2-25,
		150, 50,
		button_color,
		text=change_pack_label,
		border_color=(0,0,0)
		)

	exit_button = Button(
		WIDTH/2-75,
		HEIGHT/2+75,
		150, 50,
		button_color,
		text=exit_label,
		border_color=(0,0,0)
		)

	buttons = ButtonBlock([run_button, change_pack_button, exit_button])

	while run:
		clock.tick(FPS)

		# Blits
		WIN.blit(textures.MENU_BG, (0,0))

		# Banner movement
		if banner_first_coord[0] != int((WIDTH-banner_width)/2):
			banner_first_coord[0] += 3
		if banner_second_coord[1] != 20:
			banner_second_coord[1] += 1
		WIN.blit(banner_first, banner_first_coord)
		WIN.blit(banner_second, banner_second_coord)

		# Button's draws
		buttons.draw(WIN)

		pygame.display.update()

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Close window
				pygame.quit()

			if event.type == pygame.KEYDOWN: # Button click
				if event.key == pygame.K_UP:
					buttons.move_up()

				if event.key == pygame.K_DOWN:
					buttons.move_down()

				if event.key == pygame.K_RETURN:
					res = buttons.click()
					if res == 0:
						return 0
					elif res == 1:
						return pack_changer(textures.BG)
					elif res == 2:
						pygame.quit()
