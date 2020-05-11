import socket, pusher, psutil, os
from pymongo import MongoClient

def checkprocessor():
    if psutil.cpu_percent(1, False) <= 80:
        return True
    else:
        return False

def checkram():
    if psutil.virtual_memory().percent <= 80:
        return True
    else:
        return False

def checknetwork():
    try:
        host = socket.gethostbyname("www.google.fr")
        connection = socket.create_connection((host, 80), 5)
        connection.close()
        return True
    except:
        return False

def checkpusher():
    try:
        client = pusher.Pusher(
            app_id='862851',
            key='PUSHER_KEY',
            secret='PUSHER_SECRET',
            cluster='eu',
            ssl=True
        )
        if client.channels_info():
            return True
    except:
        return False

def checkmongo():
    try:
        client = MongoClient("mongodb+srv://skew:"+os.environ['space_mongo_pass']+"@spaceh2o-7zb9g.mongodb.net/test?retryWrites=true&w=majority")
        if client.list_database_names():
            return True
        else:
            return False
    except:
        return False