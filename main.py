import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("CSRookies Breakout")
    clock = pygame.time.Clock()
    fps = 60
    game_over = False

    while not game_over:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        clock.tick(fps)


main()
pygame.quit()
