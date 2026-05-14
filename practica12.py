from fibonacci_des import fib, fib_des, fib_asc
from time import time
import matplotlib as plt

tiempo_asc = []
tiempo_des = []
tiempo_rec = []

for i in range(1, 41):
    t0 = time()
    fib_des(i)
    tiempo_des.append(roud(time()-t0, 6))

    t0 = time()
    fib_asc(i)
    tiempo_asc.append(roud(time()-t0, 6))

datos = []
for i in range(1,41):
    datos.append(i)

fig, ax, plt.subplots()
ax.plot(datos, tiempo_asc, label = "fib_des", marker = "*", color= "r")
ax.plot(datos, tiempo_asc, label = "fib_asc", marker = "o", color= "g")
ax.set_xlabel("datos")
ax.set_ylabel("tiempo")
ax.grid(true)
ax.legend(loc = 2)

plt.title("tiempo de ejecicion")
plt.show
