# This script is designed to do the following:
# 1. Put this script in the folder intended to house all stl files of a patient
# 2. take the name of the current patient, go into the meshes folder, and go into the directory of the same patient
# 3. grab all stl files in the directory and all subdirectories and put them in the main directory

import glob, os, os.path, copy

mainDir = os.getcwd()
#print(mainDir)
#note: Z:\projects\Andrew\LAA Research\LAA_meshes\ is the 43-character string used below
#note: Z:\projects\Andrew\LAA Research\ is the 32-character string used below
active_patient = mainDir[43:]
#print(active_patient)
patient_root_dir = mainDir[:32]
#print(patient_root_dir)
grabbing_folder = patient_root_dir + "LAA_MPRs\\" + active_patient
#print(grabbing_folder)

#get all stl files in all subdirectories
# NOTE: An an example, if you want to get every .txt file under PATH you can use PATH + '/**/*.txt':
files = [file for file in glob.glob(grabbing_folder + '/**/*.stl', recursive=True)]
#print(files)
#print(len(files))
for file in files:
    file_name = file[-6:]
    print(file_name)
    newDir = mainDir + '\\' + file_name
    os.rename(file, newDir)

