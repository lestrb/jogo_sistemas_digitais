import pygame
from core import constants
from core.game_manager import StateManager
from screens.title_screen import TitleScreen, DummyScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode(constants.RESOLUTION)
    clock = pygame.time.Clock()

    manager = StateManager()
    manager.push(TitleScreen())

    running = True
    while running:
        dt = clock.tick(60) / 1000  # delta time em segundos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Exemplo: troca de telas ao apertar espaço
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    manager.switch_to(DummyScreen())

        manager.update(dt)
        manager.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()