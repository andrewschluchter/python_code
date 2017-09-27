import os, glob, os.path, copy
# OPERATOR ACTION: place this script in the folder in question, and run script

# Get a list called "files_list" of all files and folders
files_list = os.listdir()

# remove all .py, .DS_Store, and .stl file(s) from files_list
dirList = [ f for f in os.listdir(".") if f.endswith(".py") or f.endswith(".stl") or f.endswith(".DS_Store")]
for f in dirList:
    files_list.remove(f)
# NOTE: making 2nd list so that parsing can quickly be done twice (more efficient)
files_list_dup = copy.deepcopy(files_list)


# sort out the duplicated names:
# for all files in list, if len(file) == 21, then get file[5:7] (5, up to BUT NOT 7)
for f in files_list_dup:
    if len(f)==21:
        #print("test point A is valid")
        # get name of frame and suffix, put into "splitname"
        splitname = f[5:7]+'_'+f[15:17]
        print(splitname)
        # take that entry out of the files_list for later
        files_list.remove(f)
        # check if splitname dir exist, and if not, then make it
        if not os.path.exists(splitname):
            os.makedirs(splitname)
        # rename all files fitting that description to directory: splitname+'\\'+file
        os.rename(f, splitname+ '\\' + f)

# Make empty list "frames_list"
frames_list = []
# To frames_list, copy over first 7 characters from files_list
#print(files_list)
for f in files_list:
    f = f[:7]
    frames_list.append(f)
#print(frames_list)

# Remove all non-unique entries in list
frames_list = list(set(frames_list))
#print(frames_list)

# Remove all but last 2 characters in each entry of frames_list and
# make each into a folder (should leave 01, 02, ... 20, etc. as folders)
for f in frames_list:
    f = f[5:]
    os.mkdir(f)

# For each entry (now unique!) in frames_list, rename all entries that begin
# with that entry from <filename> to <entry>+'\\'+<filename>
for frame in frames_list:
    for f in files_list:
        if f.startswith(frame):
            #print(os.getcwd())
            os.rename(f, frame[5:] + '\\' + f)
