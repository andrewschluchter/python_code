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

# Give shpiel. Ask for the new Patient Name and Patient ID
print("")
print("SCHLUCHTER'S PY-NONYMIZER")
print("--------------------------")
print("Expect program to take about 22 seconds per 1,000 files. Mileage WILL vary.")
print("DO NOT TERMINATE SCRIPT BEFORE COMPLETION, OR A FILE MAY BECOME CORRUPTED!")
print("")
print("Enter prefix (such as \"CVC\", or \"TAVR\") for Patient Name and ID (MRM): ")
prefix = input()
print("Processing...")

# get the current working dir
mainDir = os.getcwd()

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

            """
            # Read Acquisition DateTime (only sometimes filled out!)
            #print("step 4")
            # ERROR HANDLER
            try:
                ds.PatientID = newValue
            except:
                print("Error log: Could not find Patient ID in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break
            """

            # Remove Birth Date
            #print("step _")
            # ERROR HANDLER
            try:
                ds.PatientBirthDate = ''
            except:
                print("No birthday present in: ")
                print(dcmFile)
                #break
            
            # Read Acquisition Date
            #print("step _")
            # ERROR HANDLER
            try:
                dateValue = ds.AcquisitionDate
                #print(dateValue)
            except:
                print("Error log: Could not find AcquisitionDate in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            # Read Acquisition Time
            #print("step _")
            # ERROR HANDLER
            try:
                fullTimeValue = ds.AcquisitionTime
                #print(fullTimeValue)
                timeValue = fullTimeValue.partition(".")[0]
                #print(timeValue)
            except:
                print("Error log: Could not find AcquisitionTime in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            # Concatenate values to form new suffix
            #print("step _")
            # ERROR HANDLER
            try:
                strDate = str(dateValue)
                strTime = str(timeValue)
                newValue = prefix+strDate+strTime
            except:
                print("Math Error: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            # Read Patient's Name field
            #print("step _")
            # ERROR HANDLER
            try:
                ds.PatientsName = newValue
            except:
                print("Error log: Could not find Patient Name in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            # Set Patient ID field
            #print("step _")
            # ERROR HANDLER
            try:
                ds.PatientID = newValue
            except:
                print("Error log: Could not find Patient ID in: ")
                print(dcmFile)
                print("Skipping file. Still processing...")
                skip_flag = 1
                #break

            #print("step ?")
            # Write the file
            if skip_flag == 0:
                ds.save_as(dcmFile)
                #print("step ?")

print("Done. Press ENTER to exit.")
input()
