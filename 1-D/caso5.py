from matplotlib.pylab import *

l = 1.  # Largo dell dominio
n = 100  # Numero de intervalos
dx = l / n  # Discretizacion espa bcial

# Vector con todos los x.. puntos del espacio
x = linspace(0, l, n + 1)


# COndicion Inicial
def f_u0(x):
    return 10 * exp(-(x - 0.5) ** 2 / 0.1 ** 2)


u0 = f_u0(x)
K = 0

# creando el vector de solucion u
u_k = u0.copy()  # Crea una nueva instancia del vector en la memoria

# Condiiones de borde escenciales
u_k[0] = 0.
u_k[n] = 20.

# Temperatura en el tiempo k + 1
u_k1 = u_k.copy()

dt = 1.
K = 79.5
c = 450.
rho = 7800.
alpha = K * dt / (c * rho * dx ** 2)

# Loop en el tiempo
plot(x, u0, "k--")

for k in range(7000):
    t = dt * k
    # Loop en el espacio i = 1 ... n - 1; u_k1[0] = 0; u_k1[n] = 20
    # Condicion de borde
    u_k[0] = 20
    u_k[n] = 20

    for i in range(1, n):
        # Algoritmo de diferencias finitas 1-D para la difusion
        u_k1[i] = u_k[i] + alpha * (u_k[i + 1] - 2 * u_k[i] + u_k[i - 1])
    # Avanzar en la solucion
    u_k = u_k1
    if k % 200 == 0:
        plot(x, u_k)

plot(x, u0)
plot(x, u_k)
title("Grafico Caso 5, Hierro")
xlabel("Discretización espacial")
ylabel("Temperatura °C")
savefig("caso5.png")
