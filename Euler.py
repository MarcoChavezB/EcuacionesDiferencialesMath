from Equation import Equation
import math
import sympy as sp

class EulerMejorado:

    def exact_solution(self, x):
        return math.exp(-0.2 + 0.2 * x**2)

    def euler_mejorado(self, function, x0, y0, x, h):
        """
        Método de Euler mejorado (Heun) para resolver ecuaciones diferenciales ordinarias.
        :param f: Función que recibe (x, y) y devuelve la ecuación diferencial
        :param x0: Valor inicial de x
        :param y0: Valor inicial de y
        :param x: Valor final de x
        :param h: Tamaño del paso
        :return: Lista con iteraciones, valores de x, valores de y y error absoluto
        """
        equation = Equation()
        parsed_equation = equation.parse_equation(function)
        f = sp.lambdify(('x', 'y'), parsed_equation, 'numpy')

        n = int((x - x0) / h)
        y = y0
        resultados = []
        
        
        for i in range(n + 1):
            y_real = self.exact_solution(x0) 
            error_abs = abs(y_real - y)
            resultados.append((i, x0, y, y_real, error_abs))
            
            k1 = f(x0, y)
            k2 = f(x0 + h, y + h * k1)
            
            y += (h / 2) * (k1 + k2)
            x0 += h  
        
        return resultados

x0 = 1
y0 = 4
x = 2
h = 0.1

euler = EulerMejorado()
unparsed_equation = '-x^3+3x^2+2x+1' 
resultados = euler.euler_mejorado(unparsed_equation, x0, y0, x, h)

# Imprimir los resultados
print("Iteración | x | y aproximado | y real | Error absoluto")
for iteracion, x_val, y_aprox, y_real, error in resultados:
    print(f"{iteracion:9} | {x_val:.2f} | {y_aprox:.6f} | {y_real:.6f} | {error:.6f}")
