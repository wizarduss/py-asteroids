import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shootTimer = 0
		self.respawnTimer = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		if self.respawnTimer%4 == 0 and self.respawnTimer > 0:
			width = 0
		else:
			width = 2
		pygame.draw.polygon(screen, "white", self.triangle(), width)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		self.shootTimer -= dt
		self.respawnTimer -= 1
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0,1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.shootTimer <= 0:
			shot = Shot(self.position.x, self.position.y)
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			self.shootTimer = PLAYER_SHOOT_COOLDOWN

	def respawn(self, x, y):
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.rotation = 0
		self.respawnTimer = PLAYER_RESPAWN_TIMER
