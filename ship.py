'''
Module for all ships
Enemy ships, Main Hero ship
'''
from laser import *
from config import *

# Base Class for ships.
class Ship:
	COOLDOWN = 30 # Shooting cool down (0.5 sec for 60 fps)

	# Base params
	def __init__(self, x, y, speed, health):
		self.x = x
		self.y = y
		self.speed = speed
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		for laser in self.lasers:
			laser.draw(window)
		window.blit(self.ship_img, (self.x, self.y))

	def move_lasers(self, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move()
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	def cooldown(self):
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x+26, self.y, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()


class Player(Ship):
	def __init__(self, x, y, sprite, speed = 5, health=100):
		super().__init__(x, y, speed, health)
		self.ship_img = sprite[0]
		self.laser_img = sprite[1]
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health


	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x+18, self.y+18, self.laser_img, speed=-4)
			self.lasers.append(laser)
			self.cool_down_counter = 1


	def move_lasers(self, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move()
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						if laser in self.lasers:
							self.lasers.remove(laser)


	def move(self, x, y):
		if (x == -1):
			self.x -= self.speed
		if (x == 1):
			self.x += self.speed
		if (y == -1):
			self.y -= self.speed
		if (y == 1):
			self.y += self.speed


	def draw(self, window):
		super().draw(window)
		self.__draw_healthbar(window)

	def __draw_healthbar(self, window):
		pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 5, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 5, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
	def __init__(self, x, y, sprite, speed = 2, health=100):
		super().__init__(x, y, speed, health)
		self.ship_img, self.laser_img = sprite[0], sprite[1]
		self.mask = pygame.mask.from_surface(self.ship_img)


	def move(self):
		self.y += self.speed 


	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x+15, self.y+15, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1
