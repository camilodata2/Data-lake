from transformacion.provedor.dimension import *

df_trades_final.to_csv('target/trades.csv',index=False, sep='|')
df_countries.to_csv('target/countries.csv',index=False, sep='|')
df_codes.to_csv('target/codes.csv',index=False, sep='|')
df_quantity.to_csv('target/quantity.csv',index=False, sep='|')
df_flow.to_csv('target/flow.csv',index=False, sep='|')
df_year.to_csv('target/years.csv',index=False, sep='|')