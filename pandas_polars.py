"""
# ---------------------------------------------------------
# LAB 0: INTRODUCCIÓN A LAS ESTRUCTURAS DE DATOS
# ---------------------------------------------------------
"""

import pandas as pd
import polars as pl

print("--- 1. CREANDO UNA SERIE (Una columna) ---")
# Imagina que estos son tiempos de latencia de 3 requests
latencias = pd.Series([120, 135, 98], name='Latencia_ms')
print(latencias)
print("\nNota como Python le asignó un índice automático (0, 1, 2)")

print("\n--- 2. CREANDO UN DATAFRAME (Una tabla) ---")
# Creamos un diccionario (clave: valor) y lo convertimos a tabla
data = {
    'Servicio': ['Auth', 'Pagos', 'Inventario', 'Auth'],
    'Status':   [200, 200, 500, 403],
    'Latencia': [120, 135, 980, 45]
}

df_pandas = pd.DataFrame(data)
print("Objeto DataFrame de PANDAS:")
print(df_pandas)

print("\n--- 3. OPERACIONES BÁSICAS (Slicing) ---")
# Seleccionar solo una columna
columna = df_pandas['Status']
print(f"Tipo de objeto columna: {type(columna)}") # Verás que es una Series

# Seleccionar una fila (por índice)
fila = df_pandas.iloc[2] # Fila índice 2 (Inventario)
print(f"\nDatos de la fila 2:\n{fila}")

print("\n--- 4. EL RETADOR: POLARS (Rust Speed) ---")
# La sintaxis es muy similar para crear, pero Polars muestra
# los tipos de datos (str, i64) explícitamente
df_polars = pl.DataFrame(data)
print(df_polars)

print("\n💡 TIP SRE:")
print("Pandas es suficiente para analítica del día a día (hasta ~1GB de datos).")
print("Si analizas logs masivos de todo un mes, Polars procesará los datos 10x-50x más rápido.")
