#-- GoldenFace 1.0 (Face Golden Ratio & Cosine Similarity Library)--
# Author      : Umit Aksoylu
# Date        : 15.05.2020
# Description : Facial Cosine Similarity,Face Golden Ratio Calculation And Facial Landmark Detecting/Drawing Library
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      : https://github.com/Aksoylu/GoldenFace
import json

def kokal(x):
    if x>0:
        return x**(1/2)
    else:
        return -1 * x**(1/2)

def usal(x,level):
    return x**level

def euclideanDistance(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ =len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] -  (A[i] ), 2 )
        distance = kokal(total)
        return distance

def noktasalCarpim(vector1,vector2):
    if len(vector1) != len(vector2):
        return -1

    toplam = 0
    for i in range(len(vector1)):
        toplam = toplam + vector1[i][1] * vector2[i][1]
    return toplam

def vectorBoyut(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam = toplam + (vector[i][1] * vector[i][1])

    return toplam ** (1/2)

def cosineSimilarity(vector1,vector2):
    return noktasalCarpim(vector1,vector2)  / ( vectorBoyut(vector1) * vectorBoyut(vector2) )

def calculateVector(A,B):

    element= [ abs(A[0] - B[0]),  abs(A[1] - B[1])  ]
    return element


#public
def loadFaceVec(path):

    data = []
    with open(path) as json_file:
        data = json.load(json_file)
    return data


#public
def saveFaceVec(facePoints,path):
    with open(path, 'w') as outfile:
        json.dump(facePoints, outfile)


