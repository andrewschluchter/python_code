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
print("mainDir:")
print(mainDir)
print("Processing...")

# walk all the subdirs
for root, dirs, files in os.walk(mainDir):
    for name in files:
        #print(name)
        if name.endswith((".dicom", ".dcm")):
            dcmFile = root + os.sep + name
            newFile = mainDir + os.sep + name

            # Set Series Description field
            #print("step _")
            # ERROR HANDLER
            try:
                ds = dicom.read_file(dcmFile)
                ds.SeriesDescription = "OVERRIDE"
            except:
                print("Error log: Could not find Series Description field in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break
            
            """
            print("dcmFile:")
            print(dcmFile)
            print("newFile:")
            print(newFile)
            input()
            
            print("root:")
            print(root)
            print("dirs:")
            print(dirs)
            print("files:")
            print(files)
            input()
            """
            os.rename(dcmFile, newFile)


print("Done. Press ENTER to exit.")
input()
