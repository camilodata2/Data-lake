import pandas as pd

def create_dimension(data, id_name):
    list_keys = []
    value = 1
    for _ in data:
        list_keys.append(value)
        value +=1
    return pd.DataFrame({id_name:list_keys, 'values':data})