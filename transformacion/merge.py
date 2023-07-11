from transformacion.transformacion import *
from Extraccion.read_table import *

df_trades_clean = df_trade.merge(df_codes[['clean_code','id_code']],how='left', left_on='comm_code',right_on='clean_code')

df_trades_clean = df_trade.merge(df_countries[['alpha-3','id_country']],how='left', left_on='country_code',right_on='alpha-3')

df_trades_clean