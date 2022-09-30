import turtle

#Ventana (wn)
wn = turtle.Screen()
wn.title("Pong by Souny MS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

# Player A
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.penup()
playerA.goto(-350, 0)
playerA.shapesize(stretch_wid=5, stretch_len=1)

# Player B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.penup()
playerB.goto(350, 0)
playerB.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#Modificar estas variables para cambiar la velocidad de la pelota
pelota.dx = 1
pelota.dy = 1


# Pen para dibujar el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0		player B: 0", align="center", font=("Courier", 25, "normal"))

# Funciones
def playerA_up():
	y = playerA.ycor()
	y += 20
	playerA.sety(y)

def playerA_down():
	y = playerA.ycor()
	y -= 20
	playerA.sety(y)

def playerB_up():
	y = playerB.ycor()
	y += 20
	playerB.sety(y)

def playerB_down():
	y = playerB.ycor()
	y -= 20
	playerB.sety(y)

#Teclado
wn.listen()
wn.onkeypress(playerA_up, "w")
wn.onkeypress(playerA_down, "s")
wn.onkeypress(playerB_up, "Up")
wn.onkeypress(playerB_down, "Down")


while True:
	wn.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)

	# Revisa colisiones con los bordes de la ventana
	if pelota.ycor() > 290:
		pelota.dy *= -1
	if pelota.ycor() < -290:
		pelota.dy *= -1

	# Si la pelota sale por la izq o derecha, esta regresa al centro
	if pelota.xcor() > 390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorA += 1
		pen.clear()

		# Esta línea de codigo vuelve a pintar el marcador, utilizo "format" de la versión 3.6 en adelante de python.
		#Si tienes python menor a la versión 3.6 esta parte no te funcionará.
		pen.write(f"Jugador A: {marcadorA}		player B: {marcadorB}", align="center", font=("Courier", 25, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorB += 1
		pen.clear()
		pen.write(f"Jugador A: {marcadorA}		player B: {marcadorB}", align="center", font=("Courier", 25, "normal"))


	# Revisa las colisiones
	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < playerB.ycor() + 50
			and pelota.ycor() > playerB.ycor() - 50)):
		pelota.dx *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < playerA.ycor() + 50
			and pelota.ycor() > playerA.ycor() - 50)):
		pelota.dx *= -1