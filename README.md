# GoldenFace OPENSOURCE SOFTWARE
An Image Processing Library About Calculating Face Golden Ratio, Facial Cosine Similarity and More

Ümit Aksoylu 2020 © M.I.T  License


## Installing Library:
```bash
pip install GoldenFace
```

#### Required Libraries (Dependencies)
opencv-python

## Basic Functions

Reading face from image file:
```bash
umitFace = GoldenFace.goldenFace("umit.png")
```

## Drawing Functions
These functions allow you to draw landmarks/ border lines on face

color = (255,255,0)

Draw a cover on face
```bash
p1.drawFaceCover(color)
```
Draw border lines on face
```bash
p1.drawLandmark(color)
```
Draw Trichion-Zygoma-Menton line on face
```bash
p1.drawTZM(color)
```
Draw Trichion-Glabella-Subnazale-Menton line on face
```bash
p1.drawTGSM(color)
```
Draw Column Parsed line on face
```bash
p1.drawVFM(color)
```
Draw Trichion-Subnazale-Menton line on face
```bash
p1.drawTSM(color)
```
Draw Lateral cantus-Chelion
```bash
p1.drawLC(color)
```
Draw facial golden ratio mask on face
```bash
p1.drawMask(color)
```
Draw facial important points on face
```bash
p1.drawFacialPoints(color)
```
Draw all landmark points on face
```bash
p1.drawLandmarks(color)
```
