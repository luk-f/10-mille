import pygame

def boolean_popup(message: str):

    pygame.init()

    # doublons de test_pygame
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    popup_display = pygame.display.set_mode((128, 128))
    popup_display.fill(WHITE)
    popup_display.set_caption(message)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                print(event)
                # TODO test yes or not
        clock.tick(60)

    pygame.quit()