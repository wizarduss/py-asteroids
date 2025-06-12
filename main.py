import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from playerscore import *
from playerlives import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	px = SCREEN_WIDTH / 2
	py = SCREEN_HEIGHT / 2
	player = Player(px, py)
	playerScore = PlayerScore(15,15)
	playerLives = PlayerLives(15,35)
	asteroidField = AsteroidField()

	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.checkCollision(player) and player.respawnTimer <= 0:
				asteroid.kill()
				if playerLives.lives == 0:
					print("Game over!")
					sys.exit()
				playerLives.death()
				player.respawn(px, py)


			for shot in shots:
				if asteroid.checkCollision(shot):
					shot.kill()
					asteroid.split()
					playerScore.add_player_score(asteroid.radius)


		screen.fill('black')
		playerScore.displayScore(screen)
		playerLives.displayLives(screen)

		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()