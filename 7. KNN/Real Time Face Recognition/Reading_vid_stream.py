import cv2
"""
1. Source to capture the live video 
        Here 0 - default webcam
        If you have multiple webcams - one can specify
"""
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    """
    Here cap.read() returns two things :
        1. Boolean value - true if frame is captured properly otherwise its false
        2. frame - the frame captured
    """
    # having gray frame also
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==False:
        continue
    cv2.imshow("Current Frame",frame)
    cv2.imshow("Gray Frame",gray)
    
    """
    Stopping webcam - let's suppose we want cam to stop when i press 'q'
    
    We will check the key pressed
        1. bitwise AND (&). Why?
                0xFF has 8 ones
                waitKey(1) - 32 bit number
                
        2. ord('q') - returns the ASCII value of the key
                ord('A') will give 65 and for q it is 113
    """
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
"""
Destroying Windows
"""
cap.release()
cv2.destroyAllWindows()
       