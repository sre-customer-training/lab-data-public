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
Generador aleatorio de ventas para 1 año
"""
#from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def generar_ventas_anuales():
    """
    Método de generación aleatorio de ventas
    """
    # Fechas: 1 año completo
    fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

    data = []
    for fecha in fechas:
        # Base de venta
        venta_base = 1000

        # Estacionalidad: Fin de semana (5=Sab, 6=Dom) vende 50% más
        if fecha.weekday() >= 5:
            venta_base *= 1.5

        # Tendencia: Las ventas suben ligeramente a fin de año
        mes = fecha.month
        venta_base += (mes * 50)

        # Ruido aleatorio (Variabilidad normal del negocio)
        ruido = np.random.normal(0, 200) # Media 0, Desviación 200
        venta_final = max(0, int(venta_base + ruido))

        data.append([fecha, venta_final])

    df = pd.DataFrame(data, columns=['Fecha', 'Ventas'])
    df.to_csv('../datos/datos_ventas_anual.csv', index=False)
    print("✅ Archivo '../datos/datos_ventas_anual.csv' generado (365 días).")

if __name__ == "__main__":
    generar_ventas_anuales()
