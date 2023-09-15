import os
import shutil

def folder_create(directory):

  os.chdir(directory)

  for file in os.listdir():
    name, ext = os.path.splitext(file)

    if ext in [".csv", ".log", ".txt"] :

      if not os.path.exists("csv"):
        os.mkdir("csv")
      if not os.path.exists("log"):
        os.mkdir("log")
      if not os.path.exists("txt"):
        os.mkdir("txt")

      if ext == ".csv":
          shutil.move(file, "csv")
      if ext == ".log":
          shutil.move(file, "log")
      if ext == ".txt":
          shutil.move(file, "txt")
    else:
      return f"Unknown extension: {file}"



def log_file_length_checker(log_window):

  os.chdir("log")
  files = os.listdir()

  log_files = []
  log_files = [file for file in files]

  log_files.sort(key=lambda time: time[:8])
  files_to_retain = log_files[-log_window:]


  excess_files = log_files[:log_window]

  for file in excess_files:
    if file not in files_to_retain:
      os.remove(file)



def txt_file_size_checker(size_threshold):

  os.chdir("..")
  os.chdir("txt")

  for files in os.listdir():

    file_size = os.stat(files).st_size
    file_size_kb = int(file_size / 1024)
    print(file_size)
    print(file_size_kb)
    print(size_threshold)

    if file_size_kb >= size_threshold:
      if not os.path.exists("large_txt_files"):
        os.mkdir("large_txt_files")

      shutil.move(files, "large_txt_files")


    # Double-check the paths you are working on in each function. 
    # Print the sizes of the files you are comparing and 
    # the threshed before applying the comparison. 
    # This should help you figure out the issue.