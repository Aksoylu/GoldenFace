import __init__.api


#######
p1 = api.goldenFace("umit.png")

color = (255,255,0)
red  =(0, 0, 255)

#p1.drawFaceCover(color)
#p1.drawLandmark(color)

#p1.drawTZM(red)
#p1.drawTGSM(red)
#p1.drawVFM(red)
#p1.drawTSM(red)
#p1.drawLC(red)
#p1.drawMask(red)
#p1.drawFacialPoints(red)
#p1.drawLandmarks(red)

#print(p1.getLandmarks())
#print(p1.getFacialPoints())
#print(p1.getFaceBorder())


#print(p1.calculateTGSM())
#print(p1.calculateVFM())
#print(p1.calculateTZM())
#print(p1.calculateTSM())
#print(p1.calculateLC())

#print(p1.face2Vec())

#print(p1.geometricRatio())
#print(p1.similarityRatio())


#loadedFace = functions.loadFaceVec("face.json")
#print(p1.faceSimilarity(loadedFace))

#p1.saveFaceVec("face.json")


print("Face Golden Ratio: "+ str(p1.geometricRatio()) )
p1.writeImage("man_analyzed.jpeg")

