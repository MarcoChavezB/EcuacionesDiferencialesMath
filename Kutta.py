import math
from Equation import Equation
import sympy as sp

class RungeKutta:

    def exact_solution(self, x):
        return math.exp(-0.2 + 0.2 * x**2)

    def rungeKutta(self, f, x0, y0, x, h):
        """
        Método de Runge-Kutta de 4to orden para resolver ecuaciones diferenciales ordinarias.
        :param f: Función que recibe (x0, y0, x, h) y devuelve la ecuación diferencial
        :return: Lista con iteraciones, valores de x, valores de y y error absoluto
        """
               
        equation = Equation()
        parsed_equation = equation.parse_equation(f)
        f = sp.lambdify(('x', 'y'), parsed_equation, 'numpy')

        n = int((x - x0) / h)
        y = y0
        resultados = []
        
        
        for i in range(n + 1):
            y_real = self.exact_solution(x0) 


            error_abs = abs(y_real - y)
            resultados.append((i, x0, y, y_real, error_abs))
            
            k1 = h * f(x0, y)
            k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * f(x0 + h, y + k3)
            
            y += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            x0 += h 
        
        return resultados

x0 = 1
y0 = 4
x = 2
h = 0.1
kutta = RungeKutta()
unparsed_equation = '-x^3+3x^2+2x+1' 
resultados = kutta.rungeKutta(unparsed_equation, x0, y0, x, h)

# Imprimir los resultados
print("Iteración | x | y aproximado | y real | Error absoluto")
for iteracion, x_val, y_aprox, y_real, error in resultados:
    print(f"{iteracion:9} | {x_val:.2f} | {y_aprox:.6f} | {y_real:.6f} | {error:.6f}")
