from Equation import Equation
import math
import sympy as sp


class EulerMejorado:
    def exact_solution(self, x):
        return math.exp(-0.2 + 0.2 * x**2)

    def euler_mejorado(self, function, x0, y0, x, h, tol=None):
        """
        Método de Euler mejorado (Heun) con criterio de tolerancia.
        :param function: Función que recibe (x, y) y devuelve la ecuación diferencial
        :param x0: Valor inicial de x
        :param y0: Valor inicial de y
        :param x: Valor final de x
        :param h: Tamaño del paso
        :param tol: Número de decimales de tolerancia para romper el ciclo
        :return: Lista con iteraciones, valores de x, valores de y y error absoluto
        """
        equation = Equation()
        parsed_equation = equation.parse_equation(function)
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
            
            k1 = f(x0, y)
            k2 = f(x0 + h, y + h * k1)
            
            y += (h / 2) * (k1 + k2)
            x0 += h  # Incrementar x0 con cada paso
            iteracion += 1
        
        return resultados
