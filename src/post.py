#!/usr/bin/python3

from firebase import firebase

firebase = firebase.FirebaseApplication('https://chaalfirebase.firebaseio.com')

#result = firebase.post('/users',{'third':'pritam'})

result = firebase.post('/users',{'fourth':{'fourth_user ':'chaalpritam'}})

print(result)
