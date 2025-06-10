import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	px = SCREEN_WIDTH / 2
	py = SCREEN_HEIGHT / 2
	player = Player(px, py)
	asteroidField = AsteroidField()

	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		screen.fill('black')
		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()