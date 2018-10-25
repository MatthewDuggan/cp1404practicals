"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Cleanup song lyrics file names"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
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
    return new_file_name


main()
# demo_walk()
