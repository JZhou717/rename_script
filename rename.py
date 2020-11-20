import os, glob, string, random
from shutil import copyfile

# save pool of lowercase ascii characters for name generation
letters = string.ascii_lowercase
# create a directory to save copy of original files
if not os.path.exists("save"):
    os.mkdir("save")

# for all files of any extension in current directory
for file in glob.glob("*.*"):
    # ignore this script
    if file == "rename.py": continue

    # save file extension
    ext = file.split(".")[1]
    # generate random 16 lowercase char string
    name = (''.join(random.choice(letters) for i in range(16)))

    # print current file name, save a copy, then rename file
    print(file)
    copyfile(file, "save/" + file)
    os.rename(file, name+"."+ext)