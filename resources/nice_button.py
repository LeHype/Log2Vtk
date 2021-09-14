import pygame

pygame.init()
screen = pygame.display.set_mode((700, 400))
screen.fill('blue')

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
    def OnClick():
        pass
    return screen.blit(text_render, (x, y))

def InputBox(screen,pos, text):

    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    color = pygame.Color('white')
    input_box = pygame.Rect(pos,(100,100))
    Box = pygame.draw.rect(screen, color, input_box, 0)
    
    screen.blit(text_render, (input_box.x+5, input_box.y+5))
    return input_box
def RemoveEntry(ClickableInstances,RemoveID):
    ClickableInstances.remove(RemoveID)
def AddEntry(ClickableInstances, yPos):
    print(yPos)
    yPos=yPos+60
    ClickableInstances.append(InputBox(screen, (100,yPos),70,50, '*',1,True))
    ClickableInstances.append(InputBox(screen, (180,yPos),70,50, '*',2,True))
class InputBox():
    def __init__(self,screen,pos,width,hight,text,MaxChar,edible):
        self.screen= screen
        self.BorderThickness=4
        self.pos = pos
        self.hight = hight
        self.width= width
        self.BorderPos = [x-self.BorderThickness for x in pos]
        self.BorderWidth = self.width+self.BorderThickness*2
        self.BorderHight = self.hight+self.BorderThickness*2
        self.text = text
        self.font = pygame.font.SysFont("Arial", 50)
        self.text_render = self.font.render(text, 1, (0, 0, 255))
        self.FieldColor = pygame.Color('white')
        self.BorderColor = pygame.Color('black')
        self.MaxChar=MaxChar
        self.edible=edible
        self.active = False
        self.input_box = pygame.Rect(self.pos,(self.width,self.hight))
        self.border =  pygame.Rect(self.BorderPos,(self.BorderWidth,self.BorderHight))
        pygame.draw.rect(self.screen, self.BorderColor, self.border, 0)
        pygame.draw.rect(self.screen, self.FieldColor, self.input_box, 0)
    
        screen.blit(self.text_render, (self.input_box.x+5, self.input_box.y+5))
    def update(self):

        if self.active ==True:
            self.BorderColor= pygame.Color('red')
        else:
            self.BorderColor= pygame.Color('black')
        self.text_render = self.font.render(self.text, 1, (0, 0, 255))
        pygame.draw.rect(self.screen, self.BorderColor, self.border, 0)
        pygame.draw.rect(self.screen, self.FieldColor, self.input_box, 0)
    
        screen.blit(self.text_render, (self.input_box.x+5, self.input_box.y+5))

def start():
    print("Ok, let's go")

def menu(VariableArray):
    """ This is the menu that waits you to click the s key to start """
    ClickableInstances=[]
    ClickableInstances.append(InputBox(screen, (300,300), 240, 50, 'Add Entry',0,False))
    ClickableInstances.append(InputBox(screen, (550,300), 120, 50, 'Start',0,False))
    for i in range(len(VariableArray)):

        ClickableInstances.append(InputBox(screen, (100,50+(i*60)),70,50, str(VariableArray[i][0]),1,True))
        ClickableInstances.append(InputBox(screen, (180,50+(i*60)),70,50, str(VariableArray[i][1]),2,True))
    done= False

    ActiveObjectId=None
    while not done:
        #Event Handling
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
        # If the user clicked on the input_box rect.
                for i in range(len(ClickableInstances)):

                    if ClickableInstances[i].input_box.collidepoint(event.pos):
            # Toggle the active variable.
                        ClickableInstances[i].active = not ClickableInstances[i].active
                        ActiveObjectId = i
                    else:
                        ClickableInstances[i].active = False

                    ClickableInstances[i].update()
        # Change the current color of the input box.
                #color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    
                    if ActiveObjectId==0:
                        AddEntry(ClickableInstances,ClickableInstances[-1].pos[1])
                elif event.key == pygame.K_BACKSPACE and ClickableInstances[ActiveObjectId].edible:
                    ClickableInstances[ActiveObjectId].text = ClickableInstances[ActiveObjectId].text[:-1]
                elif len(ClickableInstances[ActiveObjectId].text)< ClickableInstances[ActiveObjectId].MaxChar and ClickableInstances[ActiveObjectId].edible:
                    ClickableInstances[ActiveObjectId].text += event.unicode
                
                ClickableInstances[ActiveObjectId].update()
        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    DummyArray = [['U',3],['S',4],['T',1]]
    menu(DummyArray)
