import pygame
from player import Player
from ball import Ball


def main():
    pygame.init()
    width, height = 500, 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("CSRookies Breakout")
    clock = pygame.time.Clock()
    fps = 60

    # player
    player = Player(width, height)
    # ball
    ball = Ball(width, height)
    game_over = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # check for user input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.moveX(player.velocity * -1)
        if keys[pygame.K_RIGHT]:
            player.moveX(player.velocity)

        if not game_over:
            game_over = ball.move(player)

        # clearing screen
        window.fill((0, 0, 0))

        if game_over:
            font = pygame.font.SysFont("Comic Sans MS", 30)
            # apply it to text on a label
            label = font.render("Game Over!", True, (255, 255, 255))
            # put the label object on the screen at point x=100, y=100
            window.blit(label, ((width - 150) // 2, (height - 150) // 2))
        else:
            # drawing entities
            # pygame.draw.rect(window, player.color, player.get_info())
            # pygame.draw.circle(window, player.color, player.get_info())
            player.draw(window)
            ball.draw(window)

        # updates
        pygame.display.update()
        clock.tick(fps)


main()
pygame.quit()
