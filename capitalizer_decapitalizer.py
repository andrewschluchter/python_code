import os
# OPERATOR ACTION: put text to be converted into text file in same dir as this script,
# named "make_upper.txt" or "make_lower.txt" as appropriate

# Get a list called "files_list" of all files and folders
files_list = os.listdir()

# check if files_list contains "make_upper.txt"
if "make_upper.txt" in files_list:
    print ("make_upper.txt is in the current directory")
           
    # open make_upper.txt and take in the text data
    file = open("make_upper.txt")
    input_text = list(file)

    # do the case-change operation:
    output_text = list()
    # convert list into individual strings, then make upper
    for lines in input_text:
        output_text.append(lines.upper())

    # make the output file and write the new text to it
    newFile = open("all_upper.txt", "w")
    for lines in output_text:
        newFile.write(lines) 

    # close the files
    newFile.close()
    file.close()


# check if files_list contains "make_lower.txt"
if "make_lower.txt" in files_list:
    print ("make_lower.txt is in the current directory")
           
    # open make_upper.txt and take in the text data
    file = open("make_lower.txt")
    input_text = list(file)

    # do the case-change operation:
    output_text = list()
    # convert list into individual strings, then make upper
    for lines in input_text:
        output_text.append(lines.lower())

    # make the output file and write the new text to it
    newFile = open("all_lower.txt", "w")
    for lines in output_text:
        newFile.write(lines) 

    # close the files
    newFile.close()
    file.close()
