# Nivel 1: Fundamentos de Estadística y Limpieza de Datos

## Escenario: Antes de ser SREs, somos analistas de RRHH. Tenemos una lista de empleados, pero la base de datos está "sucia": faltan edades, algunos no tienen cargo asignado y hay datos extraños

### Objetivos del Lab

1. Detectar datos faltantes (Null / NaN).
2. Decidir cómo limpiar: ¿Borrar o Rellenar (Imputar)?
3. Calcular Media vs. Mediana en un contexto humano.

#### Generador de Datos "Sucios" (Script)

Crea un archivo llamado generador_rrhh.py y ejecútalo. Este script crea intencionalmente huecos en la información. El archivo será almacenado en la ruta datos con el nombre datos_empleados.csv.
