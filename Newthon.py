import sympy as sp
from Equation import Equation

class NewtonRaphson:
    @staticmethod
    def resolver(funcion, punto_inicial, tolerancia=1e-6, max_iter=100, decimales_tol=None):
        x = sp.symbols('x')
        parsed_function = Equation().parse_equation(funcion)
        derivada = sp.diff(parsed_function, x)
        f = sp.lambdify(x, parsed_function, 'numpy')
        f_prime = sp.lambdify(x, derivada, 'numpy')

        x_n = punto_inicial
        resultados = []

        for i in range(max_iter):
            f_x_n = f(x_n)
            f_prime_x_n = f_prime(x_n)

            # Si la derivada es demasiado pequeña, terminamos el proceso
            if abs(f_prime_x_n) < 1e-10:
                return []

            # Actualización de x_n con el método de Newton-Raphson
            x_n1 = x_n - f_x_n / f_prime_x_n

            resultados.append((i + 1, x_n, f_x_n, f_prime_x_n, x_n1))

            # Verificar criterio de tolerancia por número de decimales
            if decimales_tol is not None and round(abs(x_n1 - x_n), decimales_tol) == 0:
                break

            if abs(x_n1 - x_n) < tolerancia:
                break

            # Actualización de x_n para la siguiente iteración
            x_n = x_n1

        return resultados

