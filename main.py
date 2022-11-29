# TODO 1: Importar modulo tortuga y pandas
import turtle
import pandas

# todo 1.1: Crear objeto y generar una ventana
screen = turtle.Screen()
# todo 1.2: Cambiar el titulo
screen.title("U.S. States Game")
# todo 1.4: Colocar de fondo de pantalla la imagen "blank_states_img.gif"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# todo 1.5: Tamanio de la ventana
screen.screensize(canvwidth=600, canvheight=500)

# TODO 3: Iniciar recoleccion de datos con Pandas
# todo 3.1: Leer y guardar en una variable el archivo CSV con pandas
data = pandas.read_csv("50_states.csv")

# todo 3.2: verificar si la respuesta del jugador se encuentra en la lista de estados del archivo CSV
# todo 3.2.1: crear una lista con la columna donde se encuentran todos los estados del archivo CSV
all_states = data.state.to_list()

# Contador
guessed_states = []

while len(guessed_states) < 50:
    # TODO 2: Crear input donde recibira por parte del jugador el nombre del estado.
    # Este se guardara en una variable.
    # El titulo de la ventana llevara la cuenta de los aciertos
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # todo 3.2.3: Salir del juego
    if answer_state == "Exit":
        # TODO 4: Aca se guardaran los estados que no han sido adivinados y luego los enviare a un CSV nuevo
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # todo 3.2.2:
    # a)Verificar si el lo introducido por el usuario en "answer_state" se encuentra en "all_states",
    # si es correcto, procesar y volver a llamar la funcion
    if answer_state in all_states:
        # Mi contador de guessed_state = []
        guessed_states.append(answer_state)
        # Si la respuesta es "True":
        # Crear una nueva tortuga
        t = turtle.Turtle()
        # Ocultar la tortuga
        t.hideturtle()
        # Encerramos la tortuga para que no haga ningun dibujo
        t.penup()
        # Envio la tortuga a las coordenadas donde se ubica el estado,
        # usando las coordenadas del CSV (debo regresar un str)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Escribo el nombre del estado, en las coordenas
        t.write(state_data.state.item())  # .item() es para eliminar otros datos como el "id", cabeceras de la lista, otros