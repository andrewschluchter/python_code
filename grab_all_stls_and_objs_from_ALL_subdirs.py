import os

# get the current working dir
mainDir = os.getcwd()

for root, dirs, files in os.walk(mainDir):
    for name in files:
        #print(name)
        if name.endswith((".stl", ".obj")):
            new_name = mainDir+'\\'+name
            #print(name)
            os.rename(root + os.sep + name, new_name)
