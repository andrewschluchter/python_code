import os

# get the paths of all folder
mainDir = os.getcwd()

# input paths of all folders to have contents deleted
meshconv_folder_in = mainDir+"\\convert_format_STL_OBJ_ASCII_etc\\meshes_input"
meshconv_folder_out = mainDir+"\\convert_format_STL_OBJ_ASCII_etc\\meshes_output"
meshlabserver_folder_in = mainDir+"\\meshlabserver\\meshes_input"
meshlabserver_folder_out = mainDir+"\\meshlabserver\\meshes_output"

# turn those all into a single list of paths
folder_paths = []
folder_paths.append(meshconv_folder_in)
folder_paths.append(meshconv_folder_out)
folder_paths.append(meshlabserver_folder_in)
folder_paths.append(meshlabserver_folder_out)

# for each folder in that list, get the contents    
for folder in folder_paths:
    file_list = os.listdir(folder)
    #print(file_list)
    full_path_list = []
    # for that folder's contents, make new list of full paths of all items
    for item in file_list:
        item = folder+"\\"+item
        #print(item)
        full_path_list.append(item)
    
    # delete every item in the list of paths
    for things in full_path_list:
        #print(things)
        os.remove(things)
