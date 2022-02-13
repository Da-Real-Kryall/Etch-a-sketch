#!/usr/bin/env python3
#ETCH-A-SKETCH #eraser w e to toggle, a and d to tilt drawing by 45°, uses pythagorean theorem, s to sprint (roughness * 10)
# repolish camera, scale screen (RATIOS ARE 15:11 or 15:26, 600:440), shift coordanites in shake by increments of 5,
# and when out of bounds teleport not move opposite direction, and also put penup when moving if out of bounds
# 1 = off 0 = on
#left = horizontal right = veertical
import turtle, os, math, pathlib, tkinter, subprocess, asyncio
from pathlib import Path
home = str(Path.home())
turtle.speed(9999999999)
global hold, Roughness
Roughness = 5
hold = 1
sidelength =40
angle = 60
erasing = 1
sprinting = 1
lefttilt = 1
righttilt = 1
filling = 0
screen = turtle.Screen()
screen.setup(570,410)
screen.setworldcoordinates(-240,-210,330,200)
turtle.speed(99999)
screen.title("Press H For Help!")
turtle.pencolor("White")
turtle.begin_poly()
turtle.fd(sidelength)
turtle.lt(angle*2)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.fd(sidelength)
turtle.lt(angle)
turtle.end_poly()
p = turtle.get_poly()
turtle.register_shape("hexagon", p)
knobleftb = turtle.Turtle()
knoblefta = turtle.Turtle()
knobrighta = turtle.Turtle()
knobrightb = turtle.Turtle()
def knob1a():
    knobleftb.speed(999)
    knobleftb.penup()
    knobleftb.setpos(-150, -125)
    knobleftb.shape('hexagon')
    knobleftb.color("black")
    knobleftb.shapesize(1.1)
    knobleftb.pendown()
def knob1b():
    knoblefta.speed(999)
    knoblefta.penup()
    knoblefta.setpos(-150, -125)
    knoblefta.shape('hexagon')
    knoblefta.shapesize(1)
    knoblefta.color("grey")
    knoblefta.pendown()
def knob2b():
    knobrighta.speed(999)
    knobrighta.penup()
    knobrighta.setpos(225, -125)
    knobrighta.color("Black")
    knobrighta.shape('hexagon')
    knobrighta.shapesize(1.1)
    knobrighta.pendown()
def knob2a():
    knobrightb.speed(999)
    knobrightb.penup()
    knobrightb.setpos(225, -125)
    knobrightb.shape('hexagon')
    knobrightb.shapesize(1)
    knobrightb.color("Grey")
    knobrightb.pendown()
redbrdpen = turtle.Turtle()
def redboard():
    redbrdpen.speed(999)
    redbrdpen.penup()
    redbrdpen.setpos(-240, -200)
    redbrdpen.setheading(0)
    redbrdpen.pendown()
    redbrdpen.pensize(5)
    redbrdpen.begin_fill()
    redbrdpen.fillcolor("Red")
    redbrdpen.setpos(320, -200)
    redbrdpen.setpos(320, 200)
    redbrdpen.setpos(-240, 200)
    redbrdpen.setpos(-240, -200)
    redbrdpen.end_fill()
    redbrdpen.hideturtle()
whitebrdpen = turtle.Turtle()
def drawboard():
    whitebrdpen.speed(999)
    whitebrdpen.penup()
    whitebrdpen.setpos(-200, 160)
    whitebrdpen.pendown()
    whitebrdpen.begin_fill()
    whitebrdpen.fillcolor("White")
    whitebrdpen.pensize(2)
    whitebrdpen.setpos(280, 160)
    whitebrdpen.setpos(280, -60)
    whitebrdpen.setpos(-200, -60)
    whitebrdpen.setpos(-200, 160)
    whitebrdpen.end_fill()
    whitebrdpen.hideturtle()
#Logic sector past here, before now it has been rendering the image of the etch-a-sketch
g = 1
turtle.color("Black")
def go(Roughness='Roughness'):
    sprintanchoron = Roughness*5
    def holdtoggle():
        global hold
        if hold == 1:
            hold = hold - 1
        elif hold == 0:
            hold = hold + 1
    def erasetoggle():
        global erasing
        if erasing == 1:
            erasing = erasing - 1
        elif erasing == 0:
            erasing = erasing + 1
    def lefttoggle():
        global lefttilt
        if lefttilt == 1:
            lefttilt = lefttilt - 1
        elif lefttilt == 0:
            lefttilt = lefttilt + 1
    def righttoggle():
        global righttilt
        if righttilt == 1:
            righttilt = righttilt - 1
        elif righttilt == 0:
            righttilt = righttilt + 1
    def sprinttoggle():
        global sprinting
        if sprinting == 1:
            sprinting = sprinting - 1
        elif sprinting == 0:
            sprinting = sprinting + 1
    def up():
        global hold, erasing, sprinting, sprintanchor
        if sprinting == 1:
            Roughness = sprintanchoron/5
        elif sprinting != 1:
            Roughness = sprintanchoron
        if hold == 1:
            turtle.pendown()
        elif hold != 1:
            turtle.penup()
        if erasing == 1:
            turtle.pencolor("black")
        elif erasing != 1:
            turtle.pencolor("white")
        if filling == 1:
            turtle.pensize(5)
        if filling == 0:
            turtle.pensize(1)
        turtle.speed(999)
        turtle.setheading(90)
        if lefttilt == 1 and righttilt == 0:
            if turtle.ycor() > 160:
                turtle.penup()
                turtle.sety(160)
                turtle.pendown()
            elif turtle.ycor() < 160:
                turtle.rt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.lt(45)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 0 and righttilt == 1:
            if turtle.ycor() > 160:
                turtle.penup()
                turtle.sety(160)
                turtle.pendown()
            elif turtle.ycor() < 160:
                turtle.lt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.rt(45)
            knobleftb.tilt(Roughness) 
            knoblefta.tilt(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 1 and righttilt == 1:
            if turtle.ycor() > 160:
                turtle.penup()
                turtle.sety(160)
                turtle.pendown()
            elif turtle.ycor() < 160:
                turtle.fd(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 0 and righttilt == 0:
            if turtle.ycor() > 160:
                turtle.penup()
                turtle.sety(160)
                turtle.pendown()
            elif turtle.ycor() < 160:
                turtle.fd(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if turtle.ycor() > 160:
            turtle.penup()
            turtle.sety(160)
            turtle.pendown()
        if turtle.xcor() > 280:
            turtle.penup()
            turtle.setx(280)
            turtle.pendown()
        if turtle.xcor() < -200:
            turtle.penup()
            turtle.setx(-200)
            turtle.pendown()
        if turtle.ycor() < -60:
            turtle.penup()
            turtle.sety(-60)
            turtle.pendown()
    def down():
        global hold, erasing, sprinting, sprintanchor
        if sprinting == 1:
            Roughness = sprintanchoron/5
        elif sprinting != 1:
            Roughness = sprintanchoron
        if hold == 1:
            turtle.pendown()
        elif hold != 1:
            turtle.penup()
        if erasing == 1:
            turtle.pencolor("black")
        elif erasing != 1:
            turtle.pencolor("white")
        if filling == 1:
            turtle.pensize(5)
        if filling == 0:
            turtle.pensize(1)
        turtle.speed(1000)
        turtle.setheading(270)
        if lefttilt == 1 and righttilt == 0:
            if turtle.ycor() < -60:
                turtle.penup()
                turtle.sety(-60)
                turtle.pendown()
            elif turtle.ycor() > -60:
                turtle.rt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.lt(45)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 0 and righttilt == 1:
            if turtle.ycor() < -60:
                turtle.penup()
                turtle.sety(-60)
                turtle.pendown()
            elif turtle.ycor() > -60:
                turtle.lt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.rt(45)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
            knobrighta.tilt(Roughness)
            knobrightb.tilt(Roughness)
        if lefttilt == 1 and righttilt == 1:
            if turtle.ycor() < -60:
                turtle.penup()
                turtle.sety(-60)
                turtle.pendown()
            elif turtle.ycor() > -60:
                turtle.fd(Roughness)
            knobrighta.tilt(Roughness)
            knobrightb.tilt(Roughness)
        if lefttilt == 0 and righttilt == 0:
            if turtle.ycor() < -60:
                turtle.penup()
                turtle.sety(-60)
                turtle.pendown()
            elif turtle.ycor() > -60:
                turtle.fd(Roughness)
            knobrighta.tilt(Roughness)
            knobrightb.tilt(Roughness)
        if turtle.ycor() > 160:
            turtle.penup()
            turtle.sety(160)
            turtle.pendown()
        if turtle.ycor() < -60:
            turtle.penup()
            turtle.sety(-60)
            turtle.pendown()
        if turtle.xcor() > 280:
            turtle.penup()
            turtle.setx(280)
            turtle.pendown()
        if turtle.xcor() < -200:
            turtle.penup()
            turtle.setx(-200)
            turtle.pendown()
    def left():
        global hold, erasing, sprinting, sprintanchor
        if sprinting == 1:
            Roughness = sprintanchoron/5
        elif sprinting != 1:
            Roughness = sprintanchoron
        if hold == 1:
            turtle.pendown()
        elif hold != 1:
            turtle.penup()
        if erasing == 1:
            turtle.pencolor("black")
        elif erasing != 1:
            turtle.pencolor("white")
        if filling == 1:
            turtle.pensize(5)
        if filling == 0:
            turtle.pensize(1)
        turtle.speed(999)
        turtle.setheading(180)
        if lefttilt == 1 and righttilt == 0:
            if turtle.xcor() < -200:
                turtle.penup()
                turtle.setx(-200)
                turtle.pendown()
            elif turtle.xcor() > -200:
                turtle.rt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.lt(45)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 0 and righttilt == 1:
            if turtle.xcor() < -200:
                turtle.penup()
                turtle.setx(-200)
                turtle.pendown()
            elif turtle.xcor() > -200:
                turtle.lt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.rt(45)
            knobleftb.tilt(Roughness) # up by 1
            knoblefta.tilt(Roughness)
            knobrighta.tilt(Roughness)
            knobrightb.tilt(Roughness)
        if lefttilt == 1 and righttilt == 1:
            if turtle.xcor() < -200:
                turtle.penup()
                turtle.setx(-200)
                turtle.pendown()
            elif turtle.xcor() > -200:
                turtle.fd(Roughness)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
        if lefttilt == 0 and righttilt == 0:
            if turtle.xcor() < -200:
                turtle.penup()
                turtle.setx(-200)
                turtle.pendown()
            elif turtle.xcor() > -200:
                turtle.fd(Roughness)
            knobleftb.tilt(Roughness)
            knoblefta.tilt(Roughness)
        if turtle.ycor() > 160:
            turtle.penup()
            turtle.sety(160)
            turtle.pendown()
        if turtle.xcor() > 280:
            turtle.penup()
            turtle.setx(280)
            turtle.pendown()
        if turtle.xcor() < -200:
            turtle.penup()
            turtle.setx(-200)
            turtle.pendown()
        if turtle.ycor() < -60:
            turtle.penup()
            turtle.sety(-60)
            turtle.pendown()
    def right():
        global hold, erasing, sprinting, sprintanchor
        if sprinting == 1:
            Roughness = sprintanchoron/5
        elif sprinting != 1:
            Roughness = sprintanchoron
        if hold == 1:
            turtle.pendown()
        elif hold != 1:
            turtle.penup()
        if erasing == 1:
            turtle.pencolor("black")
        elif erasing != 1:
            turtle.pencolor("white")
        if filling == 1:
            turtle.pensize(5)
        if filling == 0:
            turtle.pensize(1)
        turtle.speed(1000)
        turtle.setheading(0)
        if lefttilt == 1 and righttilt == 0:
            if turtle.xcor() < 280:
                turtle.rt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.lt(45)
            elif turtle.xcor() > 280:
                turtle.penup()
                turtle.setx(280)
                turtle.pendown()
            knobleftb.tilt(-Roughness) 
            knoblefta.tilt(-Roughness)
            knobrighta.tilt(Roughness)
            knobrightb.tilt(Roughness)
        if lefttilt == 0 and righttilt == 1:
            if turtle.xcor() < 280:
                turtle.lt(45)
                turtle.fd(math.sqrt((Roughness*Roughness)+(Roughness*Roughness)))
                turtle.rt(45)
            elif turtle.xcor() > 280:
                turtle.penup()
                turtle.setx(280)
                turtle.pendown()
            knobleftb.tilt(-Roughness) 
            knoblefta.tilt(-Roughness)
            knobrighta.tilt(-Roughness)
            knobrightb.tilt(-Roughness)
        if lefttilt == 1 and righttilt == 1:
            if turtle.xcor() < 280:
                turtle.fd(Roughness)
            elif turtle.xcor() > 280:
                turtle.penup()
                turtle.setx(280)
                turtle.pendown()
            knobleftb.tilt(-Roughness)
            knoblefta.tilt(-Roughness)
        if lefttilt == 0 and righttilt == 0:
            if turtle.xcor() < 280:
                turtle.fd(Roughness)
            elif turtle.xcor() > 280:
                turtle.penup()
                turtle.setx(280)
                turtle.pendown()
            knobleftb.tilt(-Roughness)
            knoblefta.tilt(-Roughness)
        if turtle.ycor() > 160:
            turtle.penup()
            turtle.sety(160)
            turtle.pendown()
        if turtle.xcor() > 280:
            turtle.penup()
            turtle.setx(280)
            turtle.pendown()
        if turtle.xcor() < -200:
            turtle.penup()
            turtle.setx(-200)
            turtle.pendown()
        if turtle.ycor() < -60:
            turtle.penup()
            turtle.sety(-60)
            turtle.pendown()
    def clear():
        screen.setworldcoordinates(-240,-210,330,200)
        screen.setworldcoordinates(-240+5,-210+5,330+5,200+5)
        screen.setworldcoordinates(-240+10,-210+10,330+10,200+10)
        screen.setworldcoordinates(-240+15,-210+15,330+15,200+15)
        screen.setworldcoordinates(-240+10,-210+10,330+10,200+10)
        screen.setworldcoordinates(-240+5,-210+5,330+5,200+5)
        screen.setworldcoordinates(-240,-210,330,200)
        screen.setworldcoordinates(-240-5,-210-5,330-5,200-5)
        screen.setworldcoordinates(-240-10,-210-10,330-10,200-10)
        screen.setworldcoordinates(-240-15,-210-15,330-15,200-15)
        screen.setworldcoordinates(-240-10,-210-10,330-10,200-10)
        screen.setworldcoordinates(-240-5,-210-5,330-5,200-5)
        screen.setworldcoordinates(-240,-210,330,200)
        screen.setworldcoordinates(-240+5,-210+5,330+5,200+5)
        screen.setworldcoordinates(-240+10,-210+10,330+10,200+10)
        screen.setworldcoordinates(-240+15,-210+15,330+15,200+15)
        turtle.clear()
        screen.setworldcoordinates(-240+10,-210+10,330+10,200+10)
        screen.setworldcoordinates(-240+5,-210+5,330+5,200+5)
        screen.setworldcoordinates(-240,-210,330,200)
        screen.setworldcoordinates(-240-5,-210-5,330-5,200-5)
        screen.setworldcoordinates(-240-10,-210-10,330-10,200-10)
        screen.setworldcoordinates(-240-15,-210-15,330-15,200-15)
        screen.setworldcoordinates(-240-10,-210-10,330-10,200-10)
        screen.setworldcoordinates(-240-5,-210-5,330-5,200-5)
        screen.setworldcoordinates(-240,-210,330,200)
    def resizecompensation(x,y):
        screen.screensize(screen.window_height()*1.39,screen.window_height())
        screen.setworldcoordinates(-240,-210,330,200)
        if (1.1*(screen.canvheight/410))>=(1.1*(screen.canvwidth/410)):
            knobleftb.shapesize(1.1*(screen.canvwidth/410))
            knobrighta.shapesize(1.1*(screen.canvwidth/410))
            knoblefta.shapesize(1*(screen.canvwidth/410))
            knobrightb.shapesize(1*(screen.canvwidth/410))
        if (1.1*(screen.canvheight/410))<=(1.1*(screen.canvwidth/410)):
            knobleftb.shapesize(1.1*(screen.canvheight/410))
            knobrighta.shapesize(1.1*(screen.canvheight/410))
            knoblefta.shapesize(1*(screen.canvheight/410))
            knobrightb.shapesize(1*(screen.canvheight/410))
        if (0.1*(screen.canvheight/410))<=(0.1*(screen.canvwidth/410)):
            turtle.shapesize(0.1*(screen.canvheight/410))
        if (0.1*(screen.canvheight/410))>=(0.1*(screen.canvwidth/410)):
            turtle.shapesize(0.1*(screen.canvwidth/410))
    def hewp_meee():
        #file_to_open = os.path.expanduser('~/Library/Application Support/Etch-A-Sketch/help.txt')
        #f = open(file_to_open,'r')
        helptext = tkinter.Tk()
        helptextcontent = """

Hello, this document contains help with using the Etch-A-Sketch!

<=============================================================================================>

H  = Help, opens this page.

A  =  Rotates pen control by 45° Counter-Clockwise. 
(Toggleable)

D =  Similar to A, rotates pen control by 45° Clockwise. 
(Toggleable)

S  =  Sprint, Increases the distance drawn by the pen by 5x. 
(Toggleable)

E  =  Eraser, changes pen to an eraser, redraw over lines to remove them, although there 
is a bug in which it doesn't work completely while A or D is activated. 
(Toggleable)

C  =  Disables pen drawing, which admittedly is unrealistic for an Etch-A-Sketch. 
(Toggleable)

V = Fill mode, increases width of the pen/drawing dot enough to completely fill squares.
(Toggleable)

Spacebar  =  Shakes the Etch-A-Sketch, therefore clearing it, don't press this 
accidentally! 

 Escape = Closes the program

<=============================================================================================>

Enjoy using the most cursed drawing tool ever!
"""
        tkinter.Label(helptext, text=helptextcontent).grid(row=0)#f.read not helptextcontent
        helptext.title("HELP_HATH_COMETH")
        screen.title("Etch-A-Sketch!")
    def stahp():
        subprocess.call(['osascript', '-e', 'tell application "Terminal" to quit'])
    def filltoggle():
        global filling
        if filling == 1:
            filling = filling - 1
        elif filling == 0:
            filling = filling + 1
    redboard()
    knob1a()
    knob1b()
    knob2b()
    knob2a()
    drawboard()
    turtle.clear()
    turtle.shapesize(0.1)
    turtle.shape('square')
    for g in range (2): #if i do a while loop the program freezes and activity monitor says its using over 90% of my cpu sooooo... :/
        turtle.onkeypress(up, "Up")
        turtle.onkeypress(down, "Down")
        turtle.onkeypress(left, "Left")
        turtle.onkeypress(right, "Right")
        turtle.onkeypress(clear, "space")
        turtle.onkeypress(holdtoggle, "c")
        turtle.onkeypress(erasetoggle,"e")
        turtle.onkeypress(lefttoggle,"a")
        turtle.onkeypress(righttoggle,"d")
        turtle.onkeypress(sprinttoggle,"s")
        turtle.onkeypress(hewp_meee, "h")
        turtle.onkeypress(stahp, "Escape")
        turtle.onkeypress(filltoggle,"v")
        screen.onclick(resizecompensation)
        turtle.listen()
    turtle.mainloop()
go(Roughness)  #change value: go([HERE]) to either increase or decrease precision of drawing capabilities