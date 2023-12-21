import turtle 
import time 
import random

posponer = 0.1

score = 0
high_score = 0

#configuracion de ventana
wn = turtle.Screen()
wn.title("Vivoretaaa")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)#mejora la animacion

cabeza = turtle.Turtle()
cabeza.speed()
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direccion = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

segmentos = []
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0         High Score: 0", align = "center", font=("Courier",24,"normal"))

def arriba():
    cabeza.direccion = "Up"
def abajo():
    cabeza.direccion = "Down"
def izquierda():
    cabeza.direccion = "Left"
def derecha():
    cabeza.direccion = "Right"

def mov():
    if cabeza.direccion == "Up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direccion == "Down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direccion == "Left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direccion == "Right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
while True:
    wn.update()
    if (cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280):
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direccion = "stop"
        for segmento in segmentos:
            segmento.goto(1000,1000)
        segmentos.clear()
        score = 0
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font=("Courier",24,"normal"))

    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x, y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed()
        nuevo_segmento.shape("square")
        nuevo_segmento.color("yellow")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font=("Courier",24,"normal"))

    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)   
    mov()
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direccion = "stop"
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font=("Courier",24,"normal"))

    time.sleep(posponer)
    