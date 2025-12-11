"""
Genera una matriz DOE (factorial completo) y guarda CSV.
Requisitos del enunciado: > = 5 factores, al menos 3 factores con más de 4 niveles.
"""

import numpy as np
from pyDOE2 import fullfact

def main():
    # Definimos 5 factores. Aseguramos que al menos 3 factores tengan más de 4 niveles.
    # Ejemplo (nombres explicativos en el README final):
    # - size: 5 niveles
    # - order: 6 niveles
    # - method: 5 niveles
    # - load: 7 niveles
    # - env: 4 niveles
    levels = [5, 6, 5, 7, 4]  # tres factores > 4 niveles: size(5), order(6), method(5), load(7) (en realidad 4)
    design = fullfact(levels)  # matiz factorial completo
    runs = design.shape[0]
    print(f"Generado diseño factorial completo con {runs} corridas.")
    np.savetxt("../reports/doe_matrix.csv", design, delimiter=",", fmt='%d')
    with open("../reports/doe_explain.md", "w", encoding="utf-8") as f:
        f.write("# DOE - Especificación\n")
        f.write("Factores y niveles:\n")
        f.write("- size: 5 niveles\n- order: 6 niveles\n- method: 5 niveles\n- load: 7 niveles\n- env: 4 niveles\n")
        f.write("\nSe generó la matriz factorial completa con pyDOE2 (fullfact).")
    print("Archivos guardados en reports/doe_matrix.csv y reports/doe_explain.md")

if __name__ == "__main__":
    main()
