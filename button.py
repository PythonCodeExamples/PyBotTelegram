import pygame
from colormap import *

# Creating lables for buttons
def create_label(text, text_color=(255,255,255), font='comicsans', size = 50):
	if font == 'comicsans':
		font = pygame.font.SysFont(font, size)
	else:
		font = pygame.font.Font(font, size)
	label = font.render(text, 1, text_color)
	return label

# Button class for buttons inside the game
class Button:
	def __init__(self, x, y, width, height, color, text=False, text_color=(255,255,255), border=True, border_color=(255,255,255)):
		self.x = x
		self.y = y
		self.width  = width
		self.height = height
		self.color  = color
		self.text   = text
		self.text_color = text_color
		self.border = border
		self.border_color = border_color
		self.scale_counter = 0
		self.scale_coof = 1
		self.max_scale = 4
		self.hovered = False

	# Button draw method
	def draw(self, window):
		# Button body draw
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

		# Button's label draw
		if self.text != False:
			button_center = (self.x+self.width/2, self.y+self.height/2)
			label_pos = (button_center[0]-self.text.get_width()/2, button_center[1]-self.text.get_height()/2)
			window.blit(
				self.text,
				label_pos
				)

		# Buttons's border draw
		if self.border:
			pygame.draw.rect(window, self.border_color, (self.x, self.y, self.width, self.height), 3)

		# Buttons's hoveration
		if self.hovered:
			self.on_hover()
		else:
			self.on_unhover()

	def on_hover(self):
		self.color = button_color
		if self.scale_counter != self.max_scale:
			self.x -= self.scale_coof
			self.y -= self.scale_coof
			self.width += self.scale_coof*2
			self.height += self.scale_coof*2
			self.scale_counter += 1
		
	def on_unhover(self):
		self.color = button_hover_color
		if self.scale_counter != 0:
			self.x += self.scale_coof
			self.y += self.scale_coof
			self.width -= self.scale_coof*2
			self.height -= self.scale_coof*2
			self.scale_counter -= 1

	def press(self):
		self.color = button_press_color
		if self.scale_counter != self.max_scale:
			self.x += self.scale_coof
			self.y += self.scale_coof 
			self.width -= self.scale_coof * 2
			self.height -= self.scale_coof * 2
			self.scale_counter += 1


	def set_hover(self):
		self.hovered = True
	def set_unhover(self):
		self.hovered = False


class ButtonBlock:
	def __init__(self, buttons):
		self.buttons = buttons
		self.buttons[0].set_hover()
		self.active_button = 0
		self.max_button = len(buttons) - 1

	def move_up(self):
		if (self.active_button > 0):
			self.buttons[self.active_button].set_unhover()
			self.active_button -= 1
			self.buttons[self.active_button].set_hover()


	def move_down(self):
		if (self.active_button < self.max_button):
			self.buttons[self.active_button].set_unhover()
			self.active_button += 1
			self.buttons[self.active_button].set_hover()


	def click(self):
		self.buttons[self.active_button].press()
		return self.active_button


	def draw(self, window):
		for button in self.buttons:
			button.draw(window)