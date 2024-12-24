import os
from os.path import exists
import shutil

def create_folder(folder_name,path):
    new_path = os.path.join(path, folder_name)
    if not exists(path):
        raise FileNotFoundError("path not found")
    if os.path.isdir(new_path):
        raise FileExistsError("folder already exists")
    os.mkdir(new_path)


#דורס את התיקיה במידה וקים באותו שם
def create_file(file_name,path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path,file_name)
    file = open(new_path,"w")
    file.close()

#מוסיפה קטסט לקובץ ולא דורסת את מה שהיה
def write_file(path,text):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with open(path,"a") as file:
        file.write(text)


def read_file(path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with open(path,"r") as file:
        return file.read()


def copy_file(source_path,destination_path):
    shutil.copyfile(source_path,destination_path)





# create_folder("3",r"C:\לימודים שנה ב\Python\test")
# create_file("f2.html",r"C:\לימודים שנה ב\Python\test\.wit\Staging Area")
write_file(r"C:\לימודים שנה ב\Python\test\f1.html","<h1>hadasa</h1>")
# print(read_file(r"C:\לימודים שנה ב\Python\test\1\f1.html"))
# copy_file(r"C:\לימודים שנה ב\Python\test\1\f6.html",r"C:\לימודים שנה ב\Python\test\1\f2.html")