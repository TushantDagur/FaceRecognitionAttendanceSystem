# 🎓 Face Recognition Attendance System

A smart, automated attendance system using facial recognition technology.  
This project leverages OpenCV and the `face_recognition` library to detect and recognize student faces, and integrates with Firebase to manage and store attendance records securely.

---

## 🚀 Features

- ✅ Real-time face detection and recognition using webcam.
- ✅ Automatic attendance marking with time, date, and student details.
- ✅ Secure cloud storage via Firebase (Realtime Database & Storage).
- ✅ Student image capture and encoding support.
- ✅ Modular codebase for scalability and ease of maintenance.

---

## 🛠️ Tech Stack

| Component           | Technology                             |
|--------------------|-----------------------------------------|
| Face Recognition   | [face_recognition](https://github.com/ageitgey/face_recognition) |
| Image Processing   | OpenCV                                  |
| Backend (Cloud)    | Firebase Realtime Database & Storage    |
| Language           | Python 3.x                              |

---

## 📁 Project Structure

📦FaceRecognitionAttendance
┣ 📜 main.py # Main attendance script (webcam loop)
┣ 📜 EncodeGenerator.py # Generates encodings from student images
┣ 📜 Database.py # Firebase integration
┣ 📜 EncodeFile.p # Pickled known face encodings
┣ 📁 Images # Folder containing student face images
┣ 📁 AttendanceImages # Saved attendance snapshots
┣ 📜 firebase_config.py # Firebase configuration (hidden or ignored)
┗ 📜 README.md # Project documentation

## 🧠 How It Works
EncodeGenerator.py scans the Images/ folder and creates facial encodings.
main.py loads these encodings and continuously captures webcam frames.
If a face matches a known encoding:
It fetches the student data from Firebase.
Marks attendance with timestamp and stores a snapshot in Firebase Storage.
