import math
from Equation import Equation
import sympy as sp

class RungeKutta:

    def exact_solution(self, x):
        return math.exp(-0.2 + 0.2 * x**2)

    def rungeKutta(self, f, x0, y0, x, h, tol=None):
        """
        Método de Runge-Kutta de 4to orden con criterio de tolerancia.
        :param f: Función que recibe (x0, y0, x, h) y devuelve la ecuación diferencial
        :param x0: Valor inicial de x
        :param y0: Valor inicial de y
        :param x: Valor final de x
        :param h: Tamaño del paso
        :param tol: Número de decimales de tolerancia para romper el ciclo
        :return: Lista con iteraciones, valores de x, valores de y y error absoluto
        """
        equation = Equation()
        parsed_equation = equation.parse_equation(f)
        f = sp.lambdify(('x', 'y'), parsed_equation, 'numpy')

        y = y0
        resultados = []
        iteracion = 0
        
        while x0 <= x:
            y_real = self.exact_solution(x0)
            error_abs = abs(y_real - y)
            resultados.append((iteracion, x0, y, y_real, error_abs))
            
            # Verificar criterio de tolerancia
            if tol is not None and round(error_abs, tol) == 0:
                break
            
            k1 = h * f(x0, y)
            k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * f(x0 + h, y + k3)
            
            y += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            x0 += h  
            iteracion += 1
        
        return resultados

