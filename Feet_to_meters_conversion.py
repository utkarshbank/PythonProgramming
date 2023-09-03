def feet_to_meter(feet):
    #Converts feet to meters
    meter = feet * 0.3048
    return meter

def meter_to_feet(meter):
    #Converts meters to feet.
    feet = meter / 0.3048
    return feet

# Feet to Meters
print("Feet to Meters:")
for feet in range(1, 11):
    meter = feet_to_meter(feet)
    print(f"{feet} ft = {meter:.2f} m")

# Meters to Feet
print("\nMeters to Feet:")
for meter in range(20, 69, 6):
    feet = meter_to_feet(meter)
    print(f"{meter} m = {feet:.2f} ft")
