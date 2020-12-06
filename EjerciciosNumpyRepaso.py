import numpy as np
import random
import time
#Cómo agregar un borde (lleno de ceros) alrededor de una matriz existente
print("matriz con bordes ")
a=np.zeros((10,10))
a[1:-1,1:-1]=1
print(a)

#18.-Cree una matriz de 5x5 con valores 1,2,3,4 justo debajo de la diagonal
print("1.-matriz con valores debajo de la matriz")
b=np.diag(1+np.arange(4),k=-1)
print(b)

#19.-Cree una matriz de 8x8 y rellénela con un patrón de tablero de ajedrez
print("2.-tablero de ajedrez")
c=np.zeros((8,8),dtype=int)
c[1::2,::2]=1
c[::2,1::2]
print(c)

#20.-Considere una matriz de formas (6,7,8), ¿cuál es el índice (x, y, z) del elemento 100?
print("3.-posicion del elemento 100 en una matriz 3*3*3")
print(np.unravel_index(100,(6,7,8)))

#21Cree una matriz de tablero de ajedrez de 8x8 usando la función de mosaico
print("4.-tablero de ajedrez con funcion mosaico")
d=np.tile(np.array([[0,1],[1,0]]),(4,4))
print (d)

#22.-Normalizar una matriz aleatoria de 5x5
print("5.-Matriz aleatoria de 5*5 normalizada")
e=np.random.random((5,5))
emax, emin=e.max(), e.min()
e=(e-emin)/(emax-emin)   
print (e)

#23.-Multiplicar una matriz de 5x3 por una matriz de 3x2 (producto de matriz real)
print("6.-Multiplicacion matriz 5*3 con una matriz 3*2")
f=np.dot(np.ones((5,3)),np.ones((3,2)))
print(f)

#24.-Dada una matriz 1D, niegue todos los elementos que estén entre 3 y 8, en su lugar.
print("7.-numeros negandos entre 3-8")
g=np.arange(11)
g[(3<g)&(g<=8)]*=-1
print(g)

#26.-¿Cuál es el resultado del siguiente script?
print ("8.-Adivina cual es el resultado")
print(sum(range(5),-1))
from numpy import *
print ("El resultado es: ",sum(range(5),-1))

#33.-¿Cómo obtener las fechas de ayer, hoy y mañana?
print("9.-Fechas ayer, hoy y mañana")
ayer=np.datetime64('today','D')-np.timedelta64(1,'D')
hoy=np.datetime64('today','D')
maniana=np.datetime64('today','D')+np.timedelta64(1,'D')
print("Ayer: ",ayer)
print("Hoy: ",hoy)
print("Mañana: ", maniana)

#62.-Considerando dos matrices con forma (1,3) y (3,1), ¿cómo calcular su suma usando un iterador?
print("10.-Suma con iterador")
h=np.arange(3).reshape(3,1)
i=np.arange(3).reshape(1,3)
it=np.nditer([h,i,None])
for x,y,z in it: z[...]=x+y
print(it.operands[2])

#64.-Considere un vector dado, ¿cómo agregar 1 a cada elemento indexado por un segundo vector (tenga cuidado con los índices repetidos)?
print("11.-Agregar 1 a cada elemento indexado por un segundo vector")
j=np.ones(10)
k=np.random.randint(0,len(j),20)
j+=np.bincount(k,minlength=len(j))
print(j)

#67.-Considerando una matriz de cuatro dimensiones, ¿cómo obtener la suma sobre los dos últimos ejes a la vez?
print("12.-Suma de los dos ultimos ejes")
l=np.random.randint(0,10,(3,4,3,4))
suma=l.reshape(l.shape[:-2]+(-1,)).sum(axis=-1)
print("La suma es: ",suma)

#71.-Considere una matriz de dimensión (5,5,3), ¿cómo multiplicarla por una matriz con dimensiones (5,5)?
print("13.-Multiplicacion matriz [5,5,3] por una matriz [5,5]")
m=np.ones((5,5,3))
n=2*np.ones((5,5))
print("El resultado es: \n",m*n[:,:,None])

#72.-¿Cómo intercambiar dos filas de una matriz?
print("14.-Intercambio de 2 filas de una matriz")
o=np.arange(25).reshape(5,5)
print("Matriz original\n",o)
o[[0,1]]=o[[1,0]]
print("Matriz cambiada\n",o)

#74.-Dada una matriz C que es un bincount, ¿cómo producir una matriz A tal que np.bincount (A) == C?
print("15.-Resolucion")
p=np.bincount([1,1,2,3,4,4,6])
q=np.repeat(np.arange(len(p)),p)
print(q)