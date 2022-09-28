
# ----------------------------------------------------------
# Lab #4: Cyptrarithmetic Puzzle
# General cryptarithmetic puzzle solver.
#
# Date: 27-Sep-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

from csp import Constraint, CSP
from typing import Dict, List, Optional

class puzzleConstraint(Constraint[str, int]):
        def __init__(self, 
                     letras: list[str], 
                     sumados: list[str], 
                     sol: str) -> None:
            
             super().__init__(letras)
             self.letras: list[str] = letras
             self.sumados: list[str] = sumados
             self.sol: str = sol
             
        def to_numbers(self, palabra: str, valor_palabra: dict[str, int]):
            sum: int = 0
            base: int = 1
            for letter in reversed(palabra):
                sum += valor_palabra[letter] * base
                base *= 10
            return sum
        
        def verificaccion(self, asignacion: dict[str, int]):
            if len(set(asignacion.values())) < len(asignacion):
                return False
            if len(asignacion) < len(self.letras):
                return True
            suma: int = 0
            for palabra in self.letras:
                numero: int = self.to_numbers(palabra, asignacion)
                suma += numero
            return suma == self.to_numbers(self.letras[-1], asignacion)
        

def solve_cryptarithmetic_puzzle(
    sumados: list[str], 
    result: str) -> Optional[dict[str, int]]:
    
    for i  in range(len(sumados)):
        sumados[i] = sumados[i].upper()
    
    result = result.upper()
    
    variables: set[str] = set()
    for palabra in sumados:
        for letra in palabra:
            variables.add(letra)
    
    for letra in result:
        variables.add(letra.upper())
    
    letras_lista: list[str] = list(variables)
    letras_lista.sort()
    
    domains: dict[str, list[int]] = {var: list(range(10)) 
                                     for var in letras_lista}
    
    csp: CSP[str, int] = CSP(letras_lista, domains)
    csp.add_constraint(puzzleConstraint(letras_lista, sumados, result))
    sol: Optional[Dict[str, int]] = csp.backtracking_search()
    return sol
    
    



if '__main__' == __name__:
    solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes')