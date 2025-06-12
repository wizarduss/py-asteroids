import pygame
from constants import *

class PlayerLives():
	def __init__(self, x, y):
		pygame.font.init()
		self.lives = PLAYER_LIVES

		self.font = pygame.font.SysFont('Arial',16)
		self.fontX = x
		self.fontY = y

	def death(self):
		self.lives -= 1

	def displayLives(self, screen):
		text = self.font.render(f"Lives: {str(self.lives)}", True, (255, 255, 255))
		screen.blit(text, (self.fontX, self.fontY))