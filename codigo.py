import math
import random

def energia_resorte(k, x):
    return (1 / 2) * k * x ** 2

def velocidad_inicial(k, x, m):
    energia = energia_resorte(k, x)
    v0 = math.sqrt(2 * energia / m)
    return v0

def tiempo_vuelo(h, g):
    return math.sqrt(2 * h / g)

def distancia(v0, t):
    return v0 * t

def main():
    k = 200
    m = 5 / 1000
    h = 10
    g = 9.81
    
    fuerza = float(input("Introduce la fuerza (en Newtons) para estirar el resorte: "))
    x = fuerza / k
    v0 = velocidad_inicial(k, x, m)
    t = tiempo_vuelo(h, g)
    alcance = distancia(v0, t)
    objetivo = random.uniform(5,100)
    
    print(f"\nDistancia al objetivo: {objetivo:.2f} metros")
    print(f"Alcance del proyectil: {alcance:.2f} metros")
    print(f"Fuerza aplicada al resorte: {fuerza} N")
    print(f"Masa del proyectil: {m*1000} gramos")
    
    if alcance >= objetivo:
        print("Objetvio alcanzado")
    else:
        print("EObjetivo no alcanzado.")

main()
