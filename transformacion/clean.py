from transformacion.transformacion import *
from transformacion.clean_code import clean_code

df_codes[['clean_code','parent_description']] = df_codes.apply(lambda x : clean_code(x['Code']),axis=1, result_type='expand')
df_codes = df_codes[df_codes['clean_code'].notnull()][['clean_code','Description','parent_description']]
df_codes['id_code']= df_codes.index +1
df_codes['clean_code'] = df_codes['clean_code'].astype('int64')