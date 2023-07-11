from transformacion.transformacion import *

def clean_code(text):
    text = str(text)
    parent_code = None
    if len(text) == 11:
        code = text[:5]
        parent_code = text[:1]
    else:
        code = text[:6]
        parent_code = text[:2]
    try:
        parent = df_parents[df_parents['Code_comm']==parent_code]['Description'].values[0]
    except:
        parent = None
    return (code,parent)