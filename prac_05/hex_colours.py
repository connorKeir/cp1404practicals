HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "aquamarine1": "#7fffd4",
    "black": "#000000",
    "blue2": "#0000ee",
    "chartreuse1": "7fff00",
    "coral": "#ff7f50",
    "cornsilk3": "#cdc8b1",
    "cyan1": "#00ffff",
    "darkgoldenrod": "#b8860b",
    "darkviolet": "#9400d3"
}


def main():
    """search for hex-code by colour name."""
    colour_name = input("Enter a colour name: ").lower()
    while colour_name != '':
        if colour_name in HEX_COLOURS:
            print("{}'s hex-code is {}".format(colour_name, HEX_COLOURS[colour_name]))
        else:
            print("There is no hex-code for {}".format(colour_name))
        colour_name = input("Enter a colour name: ").lower()


main()
