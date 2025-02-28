import math
from Equation import Equation
import sympy as sp

def rungeKutta(f, x0, y0, x, h):
    """
    Método de Runge-Kutta de 4to orden para resolver ecuaciones diferenciales ordinarias.
    :param f: Función que recibe (x0, y0, x, h) y devuelve la ecuación diferencial
    :return: Lista con iteraciones, valores de x, valores de y y error absoluto
    """
    # Parámetros iniciales
    n = int((x - x0) / h)  # Número de iteraciones
    y = y0
    resultados = []
    
    def exact_solution(x):
        return (x - 2 + 3 * math.exp(-x / 2))
    
    for i in range(n + 1):
        y_real = exact_solution(x0)
        error_abs = abs(y_real - y)
        resultados.append((i, x0, y, y_real, error_abs))
        
        k1 = h * f(x0, y)
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x0 + h, y + k3)
        
        y += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h
    
    return resultados

# Definir la ecuación diferencial
def dydx(x, y):
    return (x - y) / 2

x0 = 1
y0 = 4
x = 2
h = 0.1

equation = Equation()
unparsed_equation = 'x * sqrt(y)'  # Cambié la ecuación a x * sqrt(y)
parsed_equation = equation.parse_equation(unparsed_equation)

# Convertir la ecuación simbólica en una función numérica
f = sp.lambdify(('x', 'y'), parsed_equation, 'numpy')

# Llamada a la función
resultados = rungeKutta(f, x0, y0, x, h)

# Imprimir los resultados
print("Iteración | x | y aproximado | y real | Error absoluto")
for iteracion, x_val, y_aprox, y_real, error in resultados:
    print(f"{iteracion:9} | {x_val:.2f} | {y_aprox:.6f} | {y_real:.6f} | {error:.6f}")
