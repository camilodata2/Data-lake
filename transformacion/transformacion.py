import pandas as pd 


df_countries = pd.read_json('/home/camilo/etl/Extraccion/country_data.json')
df_codes = pd.read_csv('/home/camilo/etl/Extraccion/hs_codes.csv')

df_parents = df_codes[df_codes['Level']==2].copy()

df_codes = df_codes[df_codes['Code_comm'].notnull()]
