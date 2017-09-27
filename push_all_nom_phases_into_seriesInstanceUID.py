import dicom, os

# EXAMPLE READ
#ds = dicom.read_file("IM-0001-0001-0001.dcm")
#print(ds)

#PY3 VERSION COMMANDS
#print(list(ds.keys())[0])      # key of "first" element
#print(list(ds.values())[0])    # value of "first" element
#print(list(ds.items())[0])     # (key, value) tuple of "first" element

#BOTH OF THESE COMMANDS PRINT THE SAME THING!
#print(ds.PatientsName)
#print(ds[0x10,0x10].value)

# Example command to change field entries
#ds.PatientID = "8675309"


#--------------------------------------------------------------------

# get the current working dir
mainDir = os.getcwd()

print("Processing...")

# walk all the subdirs
for root, dirs, files in os.walk(mainDir):
    for name in files:
        #print(name)
        if name.endswith((".dicom", ".dcm")):
            dcmFile = root + os.sep + name
            #print(dcmFile)
            skip_flag = 0

            # Read file
            #print("step 1")
            # ERROR HANDLER
            try:
                ds = dicom.read_file(dcmFile)
            except:
                print("Error log: Invalid or corrupted file: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break
            
            # Read Acquisition Date
            #print("step _")
            # ERROR HANDLER
            try:
                phaseValue = ds.NominalPercentageofCardiacPhase
            except:
                print("Error log: Could not find Nominal Percentage of Cardiac Phase field in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break
            
            # Set Series Instance UID field
            #print("step _")
            # ERROR HANDLER
            try:
                ds.SeriesInstanceUID = str(phaseValue)
            except:
                print("Error log: Could not find Series Instance UID field in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            # Set Series Description field
            #print("step _")
            # ERROR HANDLER
            try:
                ds.SeriesDescription = "Cardiac Phase %: "+str(phaseValue)
            except:
                print("Error log: Could not find Series Description field in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            #print("step ?")
            # Write the file
            if skip_flag == 0:
                #print(root)
                ds.save_as(dcmFile)
                #newPath = os.path.join(root, str(phaseValue))
                #if not os.path.exists(newPath):
                #    os.makedirs(newPath)                            
                #newDcmFile = os.path.join(newPath, name)
                #ds.save_as(newDcmFile)

print("Done. Press ENTER to exit.")
input()
