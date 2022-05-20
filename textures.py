import pygame
import os
from config import *
from random import choice


class Textures:
	def __init__(self, path):
		# Main player ship
		self.YELLOW_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "1.png")), (62, 62))

		# Imgaes loading
		self.RED_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "2.png")), (52, 52))
		self.GREEN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "3.png")), (52, 52))
		self.BLUE_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "4.png")), (52, 52))
		self.ORANGE_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "5.png")), (52, 52))
		self.BROWN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, "6.png")), (52, 52))

		# Lasers
		BULLETS_DEMENSIONS = (25, 25)

		self.YELLOW_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "1_las.png")), BULLETS_DEMENSIONS)
		self.RED_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "2_las.png")), BULLETS_DEMENSIONS)
		self.GREEN_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "3_las.png")), BULLETS_DEMENSIONS)
		self.BLUE_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "4_las.png")), BULLETS_DEMENSIONS)
		self.ORANGE_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "5_las.png")), BULLETS_DEMENSIONS)
		self.BROWN_LASER = pygame.transform.scale(pygame.image.load(os.path.join(path, "6_las.png")), BULLETS_DEMENSIONS)

		# Bonuses img
		self.HEALTH_BOTTLE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space", "7.png")), (50, 50))
		self.COOLDOWN_REDUCER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space", "8.png")), (50, 50))

		# Background
		self.BG = pygame.transform.scale(pygame.image.load(os.path.join(path, "main_bg.jpg")), (WIDTH, HEIGHT))
		self.MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space", "menu_bg.jpg")), (WIDTH, HEIGHT))


	def get_player(self):
		return [self.YELLOW_SPACE_SHIP, self.YELLOW_LASER]


	def get_enemy(self):
		return choice([
					[self.RED_SPACE_SHIP, self.RED_LASER],
				  	[self.GREEN_SPACE_SHIP, self.GREEN_LASER],
				 	[self.BLUE_SPACE_SHIP, self.BLUE_LASER],
				  	[self.ORANGE_SPACE_SHIP, self.ORANGE_LASER],
				  	[self.BROWN_SPACE_SHIP, self.BROWN_LASER]
			 	])
