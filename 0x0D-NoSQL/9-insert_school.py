#!/usr/bin/env python3
""" a Python function that inserts a new document in a collection
based on kwargs """


import pymongo

def insert_school(mongo_collection, **kwargs):
    # Insert the new document
    result = mongo_collection.insert_one(kwargs)
    # Return the new _id
    return result.inserted_id
