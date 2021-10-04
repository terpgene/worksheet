# Script written by Gene Essel 10/3/2021
# Converting and merging package list data after scraping data from remote instances
import os
import glob
import pandas as pd
from datetime import date


cwd = os.getcwd() 
files = os.listdir(cwd)
today = date.today()

# change the combined filename to suit
writer = pd.ExcelWriter('combined-workbook-{}.xlsx'.format(today), engine='xlsxwriter')

list_of_files = glob.glob(os.path.join(cwd, "*.csv"))
# loop over the list of .csv files and read the files into panda to build 
# the combined files

for f in list_of_files:
    df = pd.read_csv(f)
    f = f[:-4]  # strip the .csv from the end of the filename
    df.to_excel(writer, sheet_name=os.path.basename(f), index=False)
writer.save()

