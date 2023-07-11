import pandas as pd
import psycopg2
from Extraccion.cargue import *

def leer_tabla(conexion, trades):

    query = f"SELECT * FROM trades"
    try:
        df_trades = pd.read_sql_query(query, conexion)
        return df_trades
    except (Exception, psycopg2.Error) as error:
        print(f"Error al leer la tabla trades:", error)

# Ejemplo de uso
df_trade = leer_tabla(conexion, 'trades')

