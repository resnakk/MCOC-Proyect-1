from matplotlib.pylab import *

a = 1. #Ancho del dominio
b = 1. #Largo del dominio
c = 1. #Alto del dominio

Nx = 6 #Numero de intervalos en x
Ny = 6 #Numero de intervalos en y
Nz = 6 #Numero de intervalos en z

dx = a/Nx #Discretizacion espacial en x
dy = b/Ny #Discretizacion espacial en y
dz = c/Nz #Discretizacion espacial en z

h = dx
if dx != dy:
	print("ERORR!!!!")
	exit(-1) #-1 le dice al sistema operativo que el programa fallo

u_k = zeros((Nx + 1, Ny + 1, Nz + 1), dtype = double)
u_k1 = zeros((Nx + 1, Ny + 1, Nz + 1), dtype = double)

#Condiciones de borde escenciales iniciales
u_k[:,:,:] = 20.

dt = 0.2  # segundos
K = 116.  # conductividad termica
c = 390.  # calor especifico
rho = 7140.  # densidad
alpha = K * dt / (c * rho * dx ** 2)

#Parametros para la modelacion de la temperatura ambiente segun el dia. Esta funcion la sacamos de un paper, cuyo link se encuentra en el README
#Para estos parametros se asumio el 10 de marzo del 2018. y se extrajo la informacion de las temperatura de AccuWeather, en dichos dias, en San Carlos de Apoquindo

Tmax = 29 #Temperatura maxima en el dia
Tmin = 13 #Temperatura minima en el dia
hmax = 15 #Hora en que se alcanza la temperatura
hmin = 5  #Hora en la que se alcanza la temperatura minima 

A = (Tmax - Tmin)/2
B = (Tmax + Tmin)/2
b1 = (hmax + hmin)/2
b2 = (hmax - hmin)

for tiempo in range(1):
	t = dt*(tiempo + 1)
	u_a = A*sin(2*pi*(tiempo - b1)/(2*b2) + B)
	for i in range(1, Nx - 1):
		for j in range(1, Ny - 1):
			for k in range(1, Nz - 1):
				#Laplaciano
				nabla_u_k = (u_k[i - 1, j, k] + u_k[i + 1, j, k] + u_k[i, j - 1, k] + u_k[i, j + 1, k] + u_k[i, j, k - 1] + u_k[i, j, k + 1] - 6*u_k[i, j, k])/h**2
				# Algoritmo de diferencias finitas 1-D para la difusion
				u_k1[i,j] = u_k[i,j] + alpha*nabla_u_k
	#CB Natural
	#Para estas condiciones de borde asumi como que la cara abierta (la de arriba) es la 
	u_k1[Nx, :, :] =  u_k1[Nx - 1, :, :]
	u_k1[:, Ny, :] =  u_k1[:, Ny - 1, :]
    u_k1[:, :, Nz] =  u_k1[:, :, Nz - 1]
    u_k1[0, :, :] = u_k1[1, :, :]
    u_k1[:, :, 0] = u_k1[:, :, 1]   
	
	# Avanzar en la solucion
	u_k = u_k1



#du/dn = a
#du/dn = alpha(u - ua)
