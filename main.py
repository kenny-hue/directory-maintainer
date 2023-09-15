# Directory Maintainer
# Organizes the files within a directory
# Usage: python3 main.py [path/to/directory] [--log-window=N] [--size-threshold=M]
import argparse
import function_mange


def clean_directory(directory, log_window, size_threshold):
  # Implement the directory cleaning functionality here
  # creating folders and moving files
  function_mange.folder_create(directory)
  # checking the log folder if the time a log file was created is older or latest and 
  # deleting old files
  function_mange.log_file_length_checker(log_window)
  # checking the txt folder if the files size is higher than the size_threshold
  # if so it will create a new folder called txt_large_file and store them there 
  function_mange.txt_file_size_checker(size_threshold)
 

# This code reads the command line arguments and passes them into the
# clean_directory function.
# It sets the defaults for the log window and the size threshold
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description='Clean up a messy data directory')
  parser.add_argument('directory', help='the directory to clean')
  parser.add_argument(
      '--log-window',
      dest='log_window',
      default=30,  # retain 30 log files by default
      type=int,
      help='log retention policy: how many most recent log files to keep')
  parser.add_argument(
      '--size-threshold',
      dest='size_threshold',
      default=50,  # 50KB default
      type=int,
      help='file size threshold: how large is a large text file')
  directory = parser.parse_args().directory
  log_window = parser.parse_args().log_window
  size_threshold = parser.parse_args().size_threshold

  clean_directory(directory, log_window, size_threshold)