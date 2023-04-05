def main():
    # ask the user for the year
    year_of_interest = int(input("Enter the year of interest "))
    
    # call the other functions
    compute_overall_min_max()
    compute_average(year_of_interest)
    compute_specific_year_min_max(year_of_interest)

def compute_overall_min_max():
    # set the variables
    lowest = 99999
    low_country = ""
    low_year = ""

    highest = 0
    high_country = ""
    high_year = ""

    # Open the CSV file
    with open("life-expectancy.csv") as life_expectancy_file:
    
        # Skip the header
        next(life_expectancy_file)
    
        # For every row in the file, split the row into parts using comma delimeter
        for row in life_expectancy_file:
            parts = row.split(",")
    
            # Set the variables
            country = parts[0].strip()
            code = parts[1].strip()
            year = int(parts[2].strip())
            life = float(parts[3].strip())

            if life <= lowest:
                lowest = life
                low_country = country
                low_year = year
    
            if life >= highest:
                highest = life
                high_country = country
                high_year = year

    print(f"The overall max life expectancy is: {highest} from {high_country} in {high_year} " )
    print(f"The overall min life expectancy is: {lowest} from {low_country} in {low_year} " )

def compute_average(year_of_interest):
    specific_year_list = []
    average = 0 
    
    with open("life-expectancy.csv") as life_expectancy_file:
        # Skip the header
        next(life_expectancy_file)
        
        # For every row in the file, split the row into parts using comma delimeter 
        for row in life_expectancy_file:
            parts = row.split(",")
           
            # Set the variables
            country = parts[0].strip()
            code = parts[1].strip()
            year = int(parts[2].strip())
            life = float(parts[3].strip())

            # If year is equal to year of interest, add the life exp for in a list
            # get the average
            if year == year_of_interest:
                specific_year_list.append(life)
                average = sum(specific_year_list) / len(specific_year_list)

    print(f"For the year {year_of_interest:}:")
    print(f"The average life expectancy across all countries was {average: .2f}")

def compute_specific_year_min_max(year_of_interest):
    lowest = 99999
    low_country = ""

    highest = 0
    high_country = ""

    with open("life-expectancy.csv") as life_expectancy_file:
        # Skip the header
        next(life_expectancy_file)

        # For every row in the file, split the row into parts using comma delimeter 
        for row in life_expectancy_file:
            parts = row.split(",")
            
            # Set the variables
            country = parts[0].strip()
            code = parts[1].strip()
            year = int(parts[2].strip())
            life = float(parts[3].strip())

            # if year is equal to year of interest, get min and max life exp
            if year == year_of_interest:
                if life <= lowest:
                    lowest = life
                    low_country = country
    
                if life >= highest:
                    highest = life
                    high_country = country
                
            
    # Print the results
    print(f"The max life expectancy was {high_country} with {highest}")
    print(f"The min life expectancy was {low_country} in with {lowest}")


# Call the main function
main()