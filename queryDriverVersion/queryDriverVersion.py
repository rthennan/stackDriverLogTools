# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:14:52 2022

@author: Rajesh
Unwrap the json file to csv and also extracts the client driver details from the jsonPayload.source field
"""
try:
    import json #pip install simplejson
except:
    print('\nPackage "json" not found. Please install it by running "pip install simplejson" and re-run this code')
    exit()
    
try:
    import pandas as pd #pip install pandas
except:
    print('\nPackage "pandas" not found. Please install it by running "pip install pandas" and re-run this code')
    exit()    
    
try:
    from tkinter import Tk, filedialog #pip install tk
except:
    print('\nPackage "tkinter" not found. Please install it by running "pip install tk" and re-run this code')
    exit()    
from pathlib import Path 


def getClientDriver(inString):
    return inString.split('\t')[2]

print('Please select the query log json or csv file.')

try:
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askopenfilename(filetypes=[("json files", "*.json"), ("CSV file","*.csv"),("All Files", "*.*")])
    if filename == '':
        print('Unable to read the file or no file selected.')
        exit()     
    print(f'\nFile Selected -> {Path(filename).name}')

except Exception as e:
    print(f'\nUnable to read the file or no file selected. Exception -> {e}')
    exit()



fileExtension = filename.split('.')[-1]

if fileExtension == 'json':
    with open(filename) as json_file:
        jsonData = json.load(json_file)    
    logDF = pd.json_normalize(jsonData)
elif fileExtension == 'csv':
    logDF = pd.read_csv(filename)
else:
    print('\nInvalid File type/extension')

if 'jsonPayload.source' in logDF.columns:
    logDF['client_driver'] = logDF['jsonPayload.source'].apply(getClientDriver)
else:
    
    print('\n"jsonPayload.source" column missing. Cannot extract client_driver details' )
    
outputfile = f"{filename[:-5]+'_mod.csv'}"
logDF.to_csv(outputfile,index=False)

print(f'\nOutput file "{Path(outputfile).name}" created in the same location as the {fileExtension} file you had selected.')
