#-- GoldenFace 1.0 (Face Golden Ratio & Cosine Similarity Library)--
# Author      : Umit Aksoylu
# Date        : 15.05.2020
# Description : Facial Cosine Similarity,Face Golden Ratio Calculation And Facial Landmark Detecting/Drawing Library
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      : https://github.com/Aksoylu/GoldenFace

import cv2
import GoldenFace.goldenMath
import GoldenFace.functions
import GoldenFace.landmark
import time
class goldenFace:

    img = ""
    image_gray = ""
    landmark_detector = ""
    face_detector = ""
    faces = ""
    facePoints = ""
    faceBorders = ""

    landmarks= ""


    def __init__(self, path):
        self.img = cv2.imread(path)
        self.image_gray =cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.landmark_detector = cv2.face.createFacemarkLBF()
        self.landmark_detector.loadModel("dataset/landmark.yaml")

        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        self.faces = self.face_detector.detectMultiScale(self.image_gray, 1.3, 5)

        for faceBorders in self.faces:
            (x,y,w,h) = faceBorders
            self.faceBorders = faceBorders
            _, self.landmarks = self.landmark_detector.fit(self.image_gray, self.faces)
            self.facePoints = landmark.detectLandmark(self.landmarks)


            break

    def drawFaceCover(self,color):
        (x,y,w,h) = self.faceBorders
        self.img =  cv2.rectangle(self.img,(x,y),(x+w, y+h),color,2)

    def drawLandmark(self,color):
        self.img = landmark.drawLandmark(self.img, self.landmarks,color)

    def drawMask(self,color):
        self.img  = goldenMath.drawMask(self.img,self.faceBorders,self.facePoints,color)

    def drawTGSM(self,color):
        self.img = goldenMath.drawTGSM(self.img,self.faceBorders,self.facePoints,color)

    def drawVFM(self,color):
        self.img = goldenMath.drawVFM(self.img,self.faceBorders,self.facePoints,color)

    def drawTZM(self,color):
        self.img = goldenMath.drawTZM(self.img,self.faceBorders,self.facePoints,color)

    def drawLC(self,color):
        self.img = goldenMath.drawLC(self.img,self.faceBorders,self.facePoints,color)

    def drawTSM(self,color):
        self.img = goldenMath.drawTSM(self.img,self.faceBorders,self.facePoints,color)

    def calculateTGSM(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        return goldenMath.calculateTGSM(self.faceBorders,self.facePoints)

    def calculateVFM(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        return goldenMath.calculateVFM(self.faceBorders,self.facePoints)

    def calculateTZM(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        return goldenMath.calculateTZM(self.faceBorders,self.facePoints)

    def calculateTSM(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        return goldenMath.calculateTSM(self.faceBorders,self.facePoints)

    def calculateLC(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        return goldenMath.calculateLC(self.faceBorders,self.facePoints)

    def geometricRatio(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        TZM = goldenMath.calculateTZM(self.faceBorders,self.facePoints)
        TGSM = goldenMath.calculateTGSM(self.faceBorders,self.facePoints)
        VFM = goldenMath.calculateVFM(self.faceBorders,self.facePoints)
        TSM = goldenMath.calculateTSM(self.faceBorders,self.facePoints)
        LC = goldenMath.calculateLC(self.faceBorders,self.facePoints)

        avg = (TZM + TGSM + VFM + TZM + TSM +LC)  /6
        return 100- avg

    def face2Vec(self):
        goldenMath.unitSize =goldenMath.calculateUnit(self.facePoints)
        vector = goldenMath.face2Vec(self.faceBorders,self.facePoints)
        return vector

    def faceSimilarity(self,vector2):
        return goldenMath.vectorFaceSimilarity(self.face2Vec(),vector2)

    #Golden similarity
    def similarityRatio(self):
        facevec = self.face2Vec()
        goldenFace = functions.loadFaceVec("goldenFace.json")
        similarity = goldenMath.vectorFaceSimilarity(facevec,goldenFace)

        return similarity

    def getLandmarks(self):
        return self.landmarks

    def getFacialPoints(self):
        
        return self.facePoints

    def drawFacialPoints(self,color):
        self.img = goldenMath.drawFacialPoints(self.img,self.facePoints,color)

    def drawLandmarks(self,color):
        self.img = goldenMath.drawLandmarks(self.img,self.landmarks,color)


    def getFaceBorder(self):
        return self.faceBorders

    def writeImage(self,name):
        cv2.imwrite(name, self.img)

    def saveFaceVec(self,path):
        functions.saveFaceVec(self.face2Vec(),path)



