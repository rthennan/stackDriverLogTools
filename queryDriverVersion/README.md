This script works on CSV and json log files downloaded from Google Stackdriver logs.  
If you select a json logs file the script unwraps it into a CSV file and also extracts the client driver details as a separate column for ease of analysis.  
If you select a CSV log file, a column with just the driver details is added.  
Just run the script and select the json or CSV file when prompted.  

Dependenices:
- Pandas - pip install pandas
- Tkinter - pip install tk
