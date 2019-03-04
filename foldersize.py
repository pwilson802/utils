# Folder size finds the size of the folder given to the script
import sys
import argparse
import os
parser = argparse.ArgumentParser(description='Find the size of folders')
parser.add_argument('foldername', help='The top folder to check the size of')
parser.add_argument('--topfolders', '-t', type=int, help='The top number of folders to show')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
# myfolder = sys.argv[1]

totalsize = 0
allfolders = []

for folder, x, files in os.walk(foldername):
    foldersize = 0
    for file in files:
        try:
            foldersize = foldersize + os.path.getsize(os.path.join(folder, file))
        except FileNotFoundError as err:
            continue
    allfolders.append([folder, foldersize])
    totalsize += foldersize
allfolders.sort(key=lambda k: k[1], reverse=True)

print(totalsize / 1000 / 1000)
for x in allfolders[:5]:
    print('{0}: {1:.2f}'.format(x[0], x[1] / 1000 / 1000))
