import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://attendancesystem-42780-default-rtdb.firebaseio.com/",
    'storageBucket' : "attendancesystem-42780.appspot.com"
})

# importing student images and uploading to the bucket
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imageList = []
studentIds = []
for path in pathList:
    imageList.append(cv2.imread(folderPath+"/"+path))
    # studentIds.append(path[:-5])
    studentIds.append(os.path.splitext(path)[0])
    # uploading to the cloud storage
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


print(len(imageList))
# print(imageList)
print(studentIds)


def findEncodings(imgLists):
     encodeList = []
     for img in imgLists:
         img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
         encode = face_recognition.face_encodings(img)[0]
         encodeList.append(encode)

     return encodeList

print("...Encoding Start....")
encodeListKnown = findEncodings(imageList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
# print(encodeListKnown)
print("Encoding Ended")


# Dumping/Sending these encoding list to a file
file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved Successfully.")

