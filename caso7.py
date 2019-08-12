

from matplotlib.pylab import *


L = 1. #largo del dominio
n = 200 #numero intervalos
dx = L / n #discretizacion espacial

x = linspace(0, L, n + 1)
#condiciones iniciales del problema
def fun_u0(x):
	return 10*exp( - (x-0.5)**2/0.1**2)



u0 = fun_u0(x)
#creacion de nueva instancia
u_k = u0.copy()


#condiciones de borde
u_k[0] = 0.
u_k[n] = 40.

#temperatura en el tiempo k +1
u_km1 = u_k.copy()

#aluminio
dt = 0.001 #s, tiempo
K  = 237. #m2/s , conductividad termica
c = 900. #j/kgC , calor especifico
rho = 2698.4 #kg/m3 , densidad
alpha = K*dt/(c*rho*dx**2)


plot(x,u0, "k--")

k = 0
for k in range(10000):
	t = dt*k #tiempo
	#print("k=", k, " t= ", t)

	#loop en el espacio
	#condicion de borde
	u_km1[0] = 0.
	u_km1[n] = 40.
	for i in range(1,n):
		#algoritmo diferencias finitas
		u_km1[i] =  (t**0.5)*dt + u_k[i] + alpha*(u_k[i+1] - 2*u_k[i] + u_k[i-1])
	u_k = u_km1
	if k % 500 == 0:
		plot(x,u_k)

title("Grafico caso 7, Aluminio")
xlabel("Discretizacion espacial")
ylabel("Temperatura °C")
savefig("caso7.png")
show()