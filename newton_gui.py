from Newthon import NewtonRaphson 

def calcular(self):
    funcion = self.entry_funcion.get()
    try:
        punto_inicial = float(self.entry_punto.get())
        resultado = NewtonRaphson.resolver(funcion, punto_inicial)

        if resultado and hasattr(resultado, 'json') and resultado.json:
            self.resultado_text.set(f"Resultado: {resultado.json['message']}")
        else:
            self.resultado_text.set("Error: No se recibió un resultado válido.")
    except ValueError:
        self.resultado_text.set("Error: Ingresa un número válido para x₀.")

