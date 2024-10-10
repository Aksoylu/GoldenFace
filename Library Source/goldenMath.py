#-- GoldenFace 1.0 (Face Golden Ratio & Cosine Similarity Library)--
# Author      : Umit Aksoylu
# Date        : 15.05.2020
# Description : Facial Cosine Similarity,Face Golden Ratio Calculation And Facial Landmark Detecting/Drawing Library
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      : https://github.com/Aksoylu/GoldenFace
import cv2
import GoldenFace.functions as functions


red = (255, 255, 0)

unitSize = 0
def calculateUnit(facePoints):
    Ax = facePoints["left_eye_left"][0]
    Ay = facePoints["left_eye_left"][1]

    Bx = facePoints["left_eye_right"][0]
    By = facePoints["left_eye_right"][1]

    left_eye_distance = functions.euclideanDistance(facePoints["left_eye_left"],facePoints["left_eye_right"] )

    right_eye_distance = functions.euclideanDistance(facePoints["right_eye_left"],facePoints["right_eye_right"] )
    errorRatio = abs(left_eye_distance - right_eye_distance)

    pieceCount = left_eye_distance/errorRatio

    unitSize = left_eye_distance / pieceCount
    return unitSize

def scaleDistance(distance):
    return distance/unitSize

#public
#Calculate Trichon-Glabella-Subnazale-Menton
def calculateTGSM(faceBorders,facePoints):
    (x,y,w,h) = faceBorders

    #Trichion

    trichionY = y

    #Glabella
    left_Y = abs(facePoints["left_eyebrow_right"][1]  + facePoints["left_eyebrow_right"][1]) /2
    right_y = abs(facePoints["right_eyebrow_left"][1] + facePoints["right_eyebrow_left"][1]) /2
    mid_y = abs(facePoints["left_eyebrow_right"][1] + facePoints["right_eyebrow_left"][1]) /2

    Glabella_Y = (left_Y + right_y + mid_y) /3

    #Subnazale
    Subnazale_Y = facePoints["nose_bottom"][1]

    #Menton
    Menton_y = facePoints["chin_down"][1]

    #Trichion-Glabella distance
    TGdistance = functions.euclideanDistance( (x, trichionY) , (x,  Glabella_Y))
    TGdistance = scaleDistance(TGdistance)

    #Glabella-Subnazale distance
    GSdistance = functions.euclideanDistance( (x, Glabella_Y) , (x,  Subnazale_Y))
    GSdistance = scaleDistance(GSdistance)

    #Subnazale-menton distance
    SMdistance = functions.euclideanDistance( (x, Subnazale_Y) , (x,  Menton_y))
    SMdistance = scaleDistance(SMdistance)

    avg  = (TGdistance + GSdistance + SMdistance) /3

    deflectionPercent =  (abs(TGdistance - avg) +   abs(GSdistance - avg) +   abs(SMdistance - avg)) /(TGdistance + GSdistance + SMdistance) * 100

    #tum mesafeler birbirine esit ve 1/3 oraninda olmalidir. Toplamlari yuzun uzunlugu olmalidir.

    return deflectionPercent

#public
def drawTGSM(img,faceBorders,facePoints,color):
    red = color
    (x,y,w,h) = faceBorders

    #Trichion
    cv2.line(img, (int(x), int(y)), (int(x+w), int(y)), red, 2) 

    #Glabella

    cv2.line(img, (int(facePoints["left_eyebrow_right"][0]), int(facePoints["left_eyebrow_right"][1])), (int(facePoints["right_eyebrow_left"][0]), int(facePoints["right_eyebrow_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["left_eyebrow_right"][0]), int(facePoints["left_eyebrow_right"][1])), (int(x), int(facePoints["left_eyebrow_right"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eyebrow_left"][0]), int(facePoints["right_eyebrow_left"][1])), (int(x+w), int(facePoints["right_eyebrow_left"][1])), red, 2) 

    #Subnazale
    cv2.line(img, (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), (int(x), int(facePoints["nose_bottom"][1])), red, 2)
    cv2.line(img, (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), (int(x+w), int(facePoints["nose_bottom"][1])), red, 2) 

    #Menton
    cv2.line(img, (int(facePoints["chin_down"][0]), int(facePoints["chin_down"][1])), (int(x), int(facePoints["chin_down"][1])), red, 2)
    cv2.line(img, (int(facePoints["chin_down"][0]), int(facePoints["chin_down"][1])), (int(x+w), int(facePoints["chin_down"][1])), red, 2) 
    return img

#public
#Calculate Vertical Face Map Ratio
def calculateVFM(faceBorders,facePoints):
    (x,y,w,h) = faceBorders
    #seperator 1
    s1 = scaleDistance(abs(facePoints["face_left"][0] - facePoints["left_eye_left"][0]))
    #seperator 2
    s2 = scaleDistance(abs(facePoints["left_eye_left"][0] - facePoints["left_eye_right"][0]))
    #seperator 3
    s3 = scaleDistance(abs(facePoints["left_eye_right"][0] - facePoints["right_eye_left"][0]))
    #seperator 4
    s4 = scaleDistance(abs(facePoints["right_eye_left"][0] - facePoints["right_eye_right"][0]))
    #seperator 5
    s4 = scaleDistance(abs(facePoints["right_eye_right"][0] - facePoints["face_right"][0]))

    face_width = scaleDistance(abs(facePoints["face_left"][0] - facePoints["face_right"][0]))
    avg = face_width /5

    deflectionPercent = (abs(s1 -avg ) + abs(s2 -avg ) + abs(s3 -avg ) + abs(s4 -avg ) ) /face_width * 100
    return deflectionPercent

#public
def drawVFM(img,faceBorders,facePoints,color):
    red = color
    (x,y,w,h) = faceBorders


    #seperator 1
    cv2.line(img, (int(facePoints["face_left"][0]), int(y)), (int(facePoints["face_left"][0]), int(y+h)), red, 2) 
    #seperator 2
    cv2.line(img, (int(facePoints["left_eye_left"][0]), int(y)), (int(facePoints["left_eye_left"][0]), int(y+h)), red, 2) 
    #seperator 3
    cv2.line(img, (int(facePoints["left_eye_right"][0]), int(y)), (int(facePoints["left_eye_right"][0]), int(y+h)), red, 2) 
    #seperator 4
    cv2.line(img, (int(facePoints["right_eye_left"][0]), int(y)), (int(facePoints["right_eye_left"][0]), int(y+h)), red, 2) 
    #seperator 5
    cv2.line(img, (int(facePoints["right_eye_right"][0]), int(y)), (int(facePoints["right_eye_right"][0]), int(y+h)), red, 2) 
    #seperator 6
    cv2.line(img, (int(facePoints["face_right"][0]), int(y)), (int(facePoints["face_right"][0]), int(y+h)), red, 2)  

    return img

#public
#Calculate Trichon-Zygoma-Menton Ratio
def calculateTZM(faceBorders,facePoints):
    (x,y,w,h) = faceBorders


    #Zygoma distance
    Zdistance =  scaleDistance(abs(facePoints["face_left"][0] -  facePoints["face_right"][0]))

    #Trichion-Menton distance
    TMdistance = scaleDistance(abs(y -  facePoints["chin_down"][1]))
    deflectionPercent = abs(1.618 - TMdistance/Zdistance) / 1.618 * 100

    return deflectionPercent
#public
def drawTZM(img,faceBorders,facePoints,color):
    red = color
    (x,y,w,h) = faceBorders
    #Trichion
    cv2.line(img, (int(facePoints["nose_bottom"][0]), int(y)), (int(facePoints["nose_bottom"][0]), int(facePoints["chin_down"][1])), red, 2) 

    #Zygoma
    #nose- mouth avg
    x_avg = (facePoints["left_eye_right"][0] +  facePoints["right_eye_left"][0] ) /2
    y_avg = (facePoints["left_eye_right"][1] +  facePoints["right_eye_left"][1] ) /2

    zygoma_y = (y_avg + facePoints["nose_bottom"][1]) /2

    zygoma_y = int(zygoma_y)
    cv2.line(img, (int(facePoints["face_left"][0]), int(zygoma_y)), (int(facePoints["face_right"][0]), int(zygoma_y)), red, 2) 
    #Menton (Eyes)


    return img

#public
#Calculate Trichon-Subnazale-Menton Ratio
def calculateTSM(faceBorders,facePoints):
    (x,y,w,h) = faceBorders
    #Trichion-Subnazale

    TSdistance = scaleDistance( abs(y - facePoints["nose_bottom"][1]) )

    SMdistance = scaleDistance( abs(facePoints["nose_bottom"][1] - facePoints["chin_down"][1]) )

    deflectionPercent = abs( 1.618 - TSdistance / SMdistance) /1.618 * 100
    return deflectionPercent

#public
def drawTSM(img,faceBorders,facePoints,color):
    red = color
    (x,y,w,h) = faceBorders
    #Trichion
    cv2.line(img, (int(facePoints["face_left"][0]), int(y)), (int(facePoints["face_right"][0]), int(y)), red, 2) 
    #Subnazale
    cv2.line(img, (int(x), int(facePoints["nose_bottom"][1])), (int(x+w), int(facePoints["nose_bottom"][1])), red, 2) 
    #Menton
    cv2.line(img, (int(x), int(facePoints["chin_down"][1])), (int(x+w), int(facePoints["chin_down"][1])), red, 2)
    return img

#public
#Calculate Lateral cantus-Chelion Ratio
def calculateLC(faceBorders,facePoints):

    #Lateral Centus
    LC = abs(facePoints["right_eyebrow_right"][0] - facePoints["left_eyebrow_left"][0])
    CE = abs(facePoints["mouth_right"][0] - facePoints["mouth_left"][0])
    deflectionPercent = abs(2.30 - LC/CE) /2.30 * 1000
    return deflectionPercent


#public
def drawLC(img,faceBorders,facePoints,color):
    red = color
    (x,y,w,h) = faceBorders
    #Lateral Centus
    cv2.line(img, (int(facePoints["left_eyebrow_left"][0]), int(facePoints["left_eyebrow_right"][1])), (int(facePoints["right_eyebrow_right"][0]), int(facePoints["right_eyebrow_left"][1])), red, 2) 

    #Mouth y avg

    m_y_avg = (facePoints["mouth_left"][1] +  facePoints["mouth_left"][1] ) /2

    #Chelion
    y_avg = (facePoints["nose_bottom"][1] +  m_y_avg) /2
    y_avg = int(y_avg)

    cv2.line(img, (int(facePoints["mouth_left"][0]), int(y_avg)), (int(facePoints["mouth_right"][0]), int(y_avg)), red, 2) 
    return img

#public
def drawMask(img,faceBorders,facePoints,color):

    red = color
    cv2.line(img, (int(facePoints["face_left"][0]), int(facePoints["face_left"][1])), (int(facePoints["left_eye_left"][0]), int(facePoints["left_eye_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["face_right"][0]), int(facePoints["face_right"][1])), (int(facePoints["right_eye_right"][0]), int(facePoints["right_eye_right"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eye_left"][0]), int(facePoints["left_eye_left"][1])), (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eye_right"][0]), int(facePoints["right_eye_right"][1])), (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), red, 2) 


    cv2.line(img, (int(facePoints["face_left"][0]), int(facePoints["face_left"][1])), (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["face_right"][0]), int(facePoints["face_right"][1])), (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), red, 2) 


    cv2.line(img, (int(facePoints["chin_down"][0]), int(facePoints["chin_down"][1])), (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["chin_down"][0]), int(facePoints["chin_down"][1])), (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), red, 2) 


    cv2.line(img, (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eye_right"][0]), int(facePoints["left_eye_right"][1])), (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eye_left"][0]), int(facePoints["right_eye_left"][1])), (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eye_right"][0]), int(facePoints["left_eye_right"][1])), (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eye_left"][0]), int(facePoints["right_eye_left"][1])), (int(facePoints["nose_bottom"][0]), int(facePoints["nose_bottom"][1])), red, 2) 

    cv2.line(img, (int(facePoints["face_left"][0]), int(facePoints["face_left"][1])), (int(facePoints["left_eyebrow_left"][0]), int(facePoints["left_eyebrow_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["face_right"][0]), int(facePoints["face_right"][1])), (int(facePoints["right_eyebrow_right"][0]), int(facePoints["right_eyebrow_right"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eyebrow_left"][0]), int(facePoints["left_eyebrow_left"][1])), (int(facePoints["left_eye_left"][0]), int(facePoints["left_eye_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eyebrow_right"][0]), int(facePoints["right_eyebrow_right"][1])), (int(facePoints["right_eye_right"][0]), int(facePoints["right_eye_right"][1])), red, 2) 


    cv2.line(img, (int(facePoints["left_eye_right"][0]), int(facePoints["left_eye_right"][1])), (int(facePoints["left_eyebrow_right"][0]), int(facePoints["left_eyebrow_right"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eye_left"][0]), int(facePoints["right_eye_left"][1])), (int(facePoints["right_eyebrow_left"][0]), int(facePoints["right_eyebrow_left"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eyebrow_right"][0]), int(facePoints["left_eyebrow_right"][1])), (int(facePoints["left_eyebrow_left"][0]), int(facePoints["left_eyebrow_left"][1])), red, 2) 
    cv2.line(img, (int(facePoints["right_eyebrow_left"][0]), int(facePoints["right_eyebrow_left"][1])), (int(facePoints["right_eyebrow_right"][0]), int(facePoints["right_eyebrow_right"][1])), red, 2) 

    cv2.line(img, (int(facePoints["face_left"][0]), int(facePoints["face_left"][1])), (int(facePoints["face_left"][0]), int(facePoints["chin_down"][1])), red, 2) 
    cv2.line(img, (int(facePoints["face_right"][0]), int(facePoints["face_right"][1])), (int(facePoints["face_right"][0]), int(facePoints["chin_down"][1])), red, 2) 

    cv2.line(img, (int(facePoints["face_left"][0]), int(facePoints["chin_down"][1])), (int(facePoints["face_right"][0]), int(facePoints["chin_down"][1])), red, 2) 


    cv2.line(img, (int(facePoints["mouth_left"][0]), int(facePoints["mouth_left"][1])), (int(facePoints["face_left"][0]), int(facePoints["chin_down"][1])), red, 2) 
    cv2.line(img, (int(facePoints["mouth_right"][0]), int(facePoints["mouth_right"][1])), (int(facePoints["face_right"][0]), int(facePoints["chin_down"][1])), red, 2) 



    cv2.line(img, (int(facePoints["left_eyebrow_right"][0]), int(facePoints["left_eyebrow_right"][1])), (int(facePoints["right_eyebrow_left"][0]), int(facePoints["right_eyebrow_left"][1])), red, 2) 

    cv2.line(img, (int(facePoints["left_eye_right"][0]), int(facePoints["left_eye_right"][1])), (int(facePoints["right_eye_left"][0]), int(facePoints["right_eye_left"][1])), red, 2) 


    return img

def face2Vec(faceBorders,facePoints):

    (x,y,w,h) = faceBorders
    # 1: Scale Face Matrix
    newScaledPoints = facePoints.copy()
    for i in newScaledPoints:

        Xi = facePoints[i][0]
        Yi = facePoints[i][1]

        Xa = scaleDistance(Xi- x)
        Ya = scaleDistance(Yi -y)

        Xa =  Xa / ((x+w - x) / 1000)
        Ya =  Ya / ((y+h - y) / 1000)

        newScaledPoints[i][0] = int(Xa)
        newScaledPoints[i][1] = int(Ya)

    Vector3 = []


    Vector3.append(functions.calculateVector( (facePoints["face_left"][0], facePoints["face_left"][1] ), (facePoints["left_eye_left"][0],facePoints["left_eye_left"][1] ) ))
    Vector3.append( functions.calculateVector((facePoints["face_right"][0], facePoints["face_right"][1] ), (facePoints["right_eye_right"][0],facePoints["right_eye_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eye_left"][0], facePoints["left_eye_left"][1] ), (facePoints["mouth_left"][0],facePoints["mouth_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eye_right"][0], facePoints["right_eye_right"][1] ), (facePoints["mouth_right"][0],facePoints["mouth_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["face_left"][0], facePoints["face_left"][1] ), (facePoints["mouth_left"][0],facePoints["mouth_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["face_right"][0], facePoints["face_right"][1] ), (facePoints["mouth_right"][0],facePoints["mouth_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["chin_down"][0], facePoints["chin_down"][1] ), (facePoints["mouth_left"][0],facePoints["mouth_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["chin_down"][0], facePoints["chin_down"][1] ), (facePoints["mouth_right"][0],facePoints["mouth_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["nose_bottom"][0], facePoints["nose_bottom"][1] ), (facePoints["mouth_left"][0],facePoints["mouth_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["nose_bottom"][0], facePoints["nose_bottom"][1] ), (facePoints["mouth_right"][0],facePoints["mouth_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eye_right"][0], facePoints["left_eye_right"][1] ), (facePoints["mouth_left"][0],facePoints["mouth_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eye_left"][0], facePoints["right_eye_left"][1] ), (facePoints["mouth_right"][0],facePoints["mouth_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eye_right"][0], facePoints["left_eye_right"][1] ), (facePoints["nose_bottom"][0],facePoints["nose_bottom"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eye_left"][0], facePoints["right_eye_left"][1] ), (facePoints["nose_bottom"][0],facePoints["nose_bottom"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["face_left"][0], facePoints["face_left"][1] ), (facePoints["left_eyebrow_left"][0],facePoints["left_eyebrow_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["face_right"][0], facePoints["face_right"][1] ), (facePoints["right_eyebrow_right"][0],facePoints["right_eyebrow_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eyebrow_left"][0], facePoints["left_eyebrow_left"][1] ), (facePoints["left_eye_left"][0],facePoints["left_eye_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eyebrow_right"][0], facePoints["right_eyebrow_right"][1] ), (facePoints["right_eye_right"][0],facePoints["right_eye_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eye_right"][0], facePoints["left_eye_right"][1] ), (facePoints["left_eyebrow_right"][0],facePoints["left_eyebrow_right"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eye_left"][0], facePoints["right_eye_left"][1] ), (facePoints["right_eyebrow_left"][0],facePoints["right_eyebrow_left"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eyebrow_right"][0], facePoints["left_eyebrow_right"][1] ), (facePoints["left_eyebrow_left"][0],facePoints["left_eyebrow_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["right_eyebrow_left"][0], facePoints["right_eyebrow_left"][1] ), (facePoints["right_eyebrow_right"][0],facePoints["right_eyebrow_right"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["face_left"][0], facePoints["face_left"][1] ), (facePoints["face_left"][0],facePoints["chin_down"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["face_right"][0], facePoints["face_right"][1] ), (facePoints["face_right"][0],facePoints["chin_down"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["face_left"][0], facePoints["chin_down"][1] ), (facePoints["face_right"][0],facePoints["chin_down"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["mouth_left"][0], facePoints["mouth_left"][1] ), (facePoints["face_left"][0],facePoints["chin_down"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["mouth_right"][0], facePoints["mouth_right"][1] ), (facePoints["face_right"][0],facePoints["chin_down"][1] )) )

    Vector3.append( functions.calculateVector((facePoints["left_eyebrow_right"][0], facePoints["left_eyebrow_right"][1] ), (facePoints["right_eyebrow_left"][0],facePoints["right_eyebrow_left"][1] )) )
    Vector3.append( functions.calculateVector((facePoints["left_eye_right"][0], facePoints["left_eye_right"][1] ), (facePoints["right_eye_left"][0],facePoints["right_eye_left"][1] )) )

    return Vector3

#public
def vectorFaceSimilarity(vectorFace1,vectorFace2):

    len1 = len(vectorFace1)
    len2 = len(vectorFace2)

    if(len1 != len2):
        print("Face Vectors is not in same size")
        return -1
    else:
        localSimilarity = functions.cosineSimilarity(vectorFace1, vectorFace2)
        return localSimilarity

    return -1

#public
def goldenFace():
    return functions.loadFaceVec("goldenFace.json")

#public

def drawFacialPoints(img,facePoints,color):

    for point in facePoints:
        coord = (int(facePoints[point][0]), int(facePoints[point][1]))
        cv2.circle(img,coord,1,color,5)
    return img

#public
def drawLandmarks(img,landmarks,color):

    for landmarkArray in landmarks[0]:
        for landmark in landmarkArray:
            coord = (int(landmark[0]), int(landmark[1]))
            cv2.circle(img,coord,1,color,5)
    return img