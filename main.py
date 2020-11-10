import pygame
from player import Player
from ball import Ball
from block import Block
import random

pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("CSRookies Breakout")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 30)
large_font = pygame.font.SysFont("Comic Sans MS", 45)
btn_width, btn_height = 250, 50

# sounds
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)


def _render_btn(text, pos, mouse, run=None):
    is_hovering = 0
    if pos[0] + btn_width > mouse[0] > pos[0] and pos[1] + btn_height > mouse[1] > pos[1]:
        is_hovering = 1
        if pygame.mouse.get_pressed()[0] == 1:
            if run is not None:
                run()
            return True

    pygame.draw.rect(window, (255, 255, 255), pos + (btn_width, btn_height), is_hovering)
    label = font.render(text, True, (0, 0, 0) if is_hovering == 0 else (255, 255, 255))
    text_size = font.size(text)
    text_pos = (pos[0] + (btn_width - text_size[0]) // 2, pos[1])
    window.blit(label, text_pos)
    return False


def main_menu():
    fps = 30

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
                return

        mouse_pos = pygame.mouse.get_pos()

        # clearing screen
        window.fill((0, 0, 0))

        # Title
        title_label = large_font.render("CSRookies Breakout", True, (255, 255, 255))
        window.blit(title_label, (40, height // 4))

        # buttons
        start_pos = ((width - btn_width) // 2, height // 2)
        quit_pos = ((width - btn_width) // 2, height // 2 + 60)

        _render_btn("New Game", start_pos, mouse_pos, game)
        _render_btn("Quit", quit_pos, mouse_pos, quit)
        # start_label = font.render("New Game", True, (0, 0, 0) if is_hovering_start == 0 else (255, 255, 255))
        # quit_label = font.render("Quit", True, (0, 0, 0) if is_hovering_quit == 0 else (255, 255, 255))
        # window.blit(start_label, ((width - btn_width) // 2 + btn_width / 4.5, height // 2))
        # window.blit(quit_label, ((width - btn_width) // 2 + btn_width / 2.8, height // 2 + 60))

        # updates
        pygame.display.update()
        clock.tick(fps)


def game():
    fps = 60
    game_loop = True

    # player
    player = Player(width, height)

    # ball
    ball = Ball(width, height)
    game_over = False

    # blocks
    blocks = []
    b_width, b_height = width // 5 - 20, height // (4 * 5) - 10
    x, y = 30, 10
    for i in range(5):
        for j in range(5):
            blocks.append(Block(height, width, b_width, b_height, x, y,
                                (random.randint(20, 255), random.randint(20, 255),
                                 random.randint(20, 255))))  # block color never black
            x += 10 + b_width
        y += 10 + b_height
        x = 30

    # score
    max_score = len(blocks)

    while game_loop:
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
            ball.check_collision(blocks)
            if not game_over:
                game_over = len(blocks) == 0

        # clearing screen
        window.fill((0, 0, 0))

        if game_over:
            # Game Over text
            go_label = font.render("Game Over!", True, (255, 255, 255))
            score_label = font.render("Score: " + str(max_score - len(blocks)), True, (255, 255, 0))
            window.blit(go_label, ((width - 150) // 2, (height - 150) // 2))
            window.blit(score_label, ((width - 120) // 2, (height - 60) // 2))

            # Try Again button
            if _render_btn("Try again", ((width - btn_width) // 2, 0.75 * height), pygame.mouse.get_pos()):
                game_loop = False
                continue
        else:
            # drawing entities
            player.draw(window)
            ball.draw(window)
            for block in blocks:
                block.draw(window)

        # updates
        pygame.display.update()
        clock.tick(fps)


main_menu()
pygame.quit()
quit()
