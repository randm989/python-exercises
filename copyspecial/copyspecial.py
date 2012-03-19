#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_files(directory):
  filenames = os.listdir(directory)
  validNames = []
  for name in filenames:
    matches = re.search(r'__\w+__',name)
    if matches != None:
      validNames.append(os.path.abspath(os.path.join(directory,name)))
  return validNames

def copy_special_files_to_dir(paths,newDirectory):
  if not os.path.exists(newDirectory):
    os.mkdir(newDirectory)

  for path in paths:
    print(path)
    filename = os.path.basename(path)
    shutil.copy(path,os.path.join(newDirectory,filename))


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print( "usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = get_special_files(args[0])
  if len(todir) > 0:
    copy_special_files_to_dir(paths,todir)
  if len(tozip) > 0:
    zip_special_files_to_dir() 
  if len(tozip) == 0 and len(todir) == 0:
    get_special_files(args[0])
  
if __name__ == "__main__":
  main()
