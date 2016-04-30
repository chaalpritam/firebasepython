#!/usr/bin/python3

from firebase import firebase

#firebase = firebase.FirebaseApplication('https://chaalfirebase.firebaseio.com')
firebase = firebase.FirebaseApplication('https://chaalfirebase.firebaseio.com/users/')

#result = firebase.get('/users',None)
#result = firebase.get('/users','first')

result = firebase.get('first',None)

print (result)
