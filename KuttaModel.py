from typing import List, Optional
from pydantic import BaseModel
from sympy import real_root

class IterationData(BaseModel):
    iteration: int
    x_n: float
    y_n: float

class Kutta4Response(BaseModel):
    success: bool
    message: str
    iterations: Optional[List[IterationData]] = []
    num_iteration : int
