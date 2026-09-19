import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

if os.environ.get('FIREBASE_CREDENTIALS'):
    cred_dict = json.loads(os.environ.get('FIREBASE_CREDENTIALS'))
    cred = credentials.Certificate(cred_dict)
else:
    cred = credentials.Certificate('unsw-college-website-firebase-adminsdk-fbsvc-f8f430162d.json')

firebase_admin.initialize_app(cred)
db = firestore.client()