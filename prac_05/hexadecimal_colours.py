COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "aquamarine1": "#7fffd4",
           "azure1": "f0ffff", "beige": "#f5f5dc", "bisque1": "ffe4c4", "black": "#000000", "blue1": "#0000ff",
           "BlueViolet": "#8a2be2"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in COLOURS:
        print("{} is {}".format(colour_name, COLOURS(colour_name)))
    else:
        print("Invalid code")
    colour_name = input("Enter colour name: ")
