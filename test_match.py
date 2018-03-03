import match_api

name, voterate = match_api.match_face("./res/Angelina/20121219035908831.jpg", "./database/face.db", 0.9)

print("name:", name)
print("vote rate: ", voterate)

