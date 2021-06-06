import pygame

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Super Jogo 01")

def draw():
    display.fill([19, 173, 235])

gameLoop = True
if__name__ == "__main__":
    while gameLoop:
        draw()
        pygame.display.update()