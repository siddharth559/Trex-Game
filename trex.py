import turtle
import random
screen=turtle.Screen()
screen.setup(1360,720)
screen.bgpic('bg.gif')
screen.addshape('trex.gif')
screen.addshape('tree.gif')
screen.addshape('tree1.gif')
screen.addshape('floor.gif')
#####################################################
a=turtle.Turtle(shape='trex.gif')
a.penup()
a.speed(3)
a.setposition(-400,-200)
######################################################
tree=turtle.Turtle()
tree.hideturtle()
tree.speed(0)
tree.penup()
tree.setposition(630,-180)

jump=[1,2,3]
def upp():
    global jump
    jump.insert(2,True)
def down():
    global jump
    jump.insert(2,False)
screen.onkey(upp,'space')
screen.listen()
tree.showturtle()
floor=[turtle.Turtle(shape='floor.gif') for i in range(4)]
for n in floor:
    n.hideturtle()
    n.penup()
    n.speed(0)
    
floor[0].setposition(450, -300)
floor[1].setposition(50, -300)
floor[2].setposition(-300, -300)
floor[3].setposition(-640, -300)
for n in floor:
    n.showturtle()
def touch():
    xt=int(tree.xcor())
    yt=int(tree.ycor())
    xa=int(a.xcor())
    ya=int(a.ycor())
    if xa in range(int(xt)-25, int(xt)+26):
        if ya in range((int(yt)-80),(int(yt)+81)):
            return True

def move():
    if int(a.ycor())>=40:
        down()
def restrict():
    global jump
    if int(a.ycor())<=-220:
        jump[2]=''

        

while True:
    if touch()!=True:
        move()
        restrict()
        treedict={1:'tree.gif', 2:'tree1.gif'}
        n=random.randint(1,3)
        shpe=''
        for n in treedict:
            shpe=treedict[n]
        tree.shape(shpe)
        x=int(tree.xcor())
        y=int(tree.ycor())
        tree.setposition(x-10,y)
        if jump[2]==True:
            x_=int(a.xcor())
            y_=int(a.ycor())
            a.setposition(x_,y_+10)
        if jump[2]==False:
            X_=int(a.xcor())
            Y_=int(a.ycor())
            a.setposition(X_,Y_-10)
        if int(tree.xcor())<=-730:
            tree.hideturtle()
            tree.setposition(660,int(tree.ycor()))
            tree.showturtle()
            treedict={1:'tree.gif', 2:'tree1.gif'}
            n=random.randint(1,3)
            shpe=''
            for n in treedict:
                shpe=treedict[n]
            tree.shape(shpe)
            
    if touch==True:
        break
