import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros iniciales
alpha = 0.3
longitud = 3
num_puntos = 1000
num_steps = 10000
dx = longitud / (num_puntos - 1)
dt = alpha * dx**2
T_0 = 300

x = np.linspace(0, longitud, num_puntos)

# Posiciones y temperaturas de los pulsos
pos_soplete = 1
temp_soplete = 800

pos_chorro = 2
temp_chorro = 273

# Definición del pulso gaussiano
def pulso_gaussiano(x, pos, sigma_cuadrado, T_0):
    return T_0 * np.exp(-(x - pos)**2 / (2 * sigma_cuadrado))

# Pulsos iniciales
varianza_gaussiana = 0.05
T1 = pulso_gaussiano(x, pos_soplete, varianza_gaussiana, temp_soplete - T_0)
T2 = pulso_gaussiano(x, pos_chorro, varianza_gaussiana, temp_chorro - T_0)

# Graficar los pulsos iniciales
plt.title("Pulsos Gaussianos")
plt.plot(x, T1, label="Pulso Soplete")
plt.plot(x, T2, label="Pulso Chorro")
plt.legend()
plt.xlabel("Posición (m)")
plt.ylabel("Temperatura (K)")
plt.show()

# Condición inicial
T_inicial = T_0 + T1 + T2
T = T_inicial.copy()

# Simulación de difusión de calor
for step in range(num_steps):
    T = T + alpha * np.gradient(np.gradient(T, dx), dx) * dt

# Graficar las distribuciones inicial y final
plt.plot(x, T_inicial, label="T(x, 0)")
plt.plot(x, T, label="T(x, final)")
plt.title(f"Distribución de Calor en la Barra (T0 = {T_0}K)")
plt.xlabel("Posición (m)")
plt.ylabel("Temperatura (K)")
plt.legend()
plt.show()

# Animación de la interpolación entre T(x, 0) y T(x, final)
fig, ax = plt.subplots()
line, = ax.plot(x, T_inicial, label="Distribución de Calor")

ax.set_xlim(0, longitud)
ax.set_ylim(T.min() - 50, T.max() + 50)
ax.set_xlabel("Posición (m)")
ax.set_ylabel("Temperatura (K)")
ax.set_title(f"Interpolación de Calor en la Barra (T0 = {T_0}K)")
ax.legend()

# Función de actualización
def update(frame):
    t = frame / 100  # Progreso de la animación de 0 a 1
    y = (1 - t) * T_inicial + t * T
    line.set_ydata(y)
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=100, blit=True)

plt.show()