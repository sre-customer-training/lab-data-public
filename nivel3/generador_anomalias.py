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
Generador de datos aleatorios de anomalias de latencia
"""
import pandas as pd
import numpy as np

def generar_datos_sucios():
    """
    Método de generación de datos aleatorios de latencia, incluye
    errores
    """
    # Usamos base aleatoria simple
    data = np.random.normal(100, 10, 200) # 200 datos normales
    df = pd.DataFrame(data, columns=['Latencia_ms'])

    # --- INYECTAR ANOMALÍAS ---

    # CASO 1: Error Técnico (Sensor roto)
    # Valores negativos o ceros imposibles en latencia
    df.loc[10, 'Latencia_ms'] = -50
    df.loc[20, 'Latencia_ms'] = -999

    # CASO 2: Incidente Real (Sobrecarga / DDoS)
    # Valores positivos extremadamente altos
    df.loc[50, 'Latencia_ms'] = 500  # 5x lo normal
    df.loc[51, 'Latencia_ms'] = 520
    df.loc[52, 'Latencia_ms'] = 480

    df.to_csv('../datos/datos_latencia_sucia.csv', index=False)
    print("✅ Archivo '../datos/datos_latencia_sucia.csv' generado con errores y crisis.")

if __name__ == "__main__":
    generar_datos_sucios()
