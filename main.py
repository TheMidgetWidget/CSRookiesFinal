import pygame
from player import Player


def main():
    pygame.init()
    width, height = 500, 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("CSRookies Breakout")
    clock = pygame.time.Clock()
    fps = 60
    game_over = False

    # player
    player = Player(width, height)

    while not game_over:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # check for user input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.moveX(player.velocity * -1)
        if keys[pygame.K_RIGHT]:
            player.moveX(player.velocity)

        # clearing screen
        window.fill((0, 0, 0))

        # drawing entities
        pygame.draw.rect(window, player.color, player.get_info())

        # updates
        pygame.display.update()
        clock.tick(fps)


main()
pygame.quit()
