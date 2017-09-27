import glob, os, os.path, copy, time
#remove time after debugging completed
from collections import Counter
# for all stl files in the main folder (the folder containing this script),
# open stl and do the rest of this script


#debugging only
#start_time = time.time()

# get name of all files and put in list
mainDir = os.getcwd()
allFilesDirs = os.listdir(mainDir)
# make new directory "isolated"
os.mkdir("isolated")
allStlFiles = []
#print(allFilesDirs)
# remove all non-stl files from list
for x in allFilesDirs:
    if ".stl" in x:
        allStlFiles.append(x)
print(allStlFiles)

# for all entries in array (one at a time! I,e, only do 1 stl at a time!),
# open 'mainDir'/<stl filename>
for x in allStlFiles:
    file = open(mainDir+'//'+x)
    curFilename = x
    #print(mainDir+'//'+x)
    print(curFilename)



    # make an array and put in the line numbers and normals (as a string) of all facets into it
    # Array_0, "lineAndStr", [line#, string]
    facetsArray = []
    lineAndStr = []
    lines = list(file)
    for index, line in enumerate(lines):
        lineAndStr = []
        if "facet normal" in line:
            #print(index, line)
            lineAndStr.append(index)
            lineAndStr.append(line)
            facetsArray.append(lineAndStr)



    # make a variable, and put in the "most common string" for the normal string

    stringList = []
    for aList in facetsArray:
        for aString in aList:
            stringList.append(aString)
            #print(aString)

    counting = Counter(stringList)
    mostCom_list = counting.most_common(1)[0]
    #print(mostCom_list)
    mostCom = mostCom_list[0]
    #print(mostCom)




    # turn the most common string into an x/y/z array vector
    mostCom = mostCom[14:]
    mostCom = mostCom[:-2]
    #print(mostCom)
    vectorCom = mostCom.split()
    vectorCom[0] = float(vectorCom[0])
    vectorCom[1] = float(vectorCom[1])
    vectorCom[2] = float(vectorCom[2])
    #print(vectorCom)



    # turn the most common normal array into an upper and lower bound array
    # OPERATOR ENTERED VALUE: determines how exact the procedure will work
    # try starting with flex = 0.001
    flex = 0.01
    #vectorLower = Array_3[xvar-flex, yvar-flex, zvar-flex]
    vectorLower = vectorCom[:]
    vectorLower[0] = vectorLower[0]-flex
    vectorLower[1] = vectorLower[1]-flex
    vectorLower[2] = vectorLower[2]-flex
    #print(vectorLower)
    #vectorUpper = Array_3[xvar+flex, yvar+flex, zvar+flex]
    vectorUpper = vectorCom[:]
    vectorUpper[0] = vectorUpper[0]+flex
    vectorUpper[1] = vectorUpper[1]+flex
    vectorUpper[2] = vectorUpper[2]+flex
    #print(vectorUpper)





    # convert the facetsArray entries from strings to x/y/z's
    # vectorArray = [line #, xvar, yvar, zvar]
    vectorArray = []
    for entry in facetsArray:
        lineNum = entry[0]
        #print(lineNum)
        baseVector = entry[1][14:]
        #print(baseVector)
        baseVector = baseVector[:-1]
        #print(baseVector)
        baseVectorList = baseVector.split()
        #for item in baseVectorList:
        #    print(item)
        #print()
        baseVectorList[0] = float(baseVectorList[0])
        baseVectorList[1] = float(baseVectorList[1])
        baseVectorList[2] = float(baseVectorList[2])
        #print(baseVectorList)
        #append 0 to front of bVL
        baseVectorList.insert(0,lineNum)
        #print(baseVectorList)
        vectorArray.append(baseVectorList)
    #print(vectorArray[0])



    #debugging, part 1
    #print(len(vectorArray))

    ########################################################################################################

    #METHOD 1
    # remove all entries in vectorArray that have an x, y, or z value above any of the values in Array_Upper
    for entry in vectorArray:
    # note that "entry" has 4 elements (lineNum, x,y,z), while vectorUpper/Lower only have 3, hence numbers below    
        if entry[1] > vectorUpper[0] or entry[2] > vectorUpper[1] or entry[3] > vectorUpper[2]:
            vectorArray.remove(entry)

    #print(len(vectorArray))
    # remove all entries in Array_4 that have an x, y, or z value below any of the values in Array_Lower
    for entry in vectorArray:
        if entry[1] < vectorLower[0] or entry[2] < vectorLower[1] or entry[3] < vectorLower[2]:
            vectorArray.remove(entry)

    ########################################################################################################

    """
    #METHOD 2: remove upper and lower at once: faster, but less transparent
    # Problem! not removing all our of range normals?
    for entry in vectorArray:
    # note that "entry" has 4 elements (lineNum, x,y,z), while vectorUpper/Lower only have 3, hence numbers below    
        if entry[1] > vectorUpper[0] or entry[2] > vectorUpper[1] or entry[3] > vectorUpper[2] or entry[1] < vectorLower[0] or entry[2] < vectorLower[1] or entry[3] < vectorLower[2]:
            vectorArray.remove(entry)
    """
    """
    # METHOD 3
    # Problem! not removing all out of range normals?
    for entry in vectorArray:
        print(entry)
        print(vectorUpper)
        print(vectorLower)
        if entry[1] > vectorUpper[0] or entry[1] < vectorLower[0]:
            vectorArray.remove(entry)
            print("removed x")
        elif entry[2] > vectorUpper[1] or entry[2] < vectorLower[1]:
            vectorArray.remove(entry)
            print("removed y")
        elif entry[3] > vectorUpper[2] or entry[3] < vectorLower[2]:
            vectorArray.remove(entry)
            print("removed z")
    """

    #debugging, part 2
    #print(len(vectorArray))
    #elapsed_time = time.time() - start_time
    #print(elapsed_time)







    # make a new stl and copy over the facets that correspond to the entries in Array_4

    #take the name of the current .stl file, add "_isolated" to the original name
    originalFilename = curFilename
    curFilename = curFilename[:-4]
    curFilename = curFilename + "_isolated.stl"
    #print(curFilename)

    #make a new file titled with the new name and open it
    newFile = open(mainDir+'//'+"isolated"+'//'+curFilename,"w") 
    newFile.write("solid ascii\n") 

    #for every entry in Array_4,
    #    copy over that facet, add in the line "endsolid", close the new file, close the original .stl file, and move onto the next one
    for stuff in vectorArray:
        theLineNum = stuff[0]
        
        #print(theLineNum[0])
        for countVar in range(0, 7):
            #print(theLineNum)
            newFile.write(lines[theLineNum])
            theLineNum = theLineNum + 1
            #print(theLineNum)
            countVar = countVar + 1
            #print(countVar)

    newFile.write("endsolid\n") 
    newFile.close() 
    file.close() 

#print("end of script")
