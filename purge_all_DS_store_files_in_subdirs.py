import os

print("Processing...")
# get the current working dir
mainDir = os.getcwd()

# walk all the subdirs
for root, dirs, files in os.walk(mainDir):
    for name in files:
        #print(name)
        if name.endswith(".DS_Store"):
            filePath = root + os.sep + name
            # DELETE FILE
            os.remove(filePath)            

#print("Done. Press ENTER to exit.")
#input()
