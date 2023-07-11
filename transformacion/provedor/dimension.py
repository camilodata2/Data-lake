from provedor.clean_provedor import *
from transformacion.merge import *

df_quantity =create_dimension(df_trades_clean['quantity_name'].unique(),'id_quantity')
df_flow =create_dimension(df_trades_clean['flow'].unique(),'id_flow')
df_year =create_dimension(df_trades_clean['year'].unique(),'id_year')

df_trades_clean = df_trades_clean.merge(df_quantity, how='left',left_on='quantity_name', right_on='values')

df_trades_clean = df_trades_clean.merge(df_flow, how='left',left_on='flow', right_on='values')

df_trades_clean = df_trades_clean.merge(df_year, how='left',left_on='year', right_on='values')

df_trades_clean['id_trades'] = df_trades_clean.index + 1

df_trades_final = df_trades_clean[['id_trades','trade_usd','kg','quantity','id_code','id_country','id_quantity','id_flow','id_year']].copy()

df_countries = df_countries[['id_country','alpha-3','country','region','sub-region']]

df_codes = df_codes[['id_code','clean_code','Description','parent_description']]



