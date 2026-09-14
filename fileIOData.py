#Python program to read json file 

import json 
#Open json file 
f=open('data.json')

#returns JSON object as a dictionary
data = json.load(f)

#Iterating thriugh json 
#list
for i in data['user_details']:
    print(i)

#Closing file
f.close()

