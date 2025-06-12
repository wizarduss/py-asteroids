import pygame
from constants import *

class PlayerScore():
	def __init__(self, x, y):
		pygame.font.init()
		self.score = 0

		self.font = pygame.font.SysFont('Arial',32)
		self.fontX = x
		self.fontY = y

	def displayScore(self, screen):
		text = self.font.render(f"Current score: {str(self.score)}", True, (255, 255, 255))
		screen.blit(text, (self.fontX, self.fontY))

	def add_player_score(self, radius):
		if radius == ASTEROID_MAX_RADIUS:
			self.score += 5
		if radius < ASTEROID_MAX_RADIUS and radius > ASTEROID_MIN_RADIUS:
			self.score += 15
		if radius == ASTEROID_MIN_RADIUS:
			self.score += 30