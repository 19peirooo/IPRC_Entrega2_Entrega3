import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

# Definición del tiempo
tini = 0
tfin = 200
npuntos = 10000
t = np.linspace(tini, tfin, npuntos)

# Constantes del sistema
k1 = 1  # Constante elástica del resorte 1
k2 = 0.5  # Constante elástica del resorte 2
m1 = 1  # Masa 1
m2 = 1  # Masa 2

# Condiciones iniciales: [x1_0, v1_0, x2_0, v2_0]
condiciones_iniciales = [5, 0, -5, 0]  # Posiciones y velocidades iniciales

def coupled_oscillators(valores, t, k1, k2, m1, m2):
    x1, v1, x2, v2 = valores
    # Ecuaciones diferenciales
    dx1dt = v1
    dv1dt = (-k1 * x1 + k2 * (x2 - x1)) / m1
    dx2dt = v2
    dv2dt = (-k2 * (x2 - x1)) / m2
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Resolver el sistema
solucion = odeint(coupled_oscillators, condiciones_iniciales, t, args=(k1, k2, m1, m2))

# Extraer las soluciones
x1 = solucion[:, 0]  # Posición de la masa 1
v1 = solucion[:, 1]  # Velocidad de la masa 1
x2 = solucion[:, 2]  # Posición de la masa 2
v2 = solucion[:, 3]  # Velocidad de la masa 2

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(tini, tfin)  # Rango para el tiempo
ax.set_ylim(-6, 6)  # Rango para las posiciones
ax.set_title("Osciladores Acoplados: Curvas x1(t) y x2(t)", fontsize=14)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Posición (m)")

line1, = ax.plot([], [], 'b-', label="Masa 1: x1(t)")
line2, = ax.plot([], [], 'r-', label="Masa 2: x2(t)")
ax.legend()

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,

def update_posicion(frame):
    # Actualizar los datos de las curvas hasta el frame actual
    line1.set_data(t[:frame], x1[:frame])
    line2.set_data(t[:frame], x2[:frame])
    return line1, line2,

def update_velocidad(frame):
    line1.set_data(t[:frame], v1[:frame])
    line2.set_data(t[:frame], v2[:frame])
    return line1, line2,

funcion = update_posicion
#funcion = update_velocidad

ani = animation.FuncAnimation(fig, funcion, frames=len(t), init_func=init, blit=True, interval=20)

# Mostrar la animación
plt.show()

