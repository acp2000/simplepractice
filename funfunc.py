import sys
#renamed to make more descript, rm print to make more modular
def mi_to_km(miles):
    km = 1.60934 * miles
    return km
#returns false if val is not float
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

miles = ""
while miles is not "exit":
    #made prompt for concise
    miles = input('How many miles would you like to convert to kilometers? ')
    #keep asking for num unless user exits
    while not is_float(miles):
        if miles == "exit":
            sys.exit()
        else:
            print("Please enter a numerical value")
            miles = input(">")
    else:
        #made var more descript
        km = mi_to_km(float(miles))
        print(f"{miles} miles is {km} kilometers")
