import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('unsw-college-website-firebase-adminsdk-fbsvc-ed25ac4b5f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()