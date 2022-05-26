# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:14:52 2022

@author: Rajesh
Unwrap the json file to csv and also extracts the client driver details from the jsonPayload.source field
"""

import json
import pandas as pd #pip install pandas
from tkinter import Tk, filedialog #pip install tk
from pathlib import Path 

print('Please select the query log json file.')

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = filedialog.askopenfilename(filetypes=[("json files", "*.json"), ("All Files", "*.*")])
print(f'File Selected -> {Path(filename).name}')

def getClientDriver(inString):
    return inString.split('\t')[2]

with open(filename) as json_file:
    jsonData = json.load(json_file)
    
logDF = pd.json_normalize(jsonData)
logDF['client_driver'] = logDF['jsonPayload.source'].apply(getClientDriver)

outputfile = f"{filename[:-5]+'_mod.csv'}"
logDF.to_csv(outputfile,index=False)

print(f'Output created -> {Path(outputfile).name} in the same location as the json file you selected.')
