import pygame
import button
pygame.init()

def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)

bounds = (360, 640)
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

buttons = ['0', ',', '=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '×', 'C', '◄', '%', '÷']
buttonsObject = []

i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObject.append(button.Button( '#483D8B' if i == 3 else '#000000', '#6A5ACD' if i == 3 else '#696969', btn, 179 if i == 1 else 89, 89, bounds, bounds[0] - width, bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1

fps = 60
run = True

while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('#FF8C00')
    pygame.draw.rect(screen, '#000000', (0, 0, 400, 189))
    pygame.draw.rect(screen, '#AFEEEE', (20, 15,320, 155))

    for btn in buttonsObject:
        btn.draw(screen)

    pygame.display.flip()

pygame.quit()