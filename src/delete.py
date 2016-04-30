#!/usr/bin/python3

from firebase import firebase

firebase = firebase.FirebaseApplication('https://chaalfirebase.firebaseio.com')

#result = firebase.delete('/users','fourth')

#result = firebase.delete('/users','-KDolAgp0g3IwXxDdqhw')

result = firebase.delete('/users',None)

print(result)
