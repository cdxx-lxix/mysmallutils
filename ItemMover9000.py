import shutil
import os
# This program takes a source folder, destination folder and a filter.
# Filter can be a name or extention.
# Then it scans and moves all the files that contain filter to the destination folder.

print("Hello there, general!")
print("Short notes. Source folder - place that contains your files which you want to move")
print("Destination folder - place where you want your files to be")
print("Filter - word or extention in the names of files which will act as filter")

sourcepath = input("Now please, input your source folder: ")
destinationpath = input("Now please, input your destination folder: ")
filterword = input("Now please, input your filter: ")

os.chdir(sourcepath)
print("Currently in: " + os.getcwd())
files = os.listdir(sourcepath)
print(files)
for file in files:
    if filterword.lower() in file.lower():
        new_path = shutil.move(f"{sourcepath}/{file}", destinationpath)
        print(new_path)
