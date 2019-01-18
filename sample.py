import pymongo
import re
import sys
from pymongo import MongoClient
Client = MongoClient()
db = Client["sample"]
collection =db["person"]
per={}

ch=raw_input('1.Insert 2.Delete 3.View\n')
print(ch)

if ch=='1':
  per["name"]=raw_input('Enter Name:')
  
  if not per["name"].isalpha():
     print('enter valid name')
     sys.exit()
  else:
   per["phone"]=raw_input('Enter phone number:')
   l=len(per["phone"])
   if l<10:
     per["phone"]=""
     print('invalid')
     sys.exit()
   elif type(per["phone"])!=str:
     per["phone"]=""
     print('invalid')
     sys.exit()
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																														
   else:
     per["addr"]=raw_input('Enter addr :')
  collection.insert(per)
  print(per["name"])
  
elif ch=='2':
  dele = raw_input('Enter name to delete\n')
  d=collection.find_one({"name": dele})
  print(d)
  if d!=dele:
    print('record doesnt exist')
    sys.exit()
  else:
    print(d)
    collection.remove(d)
    print('deleted')

elif ch=='3':
  perCol = collection.find()
  for per in perCol:
            print per
  
else:
  print('invalid') 	
