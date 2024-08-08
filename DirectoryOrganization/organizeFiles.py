import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": {'.pdf', '.rtf', '.txt'},
    "AUDIO": {'.mp3', 'm4a'},
    "VIDEO": {'.mov', '.mp4', '.avi'},
    "IMAGE":{'.jpg', '.jpeg', '.png'}
}

def PickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'       

#For each item in the directory, get the extension and sort it out
def organizeDirectory():
    for item in os.scandir():
        #if item is directory we skip.
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = PickDirectory(fileType)
        directoryPath = Path(directory)
        #if the directory doesn't exist, the script should create the directory
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()