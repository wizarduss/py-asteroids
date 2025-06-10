import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, 'white', self.position,self.radius, width=2)

	def update(self, dt):
		self.position += (self.velocity*dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20,50)
		velocityOne = self.velocity.rotate(angle)
		velocityTwo = self.velocity.rotate(-angle)
		newRadius = self.radius - ASTEROID_MIN_RADIUS

		asteroidOne = Asteroid(self.position.x, self.position.y, newRadius)
		asteroidOne.velocity = velocityOne * 1.2
		asteroidTwo = Asteroid(self.position.x, self.position.y, newRadius)
		asteroidTwo.velocity = velocityTwo * 1.2