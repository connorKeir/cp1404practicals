"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
STATES_DICT = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
    }
print(STATES_DICT)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATES_DICT:
        print(state_code, "is", STATES_DICT[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for key, value in STATES_DICT.items():
    print("{:3} is {}".format(key, value))