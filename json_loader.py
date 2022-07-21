import pandas as pd
import json

def loading(file):
  with open(file) as f:
    data = json.load(f)
  return pd.DataFrame(data)
 
data=loading(file)
