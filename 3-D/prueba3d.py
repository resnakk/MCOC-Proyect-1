from matplotlib.pylab import *

a = 1.   # m, Largo del dominio
b = 0.5  # m, Alto del dominio
c = 0.6 # m, Ancho del dominio

Nx = 20 # Numero de intervalos en x, @5 cm
Ny = 10 # Numero de intervalos en y, @10 cm
Nz = 12 # Numero de intervalos en z, @5 cm
# Con este numero de intervalos, se esta generando un espacio vectorial en el que los puntos se encuentran a 5 cm de distancia (en planos 2-D)
# Son distintos para que los deltas sean iguales.

dx = a/Nx # Discretizacion espacial en x
dy = b/Ny # Discretizacion espacial en y
dz = c/Nz # Discretizacion espacial en z

h = dx
if dx != dy:
	print("ERORR 404: dx!= dy")
	exit(-1) # -1 le dice al sistema operativo que el programa fallo

u_k = zeros((Nx + 1, Ny + 1, Nz + 1), dtype = double)
u_k1 = zeros((Nx + 1, Ny + 1, Nz + 1), dtype = double)

# CB escenciales
u_k[:, :, :] = 20.

# Propiedades del hormigon
K = 116.     # m^2 / s, conductividad termica
c = 390.     # J / kg*C, calor especifico
rho = 7140.  # kg/m^3, densidad

#Arreglo de parametros
alpha_0 = 0.0001
dt = alpha_0*(c*rho*dx**2)/K
alpha = K*dt/(c*rho*dx**2)
dt = 60 # s

# Parametros para la modelacion de la temperatura ambiente segun el dia.
Tmax = 29.     # Temperatura maxima en el dia
Tmin = 13. 	   # Temperatura minima en el dia
hmax = 1260000 # Hora en que se alcanza la temperatura maxima. corresponde a las 15:00
hmin = 420000  # Hora en la que se alcanza la temperatura minima, corresponde a las 05:00 
# Para estos parametros se asumio el 10 de marzo del 2018. y se extrajo la informacion de las temperatura de AccuWeather, en San Carlos de Apoquindo.

A = (Tmax - Tmin)/2  # C
B = (Tmax + Tmin)/2  # C
b1 = (hmax + hmin)/2 # s
b2 = (hmax - hmin)   # s

#Parametros para la generacion de calor generacion de calor
Cc = 154    # kg, cantidad de cemento
Tc = 20     # C, Temperatura del concreto
Cr = 23     # C, Temperatura de referencia
R = 8.31    # J / mol*k, Ctte universal de los gases
E = 27000   # J / mol, Energia de activacion
H = 374.24  #J / kg, Hu*alpha_u; Hu: Total de calor generado al 100% de hidratacion; aplha_u: ultimo grado de hidratacion
beta = 1.05 # Pendiente de hidratacion
thau = 10.3 # Parametro de hidratacion

# Parametros para guardar las temperaturas de los puntos
dnext_t = 1800 # s
next_t = 0 # s

# Registro de temperaturas de puntos a lo largo
T_1 = []

# Registro de temperaturas puntos a lo ancho
T_10 = []

# Registro de temperaturas puntos a lo alto
T_5 = []
T_7 = []
T_9 = []
for tiempo in range(int32(3600*24*7)): # Simulacion de los primeros 7 dias
	# Avance del tiempo
	t = dt*(tiempo + 1)

	# CB Natural
	cte = tiempo % 86400 # Segundos de un dia
	if cte >= 1:
		u_a = A*sin(2*pi*((tiempo - c*86400) - b1)/(2*b2) + B)
	else:
		u_a = A*sin(2*pi*(tiempo - b1)/(2*b2) + B)
	# Esta funcion la sacamos de un paper, cuyo link se encuentra en el README
	# Este if es para hacer un ciclo entre los dias, para simplificar el problema.	
	
	for i in range(1, Nx - 1):
		for j in range(1, Ny - 1):
			for k in range(1, Nz - 1):

				# Laplaciano
				nabla_u_k = (u_k[i - 1, j, k] + u_k[i + 1, j, k] + u_k[i, j - 1, k] + u_k[i, j + 1, k] + u_k[i, j, k - 1] + u_k[i, j, k + 1] - 6*u_k[i, j, k])/h**2
				# Algoritmo de diferencias finitas 1-D para la difusion
				u_k1[i,j] = u_k[i,j] + alpha*nabla_u_k
	
	# CB Naturales
	# Para estas CB se asume que la cara abierta (la de arriba) es la u[:, Ny, :]
	u_k1[Nx, :, :] = u_k1[Nx - 1, :, :]
	u_k1[:, Ny, :] = u_k1[:, Ny - 1, :]
	u_k1[:, :, Nz] = u_k1[:, :, Nz - 1]
	u_k1[0, :, :] = u_k1[1, :, :]
	u_k1[:, :, 0] = u_k1[:, :, 1]  
	
	# Avanzar en la solucion
	u_k = u_k1
	# Guarddo de temperatura cada 30 minutos
	if t > next_t:
		next_t += dnext_t
		T_1.append([u_k[4,5,6], t])
		T_10.append([u_k[10,5,10], t])
		T_5.append([u_k[10,8,6], t])
		T_7.append([u_k[10,5,6], t])   
		T_9.append([u_k[10,2,6], t])

#Ploteo de los puntos 
xlabel('Tiempo (s)')
ylabel('Temperatura (C)')
title('Semana 1')















