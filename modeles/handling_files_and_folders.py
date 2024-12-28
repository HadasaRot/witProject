import os
from operator import truediv
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

def copy_folder(source_path,destination_path):
    shutil.copytree(source_path,destination_path)

def find_last_created_folder(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    last_created_folder = max(folders, key=lambda folder: os.path.getctime(os.path.join(directory, folder)))
    return last_created_folder


def copy_files_and_overwrite(source_dir, destination_dir):
    # מעבר על כל תיקיות והקבצים בתיקית המקור
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(destination_dir, item)
        # אם זה תיקיה, נעשה קריאה חוזרת לפונקציה להעתיק גם את תוכן התיקיה
        if os.path.isdir(source_item):
            if not os.path.exists(target_item):
                os.makedirs(target_item)  # צור את התיקיה אם היא לא קיימת
            copy_files_and_overwrite(source_item, target_item)
        else:
            # אם זה קובץ, תמיד נעתיק אותו מחדש (החלפה אוטומטית של קובץ ישן)
            shutil.copy2(source_item, target_item)  # העתק את הקובץ עם זמן יצירה ומידע נוסף


def emptying_folder (path):
    for item in os.listdir(path):
        try:
            current_file=os.path.join(path,item)
            os.remove(current_file)
        except:
            print("Folder doesn't exist")

def folder_is_empty(path):
    if not os.listdir(path):
        return True
    return  False

def read_names_files_in_folder(path):
    data = []
    try:
       for item in os.listdir(path):
         data.append(item)
       return data
    except FileNotFoundError as e:
            print(e)


#מקבלת שתי ניתובים ובודקת האם שתי התיקיות השונות נוצרו בזמן שונה ומחזירה נכון במקרה שהניתוב הראשון נעשה לאחר הניתוב השני
def is_file_modified_after(path1,path2):
    date_path1 = os.path.getmtime(path1)
    date_path2 = os.path.getctime(path2)
    if date_path1 > date_path2:
        return True
    return  False


def copy_files_without_param(source_dir, destination_dir,param):
    # מעבר על כל תיקיות והקבצים בתיקית המקור
    for item in os.listdir(destination_dir):
        if item != param:
           target_item = os.path.join(destination_dir, item)
           os.remove(target_item)
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        print(source_item)
        new_path = os.path.join(destination_dir,item)
        copy_file(source_item,new_path)




# copy_files_without_param(r"C:\לימודים שנה ב\Python\test\source",r"C:\לימודים שנה ב\Python\test\dist-",".wit")

# create_file("f2.html",r"C:\לימודים שנה ב\Python\test\.wit\Staging Area")
# write_file(r"C:\לימודים שנה ב\Python\test\f1.html","<h1>hadasa</h1>")
# print(read_file(r"C:\לימודים שנה ב\Python\test\1\f1.html"))
# copy_file(r"C:\לימודים שנה ב\Python\test\1\f6.html",r"C:\לימודים שנה ב\Python\test")
# emptying_folder(r"C:\לימודים שנה ב\Python\test\.wit\commits\commit2")
# print(folder_is_empty(r"C:\לימודים שנה ב\Python\test\2"))
# read_names_files_in_folder(r"C:\לימודים שנה ב\Python\test\.wit")
# print(is_file_modified_after(r"C:\לימודים שנה ב\Python\test\1",r"C:\לימודים שנה ב\Python\test"))