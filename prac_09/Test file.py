import os

filename = "Angels from the Realm of Glory"

new_file_name = ""
for i in range(len(filename)):
    if filename[i-1] == " ":
        new_file_name += filename[i].upper()
    else:
        new_file_name += filename[i]
print(new_file_name)

print(filename)
