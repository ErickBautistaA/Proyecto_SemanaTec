"""Tic Tac Toe"""

from turtle import color
from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import onscreenclick
from turtle import done

from freegames import line

"""Inicia una cuadrícula con las celdas vacías."""
grid_state = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def grid():
    """Dibuja la cuadrícula de tic-tac-toe."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja al jugador X."""
    color('purple')
    line(x + 90, y + 90, x + 50, y + 50)
    line(x + 90, y + 50, x + 50, y + 90)


def drawo(x, y):
    """Dibuja al jugador O."""
    color('green')
    up()
    goto(x + 70, y + 40)
    down()
    circle(30)


def floor(value):
    """Redondea el valor a la cuadrícula con un tamaño cuadrado de 133."""
    return ((value + 200) // 133) * 133 - 200


"""Crea un estado para determinar los turnos"""
state = {'player': 0}
"""Crea una lista de jugadores"""
players = [drawx, drawo]


def spot_taken(x, y):
    """Checa si el espacio en la cuadrícula ha sido tomado."""
    row = int((y + 200) // 133)
    col = int((x + 200) // 133)
    return grid_state[row][col] != -1


def tap(x, y):
    """Dibuja X o O en el cuadrado picado"""
    x = floor(x)
    y = floor(y)
    player = state['player']

    """Si no ha sido tomado por el otro jugador el espacio podra ser usado"""
    if not spot_taken(x, y):
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player

        """Actualiza el estado de grid-state con el movimiento del jugador."""
        row = int((y + 200) // 133)
        col = int((x + 200) // 133)
        grid_state[row][col] = player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
"""Habilita el click para realizar la función tap"""
onscreenclick(tap)
done()
