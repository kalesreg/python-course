# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:16:59 2021
payroll.py
@author: kales
"""
# Process a payroll report and save the results to an output file

def main():
    names = [" "] * 3
    hours = [0.0] * 3
    rates = [0.0] * 3
    gross = [0.0] * 3
    highest_gross = 0.0
    highest_paid = " "
    lowest_gross = 0.0
    lowest_paid = " "
    
    try:
        # Get file name from user
        file_name = input("Enter the file name: ")
        
        # Open the input file
        input_file = open(file_name, 'r')
        
        # Open the output file
        output_file = open('payroll.txt', 'w')
        
        
        index = 0
        # Header for print report
        print("%-15s%15s%15s%15s" % ("Name", "Hours", "Hourly Rate", "Gross Pay"))
        for line in input_file:
            # Read in the data and print each line under the header
            data_list = line.split()
            names[index] = data_list[0]
            hours[index] = float(data_list[1])
            rates[index] = float(data_list[2])
            gross[index] = hours[index] * rates[index]
            # Print the row of data
            print("%-15s%15.0f%15.2f%15.2f" % (names[index], hours[index],\
                                               rates[index], gross[index]))
            # Output the 4 lists into an output file called payroll.txt
            output_file.write(str(names[index]) + " ")
            output_file.write(str(hours[index]) + " ")
            output_file.write(str(rates[index]) + " ")
            output_file.write(str(gross[index]) + "\n")
            index += 1

        # Display the name and gross pay of the employee with the highest gross pay
        highest_gross = gross[0]
        highest_paid = names[0]
        lowest_gross = gross[0]
        lowest_paid = names[0]
        
        for m in range(0, 3, 1):
            if gross[m] > highest_gross:
                highest_gross = gross[m]
                highest_paid = names[m]
            if gross[m] < lowest_gross:
                lowest_gross = gross[m]
                lowest_paid = names[m]
        average_gross = sum(gross) / len(gross)
        
        print("\n%-25s%25s" % ("Employee", "Highest Gross Pay"))
        print("%-25s%25.2f" % (highest_paid, highest_gross))
        print("\n%-25s%25s" % ("Employee", "Lowest Gross Pay"))
        print("%-25s%25.2f" % (lowest_paid, lowest_gross))
        print("\n%-25s%25.2f" % ("Average Gross Pay", average_gross))
    
    except IOError:
        print("The file could not be found.")
    except IndexError:
        print("There was an indexing error.")
    except Exception as err:
        print("An error occurred. Give the following to the help desk:")
        print(err)

# Call main function
main()