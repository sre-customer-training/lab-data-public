# Source - https://github.com/sre-customer-training/lab1-estadistica-descriptiva

__author__ = "Andres M. Correa"
__copyright__ = "BSD 3-Clause License"
__credits__ = []
__license__ = "BSD"
__version__ = "3"
__maintainer__ = "Andres M. Correa"
__email__ = "amcorrea0@gmail.com"
__status__ = "Labs for SRE"


"""
Generador de datos de RRHH para laboratorio de fundamentos de analítica
de datos.
"""
import random
import pandas as pd
import numpy as np

def generar_datos_rrhh(n=200):
    """ Método para generación aleatoria de datos, incluyendo outliers y NaN """

    cargos = ['Desarrollador', 'SRE', 'Gerente', 'Analista', 'Diseñador', 'Soporte']

    data = []
    for i in range(n):
        # Generar edad (algunos muy jóvenes, otros mayores)
        edad = int(np.random.normal(35, 10))
        edad = max(18, min(65, edad)) # Limitar entre 18 y 65

        # Introducir un "Outlier" de salario (el CEO o un error de tipado)
        salario = np.random.randint(1000, 2000)
        if i <= 3:
            salario = 50000 # 4 outliers gigantes

        cargo = random.choice(cargos)

        # --- ENSUCIAR LOS DATOS ---
        # 10% de probabilidad de que falte la Edad
        if random.random() < 0.1:
            edad = np.nan

        # 5% de probabilidad de que falte el Cargo
        if random.random() < 0.05:
            cargo = np.nan

        data.append([f"Empleado_{i}", edad, cargo, salario])

    df = pd.DataFrame(data, columns=['Nombre', 'Edad', 'Cargo', 'Salario'])
    df.to_csv('../datos/datos_empleados.csv', index=False)
    print("✅ Archivo '../datos/datos_empleados.csv' generado con datos faltantes.")

if __name__ == "__main__":
    generar_datos_rrhh()
