from time import time

# 1. Fibonacci con Memorización (Top-down)
memoria = {0: 1, 1: 1}

def fib_des(n):
    if n in memoria:
        return memoria[n]
    
    # Se calcula y se guarda en el diccionario para evitar re-cálculos
    memoria[n] = fib_des(n-1) + fib_des(n-2)
    return memoria[n]

# 2. Fibonacci Recursivo Simple
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)

# 3. Fibonacci Ascendente (Programación Dinámica / Bottom-up)
dp = [1, 1]

def fib_asc(n):
    if n == 0 or n == 1:
        return dp[n]
    
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2])
    return dp[n]

# --- Pruebas de tiempo ---

# Prueba con el método ascendente (Muy rápido)
t0 = time()
print(f"Resultado fib_asc(50): {fib_asc(50)}")
print(f"Tiempo fib_asc: {time() - t0:.8f} segundos")

# Prueba con el método recursivo simple 
# NOTA: fib(50) sin memorización tardará muchísimo (minutos o más). 
# Es recomendable probar con un número más bajo como 35.
t0 = time()
# print(f"Resultado fib(35): {fib(35)}") 
# print(f"Tiempo fib simple: {time() - t0:.8f} segundos")

# Prueba con el método de memorización (Top-down)
t0 = time()
print(f"Resultado fib_des(50): {fib_des(50)}")
print(f"Tiempo fib_des: {time() - t0:.8f} segundos")