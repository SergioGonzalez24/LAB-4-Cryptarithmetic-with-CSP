# ----------------------------------------------------------
# Lab #4: Cyptrarithmetic Puzzle
# General cryptarithmetic puzzle solver.
#
# Date: 27-Sep-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

from typing import Optional
from csp import Constraint, CSP

class PuzzleConstraint(Constraint[str, int]):
    
    def __init__(self,
                 variables: list[str],
                 sumados: list[str],
                 resultado: str) -> None:
        
        super().__init__(variables)
        self.variables: list[str] = variables
        self.sumados = sumados
        self.expected_resultado: str = resultado

    def to_number(self, palabra: str, valores_letra: dict[str, int]):

        sum: int = 0
        base: int = 1
        for letra in reversed(palabra):
            sum += valores_letra[letra] * base
            base *= 10
        return sum

    def satisfied(self, asignacion: dict[str, int]):
   
        if len(set(asignacion.values())) < len(asignacion):
            return False
        if len(asignacion) < len(self.variables):
            return True
        sum: int = 0
        for word in self.sumados:
            number: int = self.to_number(word, asignacion)
            sum += number

        return sum == self.to_number(self.expected_resultado,
                                               asignacion)


def solve_cryptarithmetic_puzzle(
        sumados: list[str],
        resultado: str) -> Optional[dict[str, int]]:
    for i in range(len(sumados)):
        sumados[i] = sumados[i].upper()

    resultado = resultado.upper()
    variables: set[str] = set()
    for palabra in sumados:
        for letra in palabra:
            variables.add(letra)

    for letra in resultado:
        variables.add(letra.upper())

    variables_list: list[str] = list(variables)
    variables_list.sort()

    domains: dict[str, list[int]] = {var: list(range(10))
                                     for var in variables_list}
    

    csp: CSP[str, int] = CSP(variables_list, domains)
    csp.add_constraint(PuzzleConstraint(variables_list, sumados, resultado))
    sol: Optional[dict[str, int]] = csp.backtracking_search()

    return sol


if __name__ == '__main__':
    print(solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes'))