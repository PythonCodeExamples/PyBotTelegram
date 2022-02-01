#!/usr/bin/python3

'''
Space Wars
by VladOS and Pomidorka

I hope you'll enjoy with it.
Have a nice game!

© 2020
'''

# Main imports
import pygame 						 # Graphic lib
from random import randrange, choice # Some randomise
from os import path

# Custom classes
from textures import *
from ship import *
from bonuses import *
from laser import *
from config import *
from menu import main_menu
from pause import *

pygame.font.init()

# Main game function
restart_flag = 1

# Sprites path
pack = "space"

def main(asset):
	global pack

	run = True
	lives = 5
	level = 0 # Start level
	start_move = True

	# Textures
	textures = Textures(path.join("assets", asset))

	# Fonts
	main_font = pygame.font.SysFont('comicsans', 50)
	lost_font = pygame.font.SysFont('comicsans', 70)

	# Texts
	lost_label = lost_font.render('You Lost!', 1, (255,255,255))

	enemies = []
	wave_length = 5 # Eniemies per level (1 lvl = 5, 2 lvl = 10)
	
	bonuses = []
	bonus_vel = 3	 # Bonuses speed

	player = Player(int(WIDTH/2), int(HEIGHT - 50), textures.get_player(), speed = 5) # Player spawn

	lost = False
	lost_count = 0

	clock = pygame.time.Clock()


	def redraw_window():
		# Background drawing
		WIN.blit(textures.BG, (0, 0))

		# Lables
		lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

		# All enemies drawing
		for enemy in enemies:
			enemy.draw(WIN)

		# All bonuses drawing
		for bonus in bonuses:
			bonus.draw(WIN)

		# Draw main player
		player.draw(WIN)

		# Draw lose condition
		if lost:
			WIN.blit(lost_label, ((WIDTH-lost_label.get_width())/2, 350))
		
		# Draw text
		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

		# Display refresh
		pygame.display.update()

		
	menu_res = main_menu(textures)
	if menu_res == 0:
		pass
	else:
		pack = menu_res
		return menu_res

	while run:
		clock.tick(FPS)

		# Player start movement
		if player.y >= 500 and start_move:
			player.y -= 7
			continue
		else:
			start_move = False

		# Lose condition
		if lives <= 0 or player.health <= 0:
			lost = True
			lost_count += 1

		# If lose cond = True
		if lost:
			if lost_count > FPS * 3:
				break
			else:
				continue

		# If all enemies killed
		if len(enemies) == 0:
			level += 1		 # Level counter encrement
			wave_length +=  5 # Enemies on next level

			# Enemies spawn
			for i in range(wave_length):
				enemy = Enemy(
					randrange(50, WIDTH - 100),
					(-i*100)-300,
					textures.get_enemy(),
					speed=randrange(1, 3)
					)

				enemies.append(enemy)

			# Bonuses spawn
			bonuses = []
			bonus_hp = HealthReduce(randrange(50, WIDTH - 100), randrange(-1500, -100), textures.HEALTH_BOTTLE)
			bonus_cd = CoolDoownReducer(randrange(50, WIDTH - 100), randrange(-1500, -100), textures.COOLDOWN_REDUCER)
			bonuses.append(bonus_cd)
			bonuses.append(bonus_hp)

		# Game close condition
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()


		# Key handling
		# Move keys
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - player.speed > 0: # left
			player.move(-1, 0)

		if keys[pygame.K_RIGHT] and player.x + player.get_width() + player.speed < WIDTH: # right
			player.move(1, 0)

		if keys[pygame.K_UP] and player.y - player.speed > 0: # up
			player.move(0, -1)

		if keys[pygame.K_DOWN] and player.y + player.get_height() + 15 + player.speed < HEIGHT: # down
			player.move(0, 1)

		# Shoot key
		if keys[pygame.K_SPACE]:
			player.shoot()

		# Pause key
		if keys[pygame.K_ESCAPE]:
			run = pause()

		# Enemy interactive
		for enemy in enemies[:]:
			enemy.move()						 # Enemies movement
			enemy.move_lasers(player) # Enemies's lasers move

			if randrange(0, 4*60) == 1:			 # Random shooting 25%
				enemy.shoot()

			if collide(enemy, player): # Is enemy ship collided player ship
				player.health -= 10
				enemies.remove(enemy)

			elif enemy.y + enemy.get_height() > HEIGHT: # Is enemy outside the screen
				lives -= 1
				enemies.remove(enemy)

		# Bonuses interactive
		for bonus in bonuses:
			bonus.move(bonus_vel)	   # Bonuses movement

			if collide(bonus, player): # Collide with player
				bonus.effect(player)
				bonuses.remove(bonus)

			if bonus.y >= HEIGHT:
				bonuses.remove(bonus)




		player.move_lasers(enemies) # Player lasers move

		# Refresh window
		redraw_window() 

# Run main cycle condition	
while restart_flag:
	main(pack)
