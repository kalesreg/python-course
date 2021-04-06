# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:29:44 2021
groceries_list.py
@author: kales
"""
import csv
def main():
    # Buying groceries in the express lange with a LIMIT of 20 ITEMS
    sum_prices = 0.0
    num_items = 0
    
    print("How many items do you want to buy?")
    print("Remember at least 1 and no more than 20 items in express lane.")
    num_items = validate_range(num_items, 1, 20)
    items = [" "] * num_items
    qty = [0] * num_items
    price = [0.0] * num_items
    total_price = [0.0] * num_items
    
    # Read data into the lists
    for i in range(0, num_items, 1):
        print("Please enter Grocery List Item ", (i + 1), ":")
        items[i] = input()
        qty[i] = validate_int(qty[i], 0, items[i])
        price[i] = validate_float(price[i], 0, items[i])
        total_price[i] = qty[i] * price[i]
    
    # Display the grocery list
    print("%-20s%-20s%5s%15s%15s\n" % ("Item", "Description", "Qty", \
                                       "Item Price", "Total Price"))
    display_list(items, qty, price, total_price)
    
    # Calculate sum_prices
    for i in range(0, num_items, 1):
        sum_prices = sum_prices + total_price[i]
    
    # Display total
    print("%-10s%20.2f\n" % ("Total Purchase", sum_prices))
    
    # Save grocery list
    save_grocery_list(items, qty, price, total_price)
    
        
def validate_range(value, low_range, high_range):
    while True:
        try:
            value = int(input())
            if not low_range <= value <= high_range: 
                raise Exception
            else:
                break
        except ValueError:
            print("You must enter an integer.")
        except Exception:
            print("You must enter a value that is between", \
                  low_range, "and", high_range, ".")
    return value

def validate_int(value, low_value, description):
    while True:
        try:
            print("Please enter the quantity for", description, ":")
            value = int(input())
            if value < low_value: 
                raise Exception
            else:
                break
        except ValueError:
            print("You must enter an integer.")
        except Exception:
            print("You must enter a value that is at least", low_value, ".")
    return value

def validate_float(value, low_value, description):
    while True:
        try:
            print("Please enter the price for", description, ":")
            value = float(input())
            if value < low_value: 
                raise Exception
            else:
                break
        except ValueError:
            print("You must enter an float.")
        except Exception:
            print("You must enter a value that is at least", low_value, ".")
    return value

def display_list(items, qty, price, total_price):
    try:
        # By adding 1 to len(items), we will throw an error
        for i in range(0, len(items), 1):
            print("%-20s%-20s%5d%15.2f%15.2f\n" % (i, items[i], qty[i], \
                                              price[i], total_price[i]))
    except IndexError:
        print("There was an indexing error.")
    except Exception as err:
        print("An error occurred.")
        print(err)

def save_grocery_list(items, qty, price, total_price):
    try:
        headings = ["Items", "Qty", "Unit Price", "Total Price"]
        
        with open("groceries_file.csv", "w") as groceries_file:
            write = csv.writer(groceries_file)
            write.writerow(headings)
            i = 0
            for row in items:
                write.writerow([items[i], qty[i], price[i], total_price[i]])
                i = i + 1
            
            groceries_file.close()
    except IndexError:
        print("There was an indexing error.")
    except IOError:
        print("An error occurred trying to write to the file.")
    except Exception as err:
        print("An error occurred. Give the following to the help desk.")
        print(err)

main()
