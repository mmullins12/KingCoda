measurement = "3'6"

def convertToInches(measurement):
    feet = measurement.split("'")[0]
    secondHalf = measurement.split("'")[1]
    inches = int(feet) * 12
    inches = inches + int(secondHalf)
    print(inches)

    pass

convertToInches(measurement)