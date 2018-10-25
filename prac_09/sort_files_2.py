import os


def main():
    os.chdir("FilesToSort")  # change to correct dir
    extensions_to_categories = {}

    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = filename.split(".")[-1]
        if extension not in extensions_to_categories:
            category = input("What category would you like to sort {} files into?".format(extension))
            extensions_to_categories[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(extensions_to_categories[extension], filename))



main()
