import numpy as np
import matplotlib.pyplot as plt

alpha = 0.3
longitud = 3
num_puntos = 1000
num_steps = 10000
dx = longitud / (num_puntos-1)
dt = alpha * dx**2
T_0 = 300

x = np.linspace(0,longitud,num_puntos)

pos_soplete = 1
temp_soplete = 800

pos_chorro = 2
temp_chorro = 273

def pulso_gaussiano(x,pos,sigma_cuadrado,T_0):
    return T_0 * np.exp(-(x-pos)**2/(2*sigma_cuadrado))

varianza_gaussiana = 0.05
T1 = pulso_gaussiano(x,pos_soplete,varianza_gaussiana,temp_soplete-T_0)
T2 = pulso_gaussiano(x,pos_chorro,varianza_gaussiana,temp_chorro-T_0)

plt.title("Pulsos Gaussianos")
plt.plot(x,T1,label = "Pulso Soplete")
plt.plot(x,T2, label = "Pulso Chorro")
plt.legend()
plt.show()
    
T = T_0 + T1 + T2
for step in range (num_steps):
    T = T + alpha * np.gradient(np.gradient(T,dx), dx) * dt

plt.plot(x,T_0 + T1 + T2, label = "T(x,0)")
plt.plot(x,T, label = "T(x,final)")

plt.title("Distribucion de Calor en la Barra para un T0 = {:d}K".format(T_0))
plt.xlabel("Posicion (m)")
plt.ylabel("Temperatura (K)")
plt.legend();

plt.show()


