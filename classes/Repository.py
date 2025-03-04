
import json
from os import listdir
from modeles.handling_files_and_folders import *
from classes.Commit import Commit
from datetime import datetime
import hashlib



class Repository:
    def __init__(self, repository_path, user_name):
        self.dict_commits = {}
        self.user_name = user_name
        self.count_commit = 0
        self.repository_path = repository_path
        self.wit_path = os.path.join(self.repository_path,".wit")
        self.commits_path = os.path.join(self.wit_path,"commits")
        self.staging_area_path = os.path.join(self.wit_path,"Staging Area")
        self.commits_json_path = os.path.join(self.wit_path,"commits.json")
        self._load_commits()


    def __str__(self):
        commits_str = "\n".join(
            f"{key}: {str(commit)}" for key, commit in self.dict_commits.items()
        )
        return (
            f"Repository:\n"
            f"  Path: {self.repository_path}\n"
            f"  User: {self.user_name}\n"
            f"  Commits:\n{commits_str if commits_str else '  No commits yet.'}"
        )


    def _load_commits(self):
        if os.path.exists(self.commits_json_path):
            try:
                with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)
                if isinstance(existing_data, dict):
                    self.count_commit = len(existing_data)
                    self.dict_commits = existing_data
            except Exception as e:
                print(f"Error loading commits: {e}")


    def wit_init(self):
        try:
          create_folder(".wit",self.repository_path)
          create_folder("Staging Area", self.wit_path)
          create_folder("commits", self.wit_path)
          create_file("commits.json", self.wit_path)
          write_file(self.commits_json_path,"{}")
        except FileExistsError as e:
          print(e)
          return False
        except FileNotFoundError as e:
          print(e)
          return False
        return True



    def wit_add(self, file_name):

        try:
            source_path = os.path.join(self.repository_path, file_name)
            if not os.path.exists(source_path):
                raise FileNotFoundError(f"fatal: pathspec '{file_name}' did not match any files")
            create_file(file_name,self.staging_area_path)
            destination_path = os.path.join(self.staging_area_path,file_name)
            copy_file(source_path,destination_path)
            return True
        except FileNotFoundError as e:
          print(e)
          return False


    def add_commit(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        new_commit = Commit(formatted_time,self.user_name,message)
        self.dict_commits[self.count_commit] = new_commit
        self.count_commit += 1
        try:
            if os.path.exists(self.commits_json_path):
              with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                   existing_data = json.load(json_file)
            else:
              existing_data = {}
            existing_data[self.count_commit] = new_commit.to_dict()
            with open(self.commits_json_path, "w", encoding="utf-8") as json_file:
               json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error updating JSON file: {e}")


    def wit_commit(self, message):#לא בדקנו אם אין שינויים ואז אם אין שינויים אז א עושים COMMIT
        if folder_is_empty(self.staging_area_path):
            print("No changes to commit. Staging area is empty.")
            return False
        message += "(" + str(self.count_commit)+")"
        self.add_commit(message)
        path_new_folder = os.path.join(self.commits_path, message)
        if not os.listdir(self.commits_path):#בדיקה האם הקומיט שנוצר הוא הגרסה הראשונה אם כן ניצור תיקיה חדשה בלי להעתיק את הגרסה הקודמת
            create_folder(message,self.commits_path)
        else:#בכל מקרה אחר ניצור תיקיה חדשה של הגרסה החדשה ונעתיק אליה את הגרסה הקודמת
            last_folder = find_last_created_folder(self.commits_path)
            path_last_folder = os.path.join(self.commits_path, last_folder)
            copy_folder(path_last_folder, path_new_folder)
        copy_files_and_overwrite(self.staging_area_path,path_new_folder)
        emptying_folder(self.staging_area_path)
        return True


    def wit_log(self):
        try:
          with open(self.commits_json_path,"r",encoding="utf-8") as json_file:
              all_commits = json.load(json_file)
              for key, value in all_commits.items():
                  print(json.dumps({key: value}, indent=3, ensure_ascii=False))
                  print("\n")
        except FileNotFoundError as e:
          print(e)


    def wit_status(self):
        list_names_files_in_staging_area = []
        if folder_is_empty(self.staging_area_path):
            print("does not have any commits yet")
        else:
            list_names_files_in_staging_area = read_names_files_in_folder(self.staging_area_path)
        list_files_changing = self.append_changing_file()
        list_files_changing = [file for file in list_files_changing if file not in list_names_files_in_staging_area]
        return list_files_changing,list_names_files_in_staging_area


    """מוסיפה לרשימה את כל הקבצים שנעשו עליהם שינוי וצריך להציג למשתמש"""
    def append_changing_file(self):
        list_change = []#מערך שמכיל את רשימת הקבצים ששונו
        last_commit = find_last_created_folder(self.commits_path)
        path_last_commit = os.path.join(self.commits_path,last_commit)
        for item in os.listdir(self.repository_path):
            if item != ".wit" and is_file_modified_after(os.path.join(self.repository_path,item),path_last_commit):
                list_change.append(item)
        return list_change


    def checkout(self,commit_id):#לא עובד לי למה?????
        try:
            with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                all_commits = json.load(json_file)
                message_commit = ""
                for key, value in all_commits.items():
                    if key == str(commit_id):
                        message_commit = value["message"]
                if message_commit == "":
                     # print("id not valid")
                     return False
        except FileNotFoundError as e:
            print(e)
            return False
        for item in listdir(self.commits_path):
            if item == message_commit:
                copy_files_without_param(os.path.join(self.commits_path,message_commit),self.repository_path,".wit")
                return True
        return False


repo = Repository(r"C:\Users\user1\Desktop\aaa","hadasa rot")
# repo.wit_init()