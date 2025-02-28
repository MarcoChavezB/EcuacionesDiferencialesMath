
import sympy as sp
from Equation import Equation
from NewtonModel import NewtonRaphsonResponse, IterationData
from flask import jsonify

class NewtonRaphson:
    @staticmethod
    def resolver(funcion, punto_inicial, tolerancia=1e-6, max_iter=100):
        x = sp.symbols('x')
        parsed_function = Equation().parse_equation(funcion)
        derivada = sp.diff(parsed_function, x)
        f = sp.lambdify(x, parsed_function, 'numpy')
        f_prime = sp.lambdify(x, derivada, 'numpy')

        x_n = punto_inicial
        iterations = []

        for i in range(max_iter):
            f_x_n = f(x_n)
            f_prime_x_n = f_prime(x_n)

            if abs(f_prime_x_n) < 1e-10:
                response = NewtonRaphsonResponse(
                    success=False,
                    message="Derivada demasiado pequeña. El método podría no converger.",
                    iterations=[],
                    num_iteration=0,
                    result=None
                )
                return jsonify(response.dict())  # Convertir a diccionario antes de devolver

            x_n1 = x_n - f_x_n / f_prime_x_n

            iterations.append(IterationData(
                iteration=i+1,
                x_n=x_n,
                f_x_n=f_x_n,
                f_prime_x_n=f_prime_x_n,
                x_n1=x_n1
            ))

            if abs(x_n1 - x_n) < tolerancia:
                response = NewtonRaphsonResponse(
                    success=True,
                    message=f"Convergió después de {i+1} iteraciones.",
                    iterations=iterations,
                    num_iteration=len(iterations),
                    result=x_n1
                )
                return jsonify(response.dict()) 

            x_n = x_n1

        response = NewtonRaphsonResponse(
            success=False,
            message=f"No se alcanzó la convergencia después de {max_iter} iteraciones.",
            iterations=iterations,
            num_iteration=len(iterations),
            result=None
        )
        return jsonify(response.dict())  # Convertir a diccionario antes de devolver
