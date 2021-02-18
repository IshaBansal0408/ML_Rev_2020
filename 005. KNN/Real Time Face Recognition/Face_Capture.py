"""
Haar cascade classifier - pretrained model to detect faces
"""
import cv2
cap = cv2.VideoCapture(0)

# Loading Cascade file
classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame = cap.read()
    if ret==False:
        continue
    """
    detectMultiScale(<img>,<scalingFactor>,<No of neighbors>)
    Scale Factor - Shrinking the image to the desired size acc to the trained classifier
    
    returns starting point , height and width 
    """
    faces = classifier.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Current Frame",frame)
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
