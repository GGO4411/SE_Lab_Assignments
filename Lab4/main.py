import pygame
from game.game_engine import GameEngine

pygame.init()

WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner - Pygame Version")

SKY = (200, 220, 240)

clock = pygame.time.Clock()
FPS = 60

engine = GameEngine(WIDTH, HEIGHT)


def main():
    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Let the game engine handle all keyboard input.
                # This allows the difficulty menu to receive 1, 2, 3 and 4.
                engine.handle_event(event)

        engine.handle_input()
        engine.update()

        # Exit if the player selected the Exit option
        if engine.should_exit():
            running = False

        SCREEN.fill(SKY)

        engine.render(SCREEN)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()