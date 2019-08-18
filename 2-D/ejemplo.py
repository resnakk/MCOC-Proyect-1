#Difusion 1-D: Caso 1: Ti = 0, Tf = 20
from matplotlib.pylab import *
a = 1. #Ancho del dominio
b = 1. #Largo dell dominio
Nx = 6 #Numero de intervalos en x
Ny = 6 #Numero de intervalos en y
dx  = a/Nx #Discretizacion espacial en x
dy = b/Ny #Discretizacipn espacial en y

h = dx
if dx != dy:
	print("ERORR!!!!")
	exit(-1) #-1 le dice al sistema operativo que el programa fallo
#def coordS(i,j):
#	return dx*i, dy*j
#x, y = coords(4, 2)
coords = lambda i, j : (dx*i, dy*j)
x, y = coords(4, 2)
print("x = ", x)
print("y = ", y)

u_k = zeros((Nx + 1, Ny + 1), dtype = double)
u_k1 = zeros((Nx + 1, Ny + 1), dtype = double)

#Buena idea definir expreciones con nombres expresivos
def goodprint(u):
	print(u.T[Nx::-1,:])

def goodImshow(u):
	imshow(u.T[Nx::-1,:])
u_k[0,:] = 20.
u_k[:,0] = 20.
print (u_k) #eje y invertido
print (u_k.T[Nx::-1,:]) #eje y normal
figure()
goodImshow(u_k)
colorbar()
show()

dt = 0.2  # segundos
K = 116.  # conductividad termica
c = 390.  # calor especifico
rho = 7140.  # densidad
alpha = K * dt / (c * rho * dx ** 2)

for k in range(1):
	t = dt*(k + 1)
	for i in range(1, Nx - 1):
	#u_k[0, :] = 20.
	#u_k[:, 0] = 20.
		for j in range(1, Ny - 1):
			#Laplaciano
			nabla_u_k = (u_k[i-1,j] + u_k[i + 1,j] + u_k[i,j+1] + u_k[i, j-1] - 4*u_k[i,j])/h**2
			# Algoritmo de diferencias finitas 1-D para la difusion
			u_k1[i,j] = u_k[i,j] + alpha*nabla_u_k
	#CB Natural
	u_k1[Nx, :] =  u_k1[Nx - 1, :]
	u_k1[:, Ny] =  u_k1[:, Ny -1]	        
	# Avanzar en la solucion
	u_k = u_k1
	if k % 200 == 0:
		goodImshow(u_k)
		savefig()
