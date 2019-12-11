import numpy as np
import cv2
import os

def change_extension_pictures(path, inputExt = '.jpeg', targetExt = '.jpg'):
    for file in os.listdir(path):
        if file.endswith(inputExt):
            newName = file.replace(inputExt, targetExt)
            os.rename(path + file, path +  newName)

def rename_files(path):
    c = 1
    for root, folders, files in os.walk(path):
        for f in files:
            if f.endswith(".jpg"):
                npath = os.path.join(root, f)
                os.rename(npath, os.path.join(path, str(c) + ".jpg"))
                c += 1

def delete_grayscale(path):
    for root, folder, files in os.walk(path):
        for f in files:
            if f.endswith(".jpg"):
                image = cv2.imread(os.path.join(root,f), 1)
                r, g, b = image[0, 0]
                if r == g == b:
                    os.remove(os.path.join(root,f))


path = "download/Make Up"
delete_grayscale(path)