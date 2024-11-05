import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://attendancesystem-42780-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "23MCA20396" : {
        "Name" : "Tushant Dagur",
        "UID" : "23MCA20396",
        "Branch" : "MCA",
        "Total Attendance" : "0",
        "Last_Attendance_Time" : "2024-08-11 03:12:55"
    },
    "23MCA20162" : {
        "Name" : "Kapil",
        "UID" : "23MCA20162",
        "Branch" : "MCA",
        "Total Attendance" : "0",
        "Last_Attendance_Time" : "2024-08-11 03:12:55"
    },
    "21BCS7724" : {
        "Name" : "Praveen Chaudhary",
        "UID" : "21BCS7724",
        "Branch" : "CSE",
        "Total Attendance" : "0",
        "Last_Attendance_Time" : "2024-09-01 09:15:55"
    },
    "24MBA10089" : {
        "Name" : "Amita",
        "UID" : "24MBA10089",
        "Branch" : "MBA",
        "Total Attendance" : "0",
        "Last_Attendance_Time" : "2024-09-04 09:20:25"
    }
}

for key,value in data.items():
    ref.child(key).set(value)