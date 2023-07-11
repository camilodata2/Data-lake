import csv
import sys
import pandas as pd

def load_file(path):
    datos=[]
    with open(path,'r',newline='') as file:
        reader=csv.reader(file)
        try:
            for row in reader:
                datos.append(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file, reader.line_num, e))
    
    return datos

path='/home/camilo/etl/Extraccion/hs_codes.csv'
datos_csv=load_file(path)
for row in  datos_csv:
    print(row)


def convertir_csv_to_parquet(archivo_csv,archivo_parquet):
    datos=pd.read_csv('/home/camilo/etl/Extraccion/hs_codes.csv')
    datos.to_parquet(archivo_parquet,engine='pyarrow',compression='gzip')


archivo_csv='/home/camilo/etl/Extraccion/hs_codes.csv'
archivo_parquet='hs_codes.parquet'
convertir_csv_to_parquet(archivo_csv,archivo_parquet)

