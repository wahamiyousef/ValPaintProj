from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog
root=Tk()
root.withdraw() #hides the small extra window
font.init()

width,height=1100,720
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
GRAY=(40,40,40)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

#rename+new icon window
valLogo=image.load("Icons/valLogo.png")
vIcon=image.load("Icons/vIcon.png")
display.set_caption('VALORANT Photo Editor')
display.set_icon(vIcon)


#canvas settings + setup
PaintBGimg=image.load("Icons/background.jpg")
PaintBGimg=transform.scale(PaintBGimg,(width,height))
screen.blit(PaintBGimg,(0,0))
CanvasCol=(255,255,255)

canvasRect=Rect(150,60,800,600)
draw.rect(screen,CanvasCol,canvasRect)



#load and save images
saveImg=image.load("Icons/save.png")
loadImg=image.load("Icons/load.png")
#undo redo
undoImg=image.load("Icons/undo.png")
redoImg=image.load("Icons/redo.png")
#fill img
unfillImg=screen.subsurface(1025,580,20,20).copy()
#tool images
toolPics=["Icons/pencil.png","Icons/eraser.png","Icons/pbucket.png","Icons/bin.png","Icons/spray.png","Icons/brush.png","Icons/line.png","Icons/rect.png","Icons/circle.png","Icons/triangle.png"]
toolPic=["penImg","eraserImg","pbkImg","binImg","sprayImg","brushImg","lineImg","rectImg","circImg","trigImg"]
for i in range(len(toolPics)):
    toolPic[i]=image.load(toolPics[i])

#sticker images
stkPics=["Stickers/iron.png","Stickers/bronze.png","Stickers/silver.png","Stickers/gold.png","Stickers/plat.png","Stickers/diamond.png","Stickers/immo.png","Stickers/radiant.png"]
stkPic=["iron","bronze","silver","gold","plat","diamond","immo","radiant"]
for i in range(len(stkPics)):
    stkPic[i]=image.load(stkPics[i])

#background images
bgPics=["Stickers/haven.jpg","Stickers/icebox.jpg","Stickers/breeze.jpg","Stickers/ascent.jpg",]
bgPic=["haven","icebox","breeze","ascent"]
for i in range(len(bgPics)):
    bgPic[i]=image.load(bgPics[i])

bgPicsLogo=["Stickers/havenLogo.jpg","Stickers/iceboxLogo.jpg","Stickers/breezeLogo.jpg","Stickers/ascentLogo.jpg",]
bgPicLogo=["havenLogo","iceboxLogo","breezeLogo","ascentLogo"]
for i in range(len(bgPicsLogo)):
    bgPicLogo[i]=image.load(bgPicsLogo[i])


#save and load rects
saveRect=Rect(20,10,40,40)
loadRect=Rect(75,10,40,40)
#undo redo rects
undoRect=Rect(150,10,40,40)
redoRect=Rect(200,10,40,40)
#filled/unfilled rect
fillRect=Rect(1020,575,30,30)
unfillRect=Rect(1025,580,20,20)
#flip rect
HflipRect=Rect(20,350,86,40)
draw.rect(screen,WHITE,HflipRect)
VflipRect=Rect(20,400,86,40)
draw.rect(screen,WHITE,VflipRect)
#crop rect
cropRect=Rect(20,450,86,40)
draw.rect(screen,WHITE,cropRect,2)
#tool rects
pencilRect=Rect(20,90,40,40)
eraserRect=Rect(65,90,40,40)
pbucketRect=Rect(20,135,40,40)
binRect=Rect(65,135,40,40)
sprayRect=Rect(20,180,40,40)
brushRect=Rect(65,180,40,40)
lineRect=Rect(20,225,40,40)
shapeRect=Rect(65,225,40,40)
circleRect=Rect(20,270,40,40)
rectRect=Rect(65,270,40,40)

#sticker rects
ironRect=Rect(150,665,40,50)
bronzeRect=Rect(200,665,40,50)
silverRect=Rect(250,665,40,50)
goldRect=Rect(300,665,40,50)
platRect=Rect(350,665,40,50)
diaRect=Rect(400,665,40,50)
immoRect=Rect(450,665,40,50)
radiantRect=Rect(500,665,40,50)
#logo rect
valRect=Rect(425,10,278,40)
#background rects
havenRect=Rect(600,665,80,50)
breezeRect=Rect(690,665,80,50)
iceboxRect=Rect(780,665,80,50)
ascentRect=Rect(870,665,80,50)

#red slider
redSlider=Rect(965,90,125,30)
draw.rect(screen,RED,redSlider)
redSS=screen.subsurface(redSlider).copy()
redSliderButton=(965,90,10,30)
draw.rect(screen,GREY,redSliderButton)
#green slider
greenSlider=Rect(965,130,125,30)
draw.rect(screen,GREEN,greenSlider)
greenSS=screen.subsurface(greenSlider).copy()
greenSliderButton=(965,130,10,30)
draw.rect(screen,GREY,greenSliderButton)
#blue slider
blueSlider=Rect(965,170,125,30)
draw.rect(screen,BLUE,blueSlider)
blueSS=screen.subsurface(blueSlider).copy()
blueSliderButton=(965,170,10,30)
draw.rect(screen,GREY,blueSliderButton)
#size slider
sizeSlider=Rect(965,360,30,125)
draw.rect(screen,BLACK,sizeSlider)
sizeSS=screen.subsurface(sizeSlider).copy()
sizeSliderButton=(965,360,30,10)
draw.rect(screen,GREY,sizeSliderButton)

#later to use for updating size/colour
circleSize=screen.subsurface(962,212,126,126).copy()

#draw save/load images into place
screen.blit(saveImg,saveRect)
screen.blit(loadImg,loadRect)
#draw undo/redo images into place
screen.blit(undoImg,undoRect)
screen.blit(redoImg,redoRect)
#draw fill rect
draw.rect(screen,WHITE,fillRect)
screen.blit(unfillImg,unfillRect)
#draw tool images into place
toolRects=[pencilRect,eraserRect,pbucketRect,binRect,sprayRect,brushRect,lineRect,shapeRect,circleRect,rectRect]
for i in range(len(toolRects)):
    screen.blit(toolPic[i],toolRects[i])
    
#draw stickers image into place
stkRects=[ironRect,bronzeRect,silverRect,goldRect,platRect,diaRect,immoRect,radiantRect]
for i in range(len(stkRects)):
    screen.blit(stkPic[i],stkRects[i])
#Background Logos
bgLogoRects=[havenRect,iceboxRect,breezeRect,ascentRect]
for i in range(len(bgPicLogo)):
    screen.blit(bgPicLogo[i],bgLogoRects[i])
#valorant logo
screen.blit(valLogo,valRect)

#font/text load and render
familyFont=font.SysFont("Arial",15)
stampsWrd=familyFont.render("Stamps",True,WHITE)
fillWrd=familyFont.render("Fill:",True,WHITE)
rgbWrd=familyFont.render("Colours",True,BLACK)
sizeWrd=familyFont.render("Size",True,BLACK)
toolsWrd=familyFont.render("Tools",True,BLACK)
HflipWrd=familyFont.render("Horizontal Flip",True,BLACK)
VflipWrd=familyFont.render("Vertical Flip",True,BLACK)
cropWrd=familyFont.render("Crop",True,BLACK)

#initialize text
screen.blit(stampsWrd,(550,680))
screen.blit(fillWrd,(980,580))
screen.blit(rgbWrd,(1000,60))
screen.blit(sizeWrd,(968,340))
screen.blit(toolsWrd,(50,60))
screen.blit(HflipWrd,HflipRect)
screen.blit(VflipWrd,VflipRect)
screen.blit(cropWrd,cropRect)



#change colour based on value
UNSEL=(255,255,255) #unselected
HOVER=(255,0,0) #hover over
SEL=(0,0,255)   #selected
CROPT=(0,0,156) #crop border colour


#tool lists (to determine all tools , current tools using and not using)
tools=[pencilRect,eraserRect,pbucketRect,binRect,sprayRect,brushRect,lineRect,shapeRect,circleRect,rectRect,ironRect,bronzeRect,silverRect,goldRect,platRect,diaRect,immoRect,radiantRect,havenRect,iceboxRect,breezeRect,ascentRect,cropRect]#you will have more tools in the PAINT project
tool=""
toolSel=[UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL,UNSEL]
toolSelReset = toolSel.copy() #copies list and sets it

#the start of undo screenshot to back/forth to
undoShot=screen.subsurface(canvasRect).copy()
undoList=[undoShot] #lists to contain undo images
redoList=[]                          #redo

#tool settings
R=0
G=0
B=0
colour=(R,G,B)
size=15 #brush size
fill=size #shape size

running=True


while running:
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1: #left click
                click=True #true if mouse is down
                if canvasRect.collidepoint(mx,my):
                    sx,sy=evt.pos #starting x and y pos
                startShot=screen.subsurface(canvasRect).copy() #starting screenshot
        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) and tool=="crop": #if crop tool
                screen.blit(startShot,(150,60))
                rectScreen=screen.subsurface(oRect1).copy() #take screenshot of crop size
                rectScreen=transform.scale(rectScreen,(800,600))
                screen.blit(rectScreen,(150,60)) #load screnshot
            if canvasRect.collidepoint(mx,my) and tool!="":
                startShot=screen.subsurface(canvasRect).copy()
                undoList.append(startShot) #if any chanegs append to list



    if click and saveRect.collidepoint(mx,my): #save image
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        image.save(screen.subsurface(canvasRect),fname)

    if click and loadRect.collidepoint(mx,my): #load image
        fname=filedialog.askopenfilename()
        preloadPic=image.load(fname)
        loadPic=transform.scale(preloadPic,(800,600))
        screen.blit(loadPic,canvasRect)


    if click and undoRect.collidepoint(mx,my) and len(undoList)>1: #if undo button is clicked and has more than 1 image
        redoList.append(undoList[-1]) #append most recent image to redo
        undoList.pop() #remove most recent image
        screen.blit(undoList[-1],canvasRect) #display change
    if click and redoRect.collidepoint(mx,my) and len(redoList)>0: #redo button
        undoList.append(redoList[-1])
        redoList.pop()
        screen.blit(undoList[-1],canvasRect)

    #shape fill check mark
    if click and fillRect.collidepoint(mx,my):
        if fill>0: #if fill size is greater than 0
            fill=0 #set to 0
            draw.rect(screen,WHITE,fillRect) #display that its filled
        else:
            fill=size #set fill as size brush
            screen.blit(unfillImg,unfillRect) #display that its unfilled

    #Horizontal Flip
    if click and HflipRect.collidepoint(mx,my):
        startShot=transform.flip(startShot,True,False) #flips screenshot horizontally
        screen.blit(startShot,canvasRect) #blits screenshot
    #vertical flip
    if click and VflipRect.collidepoint(mx,my):
        startShot=transform.flip(startShot,False,True) #flips vertically
        screen.blit(startShot,canvasRect)
    

    #rgb sliders
    if mb[0] and redSlider.collidepoint(mx,my):  #red
        screen.set_clip(redSlider) #so user doesnt go out of slider
        screen.blit(redSS,(965,90)) #draw red rect
        redSliderButton=(mx,90,10,30) #change slider on mx
        draw.rect(screen,GREY,redSliderButton) #display moving slider
        R=(mx-965)*2 #red value
        colour=(R,G,B) #set to colour value
        screen.set_clip(None) #user can edit out of slider
    if mb[0] and greenSlider.collidepoint(mx,my): #green
        screen.set_clip(greenSlider)
        screen.blit(greenSS,(965,130))
        greenSliderButton=(mx,130,10,30)
        draw.rect(screen,GREY,greenSliderButton)
        G=(mx-965)*2
        colour=(R,G,B)
        screen.set_clip(None)
    if mb[0] and blueSlider.collidepoint(mx,my): #blyue
        screen.set_clip(blueSlider)
        screen.blit(blueSS,(965,170))
        blueSliderButton=(mx,170,10,30)
        draw.rect(screen,GREY,blueSliderButton)
        B=(mx-965)*2
        colour=(R,G,B)
        screen.set_clip(None)
    if mb[0] and sizeSlider.collidepoint(mx,my): #size
        screen.set_clip(sizeSlider)
        screen.blit(circleSize,(965,170)) #show preview of size
        screen.blit(sizeSS,(965,360))
        sizeSliderButton=(965,my,30,10)
        draw.rect(screen,GREY,sizeSliderButton)
        S=my-358 #size is determined by 'my' location
        size=int(S/2) #size is an integer and not too big
        fill=size 
        screen.set_clip(None)
        screen.blit(circleSize,(962,212)) #display changes/preview
        
    draw.circle(screen,colour,(1025,275),size) #preview circle

    #drawing tools
    for i in range(0,len(tools)):
        draw.rect(screen,toolSel[i],tools[i],2)
        
    #this system applies to everything down below
    if tools[0].collidepoint(mx,my):#is the mouse pointer inside the pencilRect
        draw.rect(screen,HOVER,tools[0],2) #draw outline
        if click: #if lmb then
            tool="pencil" #set tool as pencil
            toolSel=list(toolSelReset) #reset all other tools to unselected
            toolSel[0]=SEL #set current tool as selected
            
    if tools[1].collidepoint(mx,my):#is the mouse pointer inside the eraserRect
        draw.rect(screen,HOVER,tools[1],2)
        if click:
            tool="eraser"
            toolSel=list(toolSelReset)
            toolSel[1]=SEL
        
    if tools[2].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[2],2)
        if click:
            tool="paintbucket"
            toolSel=list(toolSelReset)
            toolSel[2]=SEL

    if tools[3].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[3],2)
        if click:
            tool="bin"
            toolSel=list(toolSelReset)
            toolSel[3]=SEL

    if tools[4].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[4],2)
        if click:
            tool="spray"
            toolSel=list(toolSelReset)
            toolSel[4]=SEL

    if tools[5].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[5],2)
        if click:
            tool="brush"
            toolSel=list(toolSelReset)
            toolSel[5]=SEL

    if tools[6].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[6],2)
        if click:
            tool="line"
            toolSel=list(toolSelReset)
            toolSel[6]=SEL

    if tools[7].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[7],2)
        if click:
            tool="rectR"
            toolSel=list(toolSelReset)
            toolSel[7]=SEL

    if tools[8].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[8],2)
        if click:
            tool="oval"
            toolSel=list(toolSelReset)
            toolSel[8]=SEL

    if tools[9].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[9],2)
        if click:
            tool="shape"
            toolSel=list(toolSelReset)
            toolSel[9]=SEL

    if tools[10].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[10],2)
        if click:
            tool="iron"
            toolSel=list(toolSelReset)
            toolSel[10]=SEL
    if tools[11].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[11],2)
        if click:
            tool="bronze"
            toolSel=list(toolSelReset)
            toolSel[11]=SEL
    if tools[12].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[12],2)
        if click:
            tool="silver"
            toolSel=list(toolSelReset)
            toolSel[12]=SEL
    if tools[13].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[13],2)
        if click:
            tool="gold"
            toolSel=list(toolSelReset)
            toolSel[13]=SEL
    if tools[14].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[14],2)
        if click:
            tool="plat"
            toolSel=list(toolSelReset)
            toolSel[14]=SEL
    if tools[15].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[15],2)
        if click:
            tool="diamond"
            toolSel=list(toolSelReset)
            toolSel[15]=SEL
    if tools[16].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[16],2)
        if click:
            tool="immo"
            toolSel=list(toolSelReset)
            toolSel[16]=SEL
    if tools[17].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[17],2)
        if click:
            tool="radiant"
            toolSel=list(toolSelReset)
            toolSel[17]=SEL
            
    if tools[18].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[18],2)
        if click:
            tool="haven"
            toolSel=list(toolSelReset)
            toolSel[18]=SEL
    if tools[19].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[19],2)
        if click:
            tool="icebox"
            toolSel=list(toolSelReset)
            toolSel[19]=SEL
    if tools[20].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[20],2)
        if click:
            tool="breeze"
            toolSel=list(toolSelReset)
            toolSel[20]=SEL
    if tools[21].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[21],2)
        if click:
            tool="ascent"
            toolSel=list(toolSelReset)
            toolSel[21]=SEL
    if tools[22].collidepoint(mx,my):
        draw.rect(screen,HOVER,tools[22],2)
        if click:
            tool="crop"
            toolSel=list(toolSelReset)
            toolSel[22]=SEL
            

    #logic code of actual tool
    if mb[0] and canvasRect.collidepoint(mx,my):#left click and inside the canvas
        screen.set_clip(canvasRect) #only canvas area can be updated
        if tool=="pencil":
            draw.line(screen,colour,(omx,omy),(mx,my))
        if tool=="eraser": #if eraser toil
            dx=mx-omx#horiz distance
            dy=my-omy #vertical distance
            dist=sqrt(dx**2+dy**2)
            for d in range(1,int(dist),1):
                dotX=d*dx/dist+omx
                dotY=d*dy/dist+omy
                draw.circle(screen,CanvasCol,(int(dotX),int(dotY)),size)
            draw.circle(screen,CanvasCol,(mx,my),size)
        if tool=="paintbucket": #if paint bucket
            CanvasCol=(colour) #set colour to canvas 
            draw.rect(screen,CanvasCol,canvasRect) #draw on canvas
        if tool=="spray": #if spray tool
            for i in range(5): #random spray pattern
                rx=randint(-size,size)
                ry=randint(-size,size)
                if rx**2+ry**2<=size**2:
                    draw.circle(screen,colour,(mx-rx,my-ry),1)
        if tool=="brush": #if brush tool
            dx=mx-omx#horiz distance
            dy=my-omy #vertical distance
            dist=sqrt(dx**2+dy**2)
            for d in range(1,int(dist),1): #to connect dots so itis seemless
                dotX=d*dx/dist+omx
                dotY=d*dy/dist+omy
                draw.circle(screen,colour,(int(dotX),int(dotY)),size)
            draw.circle(screen,colour,(mx,my),size)
    if canvasRect.collidepoint(mx,my) and mb[0]:
        #shape tools
        if tool=="line": #if line toool
            screen.blit(startShot,(150,60)) #draw screenshot before drawing
            draw.line(screen,colour,(sx,sy),(mx,my),size) #previous mx,my connect to new mx,my
        if tool=="rectR": #draw rectangle
            screen.blit(startShot,(150,60)) #draw screenshot before drawing
            oRect=Rect(sx,sy,mx-sx,my-sy)
            oRect.normalize()
            draw.rect(screen,colour,oRect,fill) #previous mx,my connect to new mx,my
        if tool=="oval": #draw circle
            screen.blit(startShot,(150,60)) #draw screenshot before drawing
            oRect=Rect(sx,sy,mx-sx,my-sy)
            oRect.normalize()
            draw.ellipse(screen,colour,oRect,fill)
        if tool=="shape":  #right angle triangle
            screen.blit(startShot,(150,60))
            draw.polygon(screen,colour,[(mx,my),(sx,sy),(mx,sy)],fill)
        if tool=="crop":
            screen.blit(startShot,(150,60)) #draw screenshot before drawing
            oRect1=Rect(sx,sy,mx-sx,my-sy)
            oRect1.normalize()
            draw.rect(screen,CROPT,oRect1,2)


        #sticker tools
        if tool=="iron":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[0],(mx,my))
        if tool=="bronze":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[1],(mx,my))
        if tool=="silver":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[2],(mx,my))
        if tool=="gold":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[3],(mx,my))
        if tool=="plat":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[4],(mx,my))
        if tool=="diamond":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[5],(mx,my))
        if tool=="immo":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[6],(mx,my))
        if tool=="radiant":
            screen.blit(startShot,(150,60))
            screen.blit(stkPic[7],(mx,my))
        

    #background images
    if tool=="haven":
        screen.blit(bgPic[0],canvasRect)
    if tool=="icebox":
        screen.blit(bgPic[1],canvasRect)
    if tool=="breeze":
        screen.blit(bgPic[2],canvasRect)
    if tool=="ascent":
        screen.blit(bgPic[3],canvasRect)

    #completely wipes canvas
    if tool=="bin":
        CanvasCol=WHITE
        draw.rect(screen,WHITE,canvasRect)
            
            
    screen.set_clip(None) #going back to the normal state
    
        
    omx,omy=mx,my #saves previous locations of mx,my
    display.flip()
            
quit()
