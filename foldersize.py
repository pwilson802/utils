# Folder size finds the size of the folder given to the script
import sys
import os
myfolder = sys.argv[1]

totalsize = 0
allfolders = {}

for folder, x, files in os.walk(myfolder):
    foldersize = 0
    for file in files:
        try:
            totalsize = totalsize + os.path.getsize(os.path.join(folder, file))
        except FileNotFoundError:
            print('File not Found')
    allfolders[folder] = foldersize

#    try:
#        totalsize = totalsize + os.path.getsize(os.path.join(myfolder, file))
#    except FileNotFoundError:
#        print('File not Found')
print(totalsize / 1000 / 1000)
print(allfolders)
