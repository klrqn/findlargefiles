#! python3
# Searches through current directory and finds large files

# Input Data Validation
import pyinputplus as pyip
from pathlib import Path
import os


MEGABYTE = 1048576

# min size of file
minFileSize = pyip.inputNum("You're looking for files larger than (mb): ")
# turn it into bytes?
minFileSizeBytes = minFileSize * MEGABYTE

Dir = ""
while True:
    if os.path.isdir(Dir):
        break
    else:
        print(f'directory: {Dir}')
        print("Enter \".\" for Current Directory")
        Dir = input("what directory would you like to examine?:\n")

# Dictionary containing large files and their sizes
filesOfACertainSize = {}

# Walk the entire folder tree.
def absoluteFilePaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

print(list(absoluteFilePaths(Dir)))

for filename in list(absoluteFilePaths(Dir)):
    # print(str(os.stat(filename).st_size) + " bytes")

    # if file is larger than threshold
    try:
        if os.stat(filename).st_size > minFileSizeBytes:
            filesOfACertainSize[filename] = os.stat(filename).st_size / MEGABYTE
    except:
        FileNotFoundError


print(filesOfACertainSize)

# TODO: Read back found files.

print ("File: ")
for i in filesOfACertainSize :
    print(f"File: {i}".ljust(100) + "   Size: " + str("{:.2f}".format(filesOfACertainSize[i])) + " mb")

# TODO: Optional (ask if you would like to delete file one by one)
print("Would you like to remove any of these files?")
deleteFilesAnswer = input()