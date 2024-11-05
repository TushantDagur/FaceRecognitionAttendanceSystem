import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://attendancesystem-42780-default-rtdb.firebaseio.com/",
    'storageBucket' : "attendancesystem-42780.appspot.com"
})




# starting camera screen
capture = cv2.VideoCapture(0)
capture.set(3,590)   #set width
capture.set(4,432)   #height

imgBackground = cv2.imread('Resources/AttendanceSystemBackground.png') #loading bg image

# Importing the modes images into a list
folderModePath = 'Resources/Modes'
modePathList =  os.listdir(folderModePath)
imageModeList = []
for path in modePathList:
    # imageModeList.append(cv2.imread(os.path.join(folderModePath,path)))
    imageModeList.append(cv2.imread(folderModePath+"/"+path))
    # Resources/Modes/1
# print(len(imageModeList))

# loading the encodeFile
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown,studentIds = encodeListKnownWithIds


while True:
    success,image = capture.read()
    # Making images bit smaller to reduce computations and time by reducing it at a sclae of 1/4 02 25%
    imgS = cv2.resize(image,(0,0),None,0.25,0.25)
    # Resize the captured image to fit the background image region
    resized_image = cv2.resize(imgS, (590, 432))
    # converting image int RGB
    imgS  = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    # faces in the current frame
    faceCurrentFrame = face_recognition.face_locations(imgS)
    # Encodings of that faces present in current frame
    encodeCurrentFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)

    imgBackground[152:152+432,62:62+590] = resized_image

    # Adding modes to bg
    # imgBackground[14:14+278,507:507+288] = imageModeList[0]
    # imgBackground[14:14+280,507:507+290] = imageModeList[1]
    # imgBackground[14:14+280,507:507+290] = imageModeList[2]
    imgBackground[14:14+280,507:507+290] = imageModeList[3]


    # matching the encoding of current frame with saved encodings
    for faceLocation,encodeFace in zip(faceCurrentFrame,encodeCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print(studentIds)
        # print(matches)
        # print(distance)
        matchIndex = np.argmin(faceDistance)  #getting index with minimum distance
    #     If matchIndex is in knownfaces then
        if matches[matchIndex]:
            print("Known Face Detacted")
            uid = studentIds[matchIndex]
            print(uid)
            # Scale back the face location to the original size
            y1,x2,y2,x1 = faceLocation
            # Calculate bounding box coordinates
            bbox = 62+x1 ,152+y1,x2-x1,y2-y1
            # print(f'Drawing rectangle at {bbox}')  #for debugging
            imgBackground = cvzone.cornerRect(imgBackground,bbox,rt = 0)
            # imgBackground = cv2.rectangle(imgBackground,62+x1,152+y1,1)

    # cv2.imshow("Webcam",image)
    cv2.imshow("Face Recognition Attendance System",imgBackground)
    cv2.waitKey(1)



