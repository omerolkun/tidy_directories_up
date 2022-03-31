import os
from os import listdir
from os.path import isfile, join
import datetime

mypath = #the path where you wants to apply the move_file 
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]


file_number_in_directory = len(onlyfiles)


if file_number_in_directory > 10:
    date = datetime.datetime.now()
    new_dir_name = date.strftime("%x").replace("/",".")
    new_dir_path = f"{mypath}/{new_dir_name}"
    

    try:
        os.makedirs((new_dir_path), exist_ok = True)
        
    except OSError as error:
        print("Directory  can not be created")

    for i in range(file_number_in_directory):
        os.rename(f"{mypath}/{onlyfiles[i]}", f"{new_dir_path}/{onlyfiles[i]}")

    
