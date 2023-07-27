import pandas as pd
import json
from tqdm import tqdm
with open(file) as f:
        data = json.load(f)
data=pd.DataFrame(data)
data = data[data['Skipped']==False]
data= data.reset_index(drop=True)
