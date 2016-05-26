import PIL
import os.path
import matplotlib.pyplot as plt
import numpy as np

def findDirectory(image):
    directory = os.path.dirname(os.path.abspath(__file__))
    fName = os.path.join(directory, image)
    img = plt.imread    (fName)
    return img

def la_noire(image):
    '''Puts an LA Noire filter over the image.
    Image must be inputed as a string
    EX: "image.png"'''
    img = findDirectory(image)
    #The actual filter starts here
    height = len(img)
    width = len(img[0])
    #makes grayscale
    for row in range(height):
        for column in range(width):
            avg = (sum(img[row][column]))/3
            img[row][column] = [x = avg for x in img[row][column]]
    #makes bright thing brighter
    for row in range(height):
        for column in range(width):
            if (sum(img[row][column]))/3 > 200:
                img[row][column] = [x*2.5 for x in img[row][column]]
    img.save(image + '_laNoire.jpg')

def mys_stranger(image):
    '''Puts a Mysterious Stranger filter over the image.
    Image must be inputed as a string
    Ex: "image.png"'''
    img = findDirectory(image)
    #the actual filter starts here
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for column in range(width):
            if (sum(img[row][column]))/3 >= 230:
                img[row][column] = [x*2.5 for x in img[row][column]]
            elif (sum(img[row][column]))/3 <= 50:
                img[row][column] = [x/10 for x in img[row][column]]
    img.save(image + '_mysStanger.jpg')
