from modeles.handling_files_and_folders import *
import os
from classes.Commit import Commit
from datetime import datetime


class Repository:
    def __init__(self, repository_path, user_name):
        self.dict_commits = {}
        self.repository_path = repository_path
        self.user_name = user_name
        self.count_commit = 0

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


    def add_commit(self, user_name, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        new_commit = Commit(formatted_time,user_name,message)
        self.dict_commits[self.count_commit] = new_commit
        self.count_commit += 1



    def wit_init(self):
        try:
          create_folder(".wit",self.repository_path)
          new_path = os.path.join(self.repository_path, ".wit")
          create_folder("Staging Area", new_path)
        except FileExistsError as e:
          print(e)
        except FileNotFoundError as e:
          print(e)


    def wit_add(self, file_name):
        try:
            new_path = os.path.join(self.repository_path,".wit")
            new_path = os.path.join(new_path,"Staging Area")
            create_file(file_name,new_path)
            source_path = os.path.join(self.repository_path,file_name)
            destination_path = os.path.join(new_path,file_name)
            copy_file(source_path,destination_path)
        except FileNotFoundError as e:
          print(e)







repo = Repository(r"C:\לימודים שנה ב\Python\test","hadasa rot")
# repo.wit_init()
# print(repo.repository_path)
# repo.wit_add("f2.html")
# source_path = os.path.join(repo.repository_path,"f1.html")
# copy_file(source_path,r"C:\לימודים שנה ב\Python\test\.wit\Staging Area\f1.html")


