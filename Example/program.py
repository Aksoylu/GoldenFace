import GoldenFace
import cv2


color_a = (255,255,0)
color_b = (0,0,255)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawFaceCover(color_a)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawTZM(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawTGSM(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawVFM(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawTSM(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawLC(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawLandmarks(color_b)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawLandmark(color_a)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
analysis.drawMask(color_a)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

analysis = GoldenFace.goldenFace("test.png")
goldenRatio = analysis.geometricRatio()

text = "Golden Ratio: %" + str(int(goldenRatio))

image = cv2.putText(analysis.img, text, (0,400), cv2.FONT_HERSHEY_SIMPLEX, 1, color_a, 2)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)


