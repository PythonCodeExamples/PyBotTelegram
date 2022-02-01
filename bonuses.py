import pygame


class Bonus:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.bonus_img = img
		self.bonuses = []
		self.mask = pygame.mask.from_surface(self.bonus_img)


	def move(self, vel):
		self.y += vel


	def draw(self, window):
		window.blit(self.bonus_img, (self.x, self.y))


	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)


	def collision(self, obj):
		return collide(self, obj)


class HealthReduce(Bonus):
	def __init__(self, x, y, img):
		super().__init__(x, y, img)


	def effect(self, player):
		player.health = 100


class CoolDoownReducer(Bonus):
	def __init__(self, x, y, img):
		super().__init__(x, y, img)


	def effect(self, player):
		player.COOLDOWN -= player.COOLDOWN * 0.15


class PlayerSpeedBooster(Bonus):
	def __init__(self, x, y, img):
		super().__init__(x, y, img)


	def effect(self, player):
		player.speed += 4