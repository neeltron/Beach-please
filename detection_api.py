# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:20:46 2021

@author: Neel
"""

import os
import io


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Downloads/cognitio-7378d-f0c72d841d75.json"

def detect(img):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(img)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels



detect = detect('a.jpg')
print(detect)
