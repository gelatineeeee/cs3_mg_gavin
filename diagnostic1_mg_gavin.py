

def calculate_space_weight(earth_weight, destination):
    destination = destination.lower()
    if destination == "mars":
        return earth_weight * 0.38
    elif destination == 'jupiter':
        return earth_weight * 2.34
    elif destination == "moon":
        return earth_weight * 0.16
    else:
        print("Error. Invalid destination.")
        return 0
#EXAMPLE FUNC CALL
print(calculate_space_weight(70, "mars"))