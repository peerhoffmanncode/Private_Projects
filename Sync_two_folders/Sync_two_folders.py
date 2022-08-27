import glob
import os
import sys
from pathlib import Path

exclude = [".git"]

def get_all_data_from_dir(path:str, exclude) -> list:
    
    main_result_list = []
    dir_items = os.walk(path)

    for j in dir_items:
        current_path = j[0]
        if current_path.endswith("/") != True:
            current_path = current_path + "/"
        if exclude not in current_path:
            with os.scandir(current_path) as dir_entries:
                sub_result_list = []
                for entry in dir_entries:
                    # if entry.name
                    info = entry.stat()
                    sub_result_list.append(current_path)
                    sub_result_list.append(entry.name)
                    sub_result_list.append(entry.is_file())
                    sub_result_list.append(info.st_size)
                    sub_result_list.append(info.st_ctime)
                    sub_result_list.append(info.st_mtime)
                    sub_result_list.append(info.st_atime)
            main_result_list.append(sub_result_list)
    return main_result_list

def show_filelist(list_to_show):
    print (len(list_to_show))
    if len(list_to_show) > 0:
        for id, i in enumerate(list_to_show):
            if i != []:
                print(id, i[0]+i[1])
    else:
        print("No files to show")

my_path_1 = "/home/user/Documents/Python CODEING/"
my_path_2 = "/home/user/Documents/GoogleDriveFolder/Python CODEING"

res_lst1 = get_all_data_from_dir(my_path_1, ".git")
res_lst2 = get_all_data_from_dir(my_path_2, ".git")

os.system("clear")
show_filelist(res_lst1)
show_filelist(res_lst2)

