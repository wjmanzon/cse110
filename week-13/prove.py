def main():

    # ask the user for the temperature
    temp = float(input("What is the temperature? "))

    # ask the user if the temperature is Fahrenheit or Celcius
    choicee = input("Fahrenheit or Celsius (F/C)? ").upper()

    # print windchill if the user enters F
    if choicee == "F":
        line = 1
        increment = 5
        length = 12

        for i in range(length):
            print(f'At temperature {temp}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill_fahr(temp,increment):.2f}F.')
            increment += 5
            line += 1

    # print windchill if the user enters C
    elif choicee == "C":
        line = 1
        increment = 5
        length = 12

        for i in range(length):
            print(f'At temperature {temp}C, and wind speed 5 mph, the windchill is: {calculate_wind_chill_cel(temp,increment):.2f}F.')
            increment += 5
            line += 1

    else:
        print("Invalid temp. Please try again!")

def calculate_wind_chill_fahr(temp, wind_default=0):
    """ 
    Calculate windchill
    Parameters: temperature in F, wind_default
    return windchill
    """
    wind_chill = 35.74 + (0.6215 * temp) - 35.75 * (wind_default ** 0.16) + 0.4275 * temp * (wind_default ** 0.16)
    return wind_chill

def calculate_wind_chill_cel(temp, wind_default=0):
    """
    Convert temp to cel and calculate windchill
    Parameters: temperature in C, wind_default
    return windchill
    """
    fahr_to_cel = (temp * 1.8) + 32 #9/5 = 1.8
    wind_chill = 35.74 + (0.6215 * fahr_to_cel) - 35.75 * (wind_default ** 0.16) + 0.4275 * fahr_to_cel * (wind_default ** 0.16)
    return wind_chill

# call the main function
main()