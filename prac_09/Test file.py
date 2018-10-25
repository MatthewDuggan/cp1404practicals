import os

filename = "ItIsWell (oh my soul).TXT"
print(filename)
new_file_name = ""
filename = filename.replace(".TXT", ".txt")
for i in range(len(filename)):
    if filename[i - 1] == " ":
        new_file_name += filename[i].upper()
    elif filename[i - 1] == " ":
        new_file_name += filename[i].upper()
    elif filename[i - 1] == "(":
        new_file_name += filename[i].upper()
    elif i > 0 and filename[i - 1].islower and filename[i].isupper():
        new_file_name += "_"
        new_file_name += filename[i]
    else:
        new_file_name += filename[i]
new_file_name = new_file_name.replace(" ", "_")
print(new_file_name)


