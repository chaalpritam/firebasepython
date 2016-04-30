#!/usr/bin/python3

from firebase import firebase

firebase = firebase.FirebaseApplication('https://chaalfirebase.firebaseio.com')

#result = firebase.post('/users',{'third':'pritam'})

result = firebase.put('/users','fourth',{'fourth_put':'chaalpritam'})

print(result)
