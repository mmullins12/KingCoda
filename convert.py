measurements = "3'6"

def convertToInches(measurements):
    feet = measurements.split("'")[0]
    secondHalf = measurements.split("'")[1]
    inches = int(feet) * 12
    inches = inches + int(secondHalf)
    print(inches)

    pass

convertToInches(measurements)