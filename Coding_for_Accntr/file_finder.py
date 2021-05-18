import os
import re
from re import search

tar = "D:/Movies/"
search_type = input("File or Folder: ")
mv_search = input("Enter the file/folder name to search: ")


for dirpath, dirnames, filename in os.walk(tar):
    search_for = {"file": filename, "folder": dirnames}
    # print("dirnames: ", dirnames)
    # print("filename: ", filename)
    # print("dirpath: ", dirpath)

    for files in search_for[search_type]:
        print("Files: ", files)
        if search(f"{mv_search}", files, re.I):
            print("Match found in files:", f"{dirpath}/{files}")
            os.startfile(f"{dirpath}/{files}")
            exit()
    #
    # for file_name in dirnames:
    #     if search(f"{mv_search}", file_name):
    #         print("Match found in dirnames:", f"{dirpath}/{file_name}")
    #         exit()
