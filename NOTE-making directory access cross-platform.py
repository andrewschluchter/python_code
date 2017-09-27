import os

print("Processing...")

# get the current working dir
mainDir = os.getcwd()

# walk all the subdirs
for root, dirs, files in os.walk(mainDir):
    for name in files:
        # EXAMPLE CONDITION
        if name.endswith(".DS_Store"):
            filePath = root + os.sep + name
            # EXAMPLE OPERATION
            os.remove(filePath)            

# ENABLE DIRECT OUTPUT TO TERMINAL TO SHOW STATUS
#print("Done. Press ENTER to exit.")
#input()
