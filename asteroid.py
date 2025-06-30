import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.shape = self._generate_asteroid()

	def _generate_asteroid(self):
		irregularity = 0.8
		num_points = int(self.radius / ASTEROID_MIN_RADIUS)*5

		points = []
		angle_step = 2 * math.pi / num_points

		for i in range(num_points):
			angle = i * angle_step
			# Vary the radius randomly to make the shape jagged
			random_radius = self.radius * (1 + irregularity * (random.uniform(-1, 1)))
			x = math.cos(angle) * random_radius
			y = math.sin(angle) * random_radius
			points.append(pygame.Vector2(x, y))

		return points

	def draw(self, screen):
		#pygame.draw.circle(screen, 'white', self.position,self.radius, width=2)
		angle = self.velocity.angle_to(pygame.Vector2(1, 0))

		# Rotate and translate the shape
		rotated_shape = [p.rotate(angle) for p in self.shape]
		translated_points = [p + self.position for p in rotated_shape]
		pygame.draw.polygon(screen, 'white', translated_points, width=2)

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