import pygame

from graphical_object import GraphicalButton

def boolean_popup(message: str, my_pygame_display):

    font = pygame.font.Font('arial.ttf', 25)
    clock = pygame.time.Clock()
    # doublons de test_pygame
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    my_pygame_display.fill(WHITE)
    pygame.display.set_caption(message)
    
    text = font.render(message, True, BLACK)
    my_pygame_display.blit(text, [150, 30])

    yes_button = GraphicalButton(250, 100, font.render, "Yes", font.size).\
        drawing(my_pygame_display)
    no_button = GraphicalButton(370, 100, font.render, "No", font.size).\
        drawing(my_pygame_display)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                if yes_button.collidepoint(event.pos):
                    return True
                if no_button.collidepoint(event.pos):
                    return False
            elif event.type == pygame.QUIT:
                return False
        clock.tick(60)