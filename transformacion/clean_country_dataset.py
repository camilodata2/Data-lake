from transformacion.transformacion import *

df_countries = df_countries[['alpha-3','country','region','sub-region']]
df_countries = df_countries[df_countries['alpha-3'].notnull()]
df_countries['id_country']=df_countries.index +1
