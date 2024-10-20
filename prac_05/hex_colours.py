"""
Hex Colour Lookup
Estimate: 30 minutes
Actual: 40 minutes
"""

HEX_COLOURS = {
    "AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4", "Azure": "#f0ffff", "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4", "Black": "#000000", "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

def main():
    colour_name = input("Enter a colour name: ").strip().title()
    while colour_name != "":
        try:
            print(f"{colour_name} = {HEX_COLOURS[colour_name]}")
        except KeyError:
            print(f"Sorry, {colour_name} is not a valid colour name.")
        colour_name = input("Enter a colour name: ").strip().title()

if __name__ == "__main__":
    main()
