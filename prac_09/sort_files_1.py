import os

os.chdir("FilesToSort") # change to correct dir
extensions = []
for filename in os.listdir("."):
    if os.path.isdir(filename):
        continue
    extension = filename.split(".")[-1]
    if extension not in extensions:
        extensions.append(extension)
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
    os.rename(filename, "{}/{}".format(extension, filename))
print(extensions)


