import pymongo
import re
import sys
from pymongo import MongoClient
Client = MongoClient()
db = Client["sample"]
collection =db["person"]
per={}

ch=input('1.Insert 2.Delete 3.Update 4.View\n')
print(ch)

if ch=='1':
  per["name"]=input('Enter Name:')
  
  if not per["name"].isalpha():
     print('enter valid name')
     sys.exit()
  else:
   per["phone"]=input('Enter phone number:')
   l=len(per["phone"])
   if 0<l<10:
     per["phone"]=""
     print('invalid')
     sys.exit()
   elif type(per["phone"])!=str:
     per["phone"]=""
     print('invalid')
     sys.exit()
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																														
   else:
     per["addr"]=input('Enter addr :')
  collection.insert_one(per)
  

elif ch=='2':
  dele = input('Enter name to delete\n')
  collection.delete_one({"name":dele})
  print('deleted')
  for y in collection.find():
       print(y)
       sys.exit()
  
elif ch=='3':
  u = input('enter name to update')
  up = input('update to?')
  collection.update_one({"name":u}, {"$set":{"name":up}})
  print('updated')  
  sys.exit()
    
elif ch=='4':
  perCol = collection.find()
  for per in perCol:
            print(per["name"])
  
else:
  print('invalid') 	