import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_frontalface_alt.xml")
face_data = []
dataset_path = './dataset/'
file_name = input("Enter the name of the person : ")
while True:
        ret,frame = cap.read()
        if ret==False:
                continue
        faces = face_cascade.detectMultiScale(frame,1.3,5)
        if len(faces)==0:
                continue
        faces = sorted(faces,key=lambda f:f[2]*f[3])
        for face in faces[-1:]:
                x,y,w,h = face
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                offset = 10
                face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
                face_section = cv2.resize(face_section,(100,100))
                face_data.append(face_section)
                print(len(face_data))
                if(len(face_data)==100):
                        break;
        break;
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully save at "+dataset_path+file_name+'.npy')
cap.release()
cv2.destroyAllWindows()

