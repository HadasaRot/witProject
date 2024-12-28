import os
from os.path import exists
import shutil
import this
def find_last_created_folder(directory):
    # קבל את כל התיקיות בתיקיה הנתונה
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    # מיין את התיקיות לפי זמן יצירתן (מהחדש לישן)
    last_created_folder = max(folders, key=lambda folder: os.path.getctime(os.path.join(directory, folder)))

    return last_created_folder


# directory_path = r"C:\לימודים שנה ב\Python\test"
# last_folder = find_last_created_folder(directory_path)
# print(f"התיקיה האחרונה שנוצרה היא: {last_folder}")

#
# def copy_folder(source_path, destination_path):
#     shutil.copytree(source_path, destination_path)
#
#
# copy_folder(r"C:\לימודים שנה ב\Python\test2",r"C:\לימודים שנה ב\Python\test3")

import os
import shutil

#
# def move_files_and_overwrite(source_dir, target_dir):
#     # עבור על כל הקבצים והתיקיות בתיקיית המקור
#     for item in os.listdir(source_dir):
#         source_item = os.path.join(source_dir, item)
#         target_item = os.path.join(target_dir, item)
#
#         # אם זה תיקיה, נעשה קריאה חוזרת לפונקציה להעתיק גם את תוכן התיקיה
#         if os.path.isdir(source_item):
#             if not os.path.exists(target_item):
#                 os.makedirs(target_item)  # צור את התיקיה אם היא לא קיימת
#             move_files_and_overwrite(source_item, target_item)
#         else:
#             # אם זה קובץ, תמיד נעתיק אותו מחדש (החלפה אוטומטית של קובץ ישן)
#             shutil.copy2(source_item, target_item)  # העתק את הקובץ עם זמן יצירה ומידע נוסף


#
# move_files_and_overwrite(r"C:\לימודים שנה ב\Python\test2",r"C:\לימודים שנה ב\Python\test3")
# # copy_folder(r"C:\לימודים שנה ב\Python\test2",r"C:\לימודים שנה ב\Python\test3")


def emptying_folder(path):
    for item in os.listdir(path):
        try:
            current_file=os.path.join(path,item)
            os.remove(current_file)
        except:
            print("Folder doesn't exist")


emptying_folder(r"C:\לימודים שנה ב\Python\test\.wit\commits\check2")
