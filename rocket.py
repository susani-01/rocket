import pygame

class Rocket:
	"""A class to manage the rocket"""

	def __init__(self,rg_game):
		"""Initialize the rocket and set its starting position"""
		self.screen = rg_game.screen
		self.settings = rg_game.settings
		self.screen_rect = rg_game.screen.get_rect()


		#Load the image and get its rect
		self.image = pygame.image.load("rocket1.png")
		self.rect = self.image.get_rect()

		#start each new rocket at the center of the screen
		self.rect.center = self.screen_rect.center

		#store decimal value for the rocket
		self.x = float(self.rect.x)
		self.y = float(self.rect.y) 

		#movement flag.
		self.moving_right,self.moving_left = False,False
		self.moving_up,self.moving_down = False,False

	def update(self):
		"""Update the rocket's position based on the movement flags."""
		if self.moving_right  and self.rect.right < self.screen_rect.right:
			self.x += self.settings.rocket_speed
		if self.moving_left and self.rect.left > 0:
			self.x -=  self.settings.rocket_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.rocket_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.rocket_speed

		#update rect object from position attribute'
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the rocket at its current location."""
		self.screen.blit(self.image,self.rect)