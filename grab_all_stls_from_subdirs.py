import glob, os, os.path, copy

# get the current working dir
mainDir = os.getcwd()

# get the subdirectories
subdirs = os.listdir()
#print(subdirs)

# remove all ".py" entries
dirList = [ f for f in os.listdir(".") if f.endswith(".py") ]
for f in dirList:
    subdirs.remove(f)
#print(subdirs)

# for each subdirectory, go into the dir and get a list of the stl files
for subdir in subdirs:
    thisDir = mainDir+'\\'+subdir
    #print(thisDir)
    os.chdir(thisDir)

    # for each stl file found, rename it to move it to the main folder
    fileList = [ f for f in os.listdir(".") if f.endswith(".stl") ]
    for f in fileList:
        newDir = mainDir+'\\'+f
        os.rename(f, newDir)

    # and go back to the main directory, to go into the next subdir
    os.chdir(mainDir)
