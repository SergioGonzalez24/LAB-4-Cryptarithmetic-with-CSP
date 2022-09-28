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
    
    # Constructor
    
    def __init__(self,
                 variables: list[str],
                 sumados: list[str],
                 resultado: str) -> None:
        
        super().__init__(variables)
        self.variables: list[str] = variables
        self.sumados = sumados
        self.expected_resultado: str = resultado
        
    # Convert a word into a number based on the sum of the values given on the dictionary
    # for each letter in the word.
    
    def to_number(self, palabra: str, valores_letra: dict[str, int]):
        
        sum: int = 0
        base: int = 1
        
        # Sum the values of the letters in the word.
        for letra in reversed(palabra):
            sum += valores_letra[letra] * base
            base *= 10
            
        # Return the sum of the values of the letters in the word.
        return sum
    
    # Check if condition is satisfied to return True or False.
    
    def satisfied(self, asignacion: dict[str, int]):
        
        # Check if all letters have a different value.
        if len(set(asignacion.values())) < len(asignacion):
            return False
        
        # Check if the first letter of the word is not 0.
        if len(asignacion) < len(self.variables):
            return True
        sum: int = 0
        
        # Sum the values of the letters in the words.
        for word in self.sumados:
            number: int = self.to_number(word, asignacion)
            sum += number
        
        # Return True if the sum of the values of the letters in the words is 
        # equal to the value of the letters in the result word.
        
        return sum == self.to_number(self.expected_resultado,
                                               asignacion)

# Solve a cryptarithmetic puzzle.

def solve_cryptarithmetic_puzzle(
        sumados: list[str],
        resultado: str) -> Optional[dict[str, int]]:
    
    # Create a list of all the letters in the words.
    for i in range(len(sumados)):
        sumados[i] = sumados[i].upper()

    resultado = resultado.upper()
    variables: set[str] = set()
    
    # Add the letters of the words to the list of variables.
    for palabra in sumados:
        for letra in palabra:
            variables.add(letra)
            
    # Add the letters of the result word to the list of variables.
    for letra in resultado:
        variables.add(letra.upper())
        
    # Create a list of all the possible values for each letter.
    variables_list: list[str] = list(variables)
    variables_list.sort()

    domains: dict[str, list[int]] = {var: list(range(10))
                                     for var in variables_list}
    
    csp: CSP[str, int] = CSP(variables_list, domains)
    
    # Add the constraint to the CSP.
    csp.add_constraint(PuzzleConstraint(variables_list, sumados, resultado))
    
    # Solve the CSP.
    sol: Optional[dict[str, int]] = csp.backtracking_search()
    
    # Return the solution.
    return sol


if __name__ == '__main__':
    print(solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes'))