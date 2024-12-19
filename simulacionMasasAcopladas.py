from vpython import *

# Definir las constantes del sistema
k1 = 5  # Constante elástica del resorte 1 (N/m)
k2 = 3  # Constante elástica del resorte 2 (N/m)
m1 = 1  # Masa del primer péndulo (kg)
m2 = 0.5  # Masa del segundo péndulo (kg)
L1 = 5  # Longitud del primer resorte (m)
L2 = 3  # Longitud del segundo resorte (m)
x1_0 = 3  # Posición inicial de la primera masa (m)
x2_0 = -2  # Posición inicial de la segunda masa (m)

# Crear la escena
scene = canvas(title="Simulación de Masas Acopladas con Resortes",
               width=800, height=600)

# Crear el punto de fijación (la pared)
fijacion = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.red)

# Crear el primer bob (la masa del primer resorte)
bob1 = sphere(pos=vector(x1_0, 0, 0), radius=0.5, color=color.blue, mass=m1)

# Crear el segundo bob (pendulo colgado del primer bob)
bob2 = sphere(pos=vector(x2_0, 0, 0), radius=0.5, color=color.green, mass=m2)

# Crear los resortes
resorte1 = cylinder(pos=fijacion.pos, axis=bob1.pos - fijacion.pos, radius=0.05, color=color.white)
resorte2 = cylinder(pos=bob1.pos, axis=bob2.pos - bob1.pos, radius=0.05, color=color.white)

# Variables de simulación
v1 = 0  # Velocidad de la primera masa
v2 = 0  # Velocidad de la segunda masa

# Paso de tiempo
dt = 0.01  # Paso de tiempo
t = 0  # Tiempo inicial

# Función para calcular la fuerza de un resorte
def fuerza_resorte(x, L, k):
    return -k * (x - L)

# Bucle de simulación
while t < 50:
    rate(100)  # Control de la velocidad de la simulación (cuántos pasos por segundo)

    # Posiciones actuales de las masas
    x1 = bob1.pos.x
    x2 = bob2.pos.x

    # Calcular las fuerzas sobre las masas
    F1 = fuerza_resorte(x1, L1, k1)  # Fuerza sobre la masa 1
    F2 = fuerza_resorte(x2 - x1, L2, k2)  # Fuerza sobre la masa 2 (en relación a la masa 1)
    
    # Calcular las aceleraciones (F = m * a => a = F / m)
    a1 = F1 / m1
    a2 = F2 / m2

    # Actualizar las velocidades
    v1 += a1 * dt
    v2 += a2 * dt

    # Actualizar las posiciones
    bob1.pos.x += v1 * dt
    bob2.pos.x += v2 * dt

    # Asegurar que la primera masa no cruce el eje de fijación
    if bob1.pos.x < 0:
        bob1.pos.x = 0
        v1 = 0  # Detener la masa si toca la pared

    # Asegurar que la segunda masa no cruce la primera
    if bob2.pos.x < bob1.pos.x:
        bob2.pos.x = bob1.pos.x
        v2 = 0  # Detener la masa si toca la primera masa

    # Actualizar los resortes (con las posiciones actuales)
    resorte1.axis = bob1.pos - fijacion.pos
    resorte2.axis = bob2.pos - bob1.pos

    # Incrementar el tiempo
    t += dt
