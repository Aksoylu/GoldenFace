# GoldenFace OPENSOURCE SOFTWARE
An Image Processing Library About Calculating Face Golden Ratio, Facial Cosine Similarity and More

Ümit Aksoylu 2021 © M.I.T  License
Please check example.py for practical usage.

## Installing Library:
```bash
pip install GoldenFace
```

#### Required Libraries (Dependencies)
opencv-python

## Core Functions

Reading a face image as goldenFace object:
```python
umitFace = GoldenFace.goldenFace("umit.png")
```
Printing face vectors:
```python
print(umitFace.face2Vec())
```
Printing Geometric Facial Golden Ratio (Between 0-100):
```python
print(umitFace.geometricRatio())
```
Printing Facial Cosine Similarity With A Golden Face (Between 1.0-0):
```python
print(umitFace.similarityRatio())
```

Saving a goldenFace objects vectors as json file:
```python
umitFace.saveFaceVec("umitFaceVectors.json")
```


Reading a face as vectors from json file:
```python
loadedFace = functions.loadFaceVec("face.json")
```
Calculating face similarity between two face:
```python
print(umitFace.faceSimilarity(loadedFace))
```

## Ratio Calculating Functions







## Drawing Functions
These functions allow you to draw landmarks/ border lines on face

color = (255,255,0)

Draw a cover on face
```python
umitFace.drawFaceCover(color)
```
Draw border lines on face
```python
umitFace.drawLandmark(color)
```
Draw Trichion-Zygoma-Menton line on face
```python
umitFace.drawTZM(color)
```
Draw Trichion-Glabella-Subnazale-Menton line on face
```python
umitFace.drawTGSM(color)
```
Draw Column Parsed line on face
```python
umitFace.drawVFM(color)
```
Draw Trichion-Subnazale-Menton line on face
```python
umitFace.drawTSM(color)
```
Draw Lateral cantus-Chelion
```python
umitFace.drawLC(color)
```
Draw facial golden ratio mask on face
```python
umitFace.drawMask(color)
```
Draw facial important points on face
```python
umitFace.drawFacialPoints(color)
```
Draw all landmark points on face
```python
umitFace.drawLandmarks(color)
```
## Write processed goldenFace object as image:
```python
umitFace.writeImage("umit_analyzed.jpeg")
```
