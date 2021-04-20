# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:59:20 2021
gas_prices.py
@author: kales
"""

def main():
    prices = [0.0] * 52
    
    try:
        # Task 1
        
        # Read in the GasPricesFile.txt
        input_file = open('GasPricesFile.txt', 'r')

        # Create list of gas prices
        # Print the headings and the contents of the list with 2 decimals
        index = 0
        print("%-10s%10s" % ("Week", "Gas Prices"))
        for line in input_file:
            data_list = line.split()
            prices[index] = float(data_list[0])
            print("%-10d%10.2f" % (index + 1, prices[index]))
            index += 1
        
        input_file.close()
        
        # Task 2

        # Calculate average gas price by sum prices/size of list
        avg_price = sum(prices) / len(prices)
        
        # Print the results in 2 columns with formatting for 2 decimal places
        print("%-20s%10.2f" % ("average gas price", avg_price))

        # Task 3

        # Save average gas price to file called GasPriceStatistics.txt
        output_file = open('GasPriceStatistics.txt', 'w')
        output_file.write("Average Gas Price: " + str(avg_price))
        output_file.close()

    except IOError:
        print("The file could not be found.")
    except IndexError:
        print("There was an indexing error.")
    except Exception as err:
        print("An error occurred. Give the following to the help desk:")
        print(err)

# Call the main function
main()