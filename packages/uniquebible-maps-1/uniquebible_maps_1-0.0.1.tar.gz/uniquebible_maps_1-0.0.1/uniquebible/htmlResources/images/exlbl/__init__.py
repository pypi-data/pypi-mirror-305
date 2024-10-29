import os
from pathlib import Path

thisFolder = os.path.dirname(os.path.realpath(__file__))

ubahome = os.path.expanduser(os.path.join("~", "UniqueBible"))

imageFolder = os.path.join(ubahome, "htmlResources", "images")

if not os.path.isdir(imageFolder):
    Path(imageFolder).mkdir(parents=True, exist_ok=True)

#for i in ("exlbl", "exlbl_large", "exlbl_largeHD"):
for i in ("exlbl",):
    destFolder = os.path.join(imageFolder, "i")
    if not os.path.isdir(destFolder):
        copytree(thisFolder, targetFolder, dirs_exist_ok=True)