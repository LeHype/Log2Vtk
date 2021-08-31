import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def InputBox(screen,pos, text):

    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    color = pygame.Color('white')
    input_box = pygame.Rect(pos,(100,100))
    Box = pygame.draw.rect(screen, color, input_box, 0)
    
    screen.blit(text_render, (input_box.x+5, input_box.y+5))
    return input_box

class InputBox():
    def __init__(self,screen,pos,text):
        self.screen= screen
        self.pos = pos
        self.text = text
        self.font = pygame.font.SysFont("Arial", 50)
        self.text_render = self.font.render(text, 1, (255, 0, 0))
        self.color = pygame.Color('white')
        self.input_box = pygame.Rect(self.pos,(100,100))
        self.active = False
        pygame.draw.rect(self.screen, self.color, self.input_box, 0)
    
        screen.blit(self.text_render, (self.input_box.x+5, self.input_box.y+5))
        

def start():
    print("Ok, let's go")

def menu():
    """ This is the menu that waits you to click the s key to start """
    b1 = button(screen, (400, 300), "Quit")
    b2 = button(screen, (500, 300), "Start")
    input_box = InputBox(screen, (100,100), 'Text')
    done= False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
        # If the user clicked on the input_box rect.
                if input_box.input_box.collidepoint(event.pos):
            # Toggle the active variable.
                    input_box.active = not input_box.active
                else:
                    input_box.active = False
        # Change the current color of the input box.
                #color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(input_box.text)
                            input_box.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_box.text = input_box.text[:-1]
                else:
                    input_box.text += event.unicode
        pygame.display.update()
    pygame.quit()

menu()
