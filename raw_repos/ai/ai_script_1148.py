#!/usr/bin/env python

import sqlite3

db_name = 'example.db'

# connect to the database

db_connection = sqlite3.connect(db_name)

# create tables

db_connection.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        password TEXT NOT NULL)
''')

db_connection.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        description TEXT NOT NULL)
''')

# commit the changes 

db_connection.commit()