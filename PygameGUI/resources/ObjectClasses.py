import pygame
import numpy as np
class ClickableInstance():
    def __init__(self,screen,pos,width,hight,text):
        self.screen= screen
        self.BorderThickness=3
        self.pos = [x+self.BorderThickness for x in pos]
        self.hight = hight-self.BorderThickness
        self.width= width-self.BorderThickness*2
        self.text = text
        self.font = pygame.font.SysFont("Arial", 50)
        self.FieldColor = pygame.Color('white')
        self.UniqueAction=None
        self.MaxChar=2
        self.edible=False
        self.active = False
        self.input_box = pygame.Rect(self.pos,(self.width,self.hight))
        self.Border=Border(self)
        pygame.draw.rect(self.screen, self.FieldColor, self.input_box, 0)
        self.text_render = blit_text(self.screen,self.text,self.pos,self.font)
    
        #screen.blit(self.text_render, (self.input_box.x+5, self.input_box.y+5))

    def update(self):

        if self.active ==True:
            self.Border.Color= pygame.Color('red')
        else:
            self.Border.Color= pygame.Color('black')
        self.Border.update() 
        pygame.draw.rect(self.screen, self.FieldColor, self.input_box, 0)
        self.text_render = blit_text(self.screen,self.text,self.pos,self.font)
        #self.screen.blit(self.text_render, (self.input_box.x+5, self.input_box.y+5))
    def checkCollision(self,ClickPosition):
        if self.input_box.collidepoint(ClickPosition) and not self.active:
            self.active= True
            self.update()
            return self
        else: 
            self.active = False
            self.update()
            return  None
    def isActive(self):
        if self.active:
            return self
        else:
            return None
    
     
        
    
class TextField(ClickableInstance):
    def __init__(self,screen,pos,width,hight,text):
        ClickableInstance.__init__(self,screen, pos, width, hight, text)
        self.edible=True
    def Backspace(self):
        self.text=self.text[:-1]

class Border():
    def __init__(self,Object):
        
        self.screen = Object.screen
        self.Thickness=Object.BorderThickness
        #self.Pos = [x-self.Thickness for x in Object.pos]
        self.Pos = [x-self.Thickness for x in Object.pos]
        self.Width = Object.width + self.Thickness*2
        self.Hight = Object.hight + self.Thickness*2
        self.Color = pygame.Color('black')
        self.Border =  pygame.Rect(self.Pos,(self.Width,self.Hight))
        pygame.draw.rect(Object.screen, self.Color, self.Border, 0)
    
    def update(self):
        pygame.draw.rect(self.screen, self.Color, self.Border, 0)

class Line():
    def __init__(self,screen,pos,width,hight,Data):
        self.pos = pos 
        self.totalWidth= width
        self.ratios=[5,2,3]
        self.hight= hight
        self.width = self.totalWidth*(self.ratios/np.sum(self.ratios))
        
        self.Data = Data 
        self.Field=[]
        self.Field.append(TextField(screen, (pos[0],pos[1]), self.width[0], self.hight, str(Data[0])))

        self.Field.append(TextField(screen, (pos[0]+self.width[0],pos[1]), self.width[1], self.hight, str(Data[1])))

        self.Field.append(TextField(screen, (pos[0]+self.width[0]+self.width[1],pos[1]), self.width[2], self.hight, ''))
        self.Field[2].text='Remove \n Line'
        self.Field[2].font = pygame.font.SysFont("Arial", 20)
        self.Field[2].update()

    def checkCollision(self,collidepoint):
        z = None
        for x in self.Field:
            y = x.checkCollision(collidepoint)
            if  y != None:
                z = y
        
        return z
    def isActive(self):
        for x in self.Field:
            if x.active:
                return x
            else:
                pass
        return None
    
                
                



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def draw_Lines(VariableArray,ClickableInstances, screen):
    Lines=[]
    for Data in VariableArray:
        Lines.append(New_Line((0,0),screen,300,50,Lines,Data))
        ClickableInstances.append(Lines[-1])
    return Lines
def New_Line(Original_Pos,screen,width,hight,Lines,Data):

    if len(Lines) ==0 or Lines[0]==None:
        pos=Original_Pos
        newLine=Line(screen,pos,width,hight,Data)
        return newLine
    else:
        
        pos = [(Original_Pos[0]),(Lines[-1].Field[0].pos[1] + hight)]
        newLine=Line(screen,pos,width,hight,Data)
        return newLine