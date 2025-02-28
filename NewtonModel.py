import sympy as sp
from pydantic import BaseModel
from typing import Optional, List

# Definimos los modelos de respuesta
class IterationData(BaseModel):
    iteration: int
    x_n: float
    f_x_n: float
    f_prime_x_n: float
    x_n1: float

class NewtonRaphsonResponse(BaseModel):
    success: bool
    message: str
    iterations: Optional[List[IterationData]] = []
    result: Optional[float] = None
    num_iteration: int
