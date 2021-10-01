import pygame
import os
from resources.ObjectClasses import ClickableInstance, TextField, Line,New_Line,draw_Lines
import csv
pygame.init()
screen = pygame.display.set_mode((700, 400))

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

def RemoveEntry(ClickableInstances,RemoveID):
    ClickableInstances.remove(RemoveID)
def AddEntry(ClickableInstances, yPos):
    print(yPos)
    yPos=yPos+60
    ClickableInstances.append(ClickableInstance(screen, (100,yPos),70,50, '*',1,True))
    ClickableInstances.append(ClickableInstance(screen, (180,yPos),70,50, '*',2,True))
def start():
    print("Ok, let's go")

def SaveToConfig(VariableArray):
    Lines=lsit(csv.reader.open(os.path.abspath('config.txt')))

def draw_All(screen,VariableArray):
    ClickableInstances=[]
    Lines=[]
    screen.fill('blue')
    ClickableInstances.append(ClickableInstance(screen, (300,300), 240, 50, 'Add entry'))
    ClickableInstances[-1].UniqueAction='AddEntry'
    ClickableInstances.append(ClickableInstance(screen, (550,300), 120, 50, 'Save entries to config-file'))
    ClickableInstances[-1].UniqueAction='Save'
    Lines=draw_Lines(VariableArray,ClickableInstances,screen)

    return ClickableInstances, Lines


def menu(VariableArray):
    """ This is the menu that waits you to click the s key to start """
    
    screen.fill('blue')
    ClickableInstances,Lines=draw_All(screen, VariableArray)
    #for Data in VariableArray:
    #    Lines.append(New_Line((0,0),screen,300,50,Lines,Data))
    #    ClickableInstances.append(Lines[-1])
    done= False

    ActiveInstance=None
    while not done:
        print(len(ClickableInstances))
        #print(ActiveInstance)
        #Event Handling
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Click')
                for x in ClickableInstances:
                    x.checkCollision(event.pos)
                
                Temp=None
                for x in ClickableInstances:
                    if x.isActive() != None:
                        Temp=x.isActive()
                ActiveInstance=Temp
                if ActiveInstance!=None:

                    for x in range(len(Lines)):
                        if Lines[x].Field[2].active:
                            del VariableArray[x]

                            #screen.fill('blue')
                            ActiveInstance.active=False
                            ActiveInstance.update()
                            #ClickableInstances, Lines = draw_All(screen, VariableArray)
                            ActiveInstance = None
                            
                    
                ## Add Entry
                    if ActiveInstance.UniqueAction=='AddEntry':
                        print('Ugabuga')
                        VariableArray.append(['',''])
                        ActiveInstance.active=False
                        ClickableInstances, Lines = draw_All(screen, VariableArray)
                    
                    if ActiveInstance.UniqueAction=='Save':
                        SaveToConfig(VariableArray)
                        
                

                
            
            if ActiveInstance != None:        
            
                if event.type == pygame.KEYDOWN:
                        
                    if ActiveInstance.edible==True:
                        if event.key == pygame.K_BACKSPACE:
                            ActiveInstance.text = ActiveInstance.text[:-1]
                        elif len(ActiveInstance.text)< ActiveInstance.MaxChar:
                            ActiveInstance.text += event.unicode
                        if event.key == pygame.K_RETURN:
                            print(ActiveInstance.text)
                ActiveInstance.update()        
                    #ClickableInstances[ActiveObjectId].update()
        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    DummyArray = [['U',3],['S',4],['T',1]]
    menu(DummyArray)
