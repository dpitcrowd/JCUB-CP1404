"""
Hexadecimal colour
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff",
                "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0",
                "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4",
                "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74",
                "azure1": "#f0ffff",
                "azure2": "#e0eeee",
                "azure3": "#c1cdcd",
                "azure4": "#838b8b",
                "beige": "#f5f5dc",
                "bisque1": "#ffe4c4"
}

COLOUR_NAMES_MENU = """
    COLOUR_NAMES_MENU 
    
    AliceBlue 
    AntiqueWhite AntiqueWhite1 AntiqueWhite2 AntiqueWhite3 AntiqueWhite1
    aquamarine1 aquamarine2 aquamarine3 
    azure1  azure2 azure3 azure4
    beige
    bisque
"""


def main():
    print(COLOUR_NAMES_MENU)
    colour_name = input("\t\tEnter a colour name: ")

    while colour_name != "":
        print("\t\tThe code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
        colour_name = input("\t\tEnter a colour name: ")


if __name__ == '__main__':
    main()