#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image
from glob import glob

import os
import shutil
import cv2
import imutils 


def convert_to_webp(source):
    """Convert image to WebP.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination

def create_images_crops(webp_path):
    head, tail = os.path.split(webp_path)
    filename = str(tail).split('.')[0]
    ext = str(tail).split('.')[-1]
    
    image = cv2.imread(str(webp_path))
    print("creating resized images...")
    imageOut1 = imutils.resize(image,width=1250)
    imageOut2 = imutils.resize(image,width=600)
    imageOut3 = imutils.resize(image,width=300)

    img_name_1250 = filename+"_1250."+ext
    img_name_600 = filename+"_600."+ext
    img_name_300 = filename+"_300."+ext
    
    print("save & move imgs...")
    cv2.imwrite(img_name_1250, imageOut1)
    cv2.imwrite(img_name_600, imageOut2)
    cv2.imwrite(img_name_300, imageOut3)

    # Move to original path
    shutil.move(img_name_1250, head)
    shutil.move(img_name_600, head)
    shutil.move(img_name_300, head)


def main():
    print("init main...")
    types = ["png", "jpeg", "jpg"]
    for t in types:
        paths = Path("/Users/jotxee/Downloads/imagesToConvert").glob("**/*."+t)
        for img in paths:
            # Create image to webp
            webp_path = convert_to_webp(img)
            # Create thumbnails
            create_images_crops(webp_path)
    

main()
print ("...End")