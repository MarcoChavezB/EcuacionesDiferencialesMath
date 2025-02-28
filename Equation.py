from typing import Callable
import sympy as sp
import re

class Equation:
    _replacements = {
        '^': '**',  # Reemplazo para permitir el uso de "^"
    }
    
    def __init__(self, expression: str = '') -> None:
        self.expression = expression

    def parse_equation(self, fun) -> sp.Expr:
        if not isinstance(fun, str):
            raise TypeError("La función debe ser una cadena de texto.")

        # Reemplazar "^" por "**"
        for symbol, new in self._replacements.items():
            fun = fun.replace(symbol, new)
        
        # Expresión regular para agregar "*" entre números y variables (Ej: "2x" → "2*x")
        fun = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fun)

        return sp.sympify(fun)



    def parse_numpy_equation(self, fun: str) -> Callable[[float, float], float]:
        if not isinstance(fun, str):
            raise TypeError("La función debe ser una cadena de texto.")

        for symbol, new in self._replacements.items():
            fun = fun.replace(symbol, new)
        
        fun = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fun)

        vars = self.get_vars_in_equation(fun)

        x, y = sp.symbols(vars)

        expr = sp.sympify(fun)

        f_numpy = sp.lambdify((x, y), expr, 'numpy')

        return f_numpy  # Retorna una función de numpy




    def get_vars_in_equation(self, equation: str) -> str:
        letras = re.findall(r'[a-zA-Z]', equation)

        if len(letras) < 2:
            raise ValueError("La ecuación debe contener al menos dos variables diferentes.")

        return f"{letras[0]} {letras[1]}"

# Ejecutar la aplicación
if __name__ == "__main__":
    print(Equation().parse_equation('2x^4+2x-1'))
