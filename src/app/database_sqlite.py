import sqlite3
import datetime
import array

users = []

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d)) 