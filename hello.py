print('Hello, world!')
print('Wie heißt du?') # ask for their name
myName = input()
print('Freut mich, dich kennenzulernen, ' + myName)
print('Die Länge deines Namens ist:')
print(len(myName))
print('Wie alt bist du?') # ask for their age
myAge = input()
print('In einem Jahr wirst du ' + str(int(myAge) + 1) + ' Jahre alt')