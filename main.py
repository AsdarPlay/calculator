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

buttons = ['0', ',', '=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '×', 'AC', '+/-', '%', '÷']
buttonsObject = []

mainText = ''

operatorA = 0
operatorB = 0
operand = ''
result = 0


def draw_text(screen, bounds, text):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 65)
    text_image = font.render(text, True, '#FFFFFF')
    text_rect = text_image.get_rect()
    text_rect.right = bounds[0] - 15
    text_rect.top = bounds[1] - 575
    screen.blit(text_image, text_rect)

i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObject.append(button.Button( '#2F4F4F' if i == 3 else '#000000', '#008080' if i == 3 else '#696969', btn, 179 if i == 1 else 89, 89, bounds, bounds[0] - width, bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1

fps = 60
run = True

while run:
    clock.tick(fps)
    IsClicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            IsClicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            IsClicked = False

    screen.fill('#D2691E')
    pygame.draw.rect(screen, '#000000', (2, 2, 356, 187))

    for btn in buttonsObject:
        text = btn.draw(screen, IsClicked, mainText)
        if text and text[0] == 'operand':
            if text[1] != '=':
                operand = text[1]
                if not operatorA:
                    operatorA = mainText
                    mainText = ''
                else:
                    operatorB = mainText
                    mainText = ''
            else:
                if not operatorB:
                    operatorB = mainText
                if operand == '+':
                    mainText = str(int(operatorA) + int(operatorB))
                elif operand == '-':
                    mainText = str(int(operatorA) - int(operatorB))
                elif operand == '×':
                    mainText = str(int(operatorA) * int(operatorB))
                elif operand == '÷':
                    mainText = str(int(operatorA) / int(operatorB))
                elif operand == '%':
                    mainText = str(int(operatorA) / 100)
                operand = '='
        elif text and text[0] == 'method':
            if text[1] == 'AC':
                mainText = ''
                operatorA = 0
                operatorB = 0
                operand = ''
                result = 0
            elif text[1] == '+/-':
                if len(mainText) != 0:
                    if mainText[0] != '-':
                        mainText = '-' + mainText
                    else:
                        mainText = mainText.replace('-', '')
                else:
                    mainText = ''
        elif text:
            if operand == '=':
                mainText = ''
                operatorA = 0
                operatorB = 0
                operand = ''
                result = 0
            mainText += text

    draw_text(screen, bounds, mainText)

    pygame.display.flip()

pygame.quit()