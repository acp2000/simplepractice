def convert(miles):
    km = 1.60934 * miles
    print(f"{miles} miles is {km} kilometers")

print("How many miles would you like to convert to kilometers?")

miles = input(">")

if miles != float(miles):
    print("Please enter a numerical value")
    miles = input(">")

float_miles = float(miles)
convert(float_miles)
