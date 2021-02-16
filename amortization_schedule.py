# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:12:01 2021
amortization_schedule.py
@author: kales
"""

# An amortization schedule shows the detail for loan payments with a fixed rate
# not adjustable like a credit card.

def main():
    # sum of interest is summing the interest for all loans
    sum_of_interest = 0.0
    print("At we <3 You Auto Dealers, we give credit to everyone.")
    print("Please enter InDebtMe if you want to run the program or No to quit.")
    run_program = input()
    # begin the sentinel value loop that runs the program w/InDebtMe
    while (run_program.lower() == "indebtme"):
        loan_amount = float(input("Loan Amount: "))
        # this is a data validation loop making sure loan >= $1
        while loan_amount < 1:
            print("Invalid. The loan amount must be at least 1 dollar.")
            loan_amount = float(input("Loan Amount: "))
        
        # getting years for the loan term
        years = int(input("number of Years: "))
        # validation loop to make sure that years >= 1
        while years < 1:
            print("Invalid. The loan term must be at least 1 year.")
            years = int(input("Number of Years: "))
       
        # getting the annual interest rate
        annual_rate = float(input("Annual Interest Rate: (ex. 1 for 1%): "))
        # validation loop to make sure the annual_rate >= 1
        while annual_rate < 1:
            print("Invalid. The annual interest rate must be at least 1%.")
            annual_rate = float(input("Annual Interest Rate: "))
        
        # calculate the monthly interest rate
        monthly_interest_rate = annual_rate / 100 / 12
        
        # calculate monthly payment
        monthly_payment = loan_amount * monthly_interest_rate / \
            (1 - (1 / (1 + monthly_interest_rate) ** (years * 12)))
        # display monthly payment
        print("Monthly Payment: %.2f" % monthly_payment)
        
        # Display monthly percent
        print("Monthly Interest Rate: %s%.5f\n" % ("%", \
            (monthly_interest_rate * 100)))
        
        # Display total payments
        number_of_payments = years * 12
        print("Total Payments: %.2f\n" % (monthly_payment * number_of_payments))
        
        # Create amortization schedule
        beginning_balance = loan_amount
        # Print report headings
        print("%-10s%15s%10s%12s%12s%12s" % ("Payment#", "Beginning Bal.", \
            "Interest", "Principal", "Total Paid", "Ending Bal."))
        for i in range(1, number_of_payments + 1, 1):
            interest = monthly_interest_rate * beginning_balance
            principal = monthly_payment - interest
            total_paid = interest + principal
            ending_balance = beginning_balance - principal
            print("%-10d%15.2f%10.2f%12.2f%12.2f%12.2f" % (i, beginning_balance, \
                interest, principal, total_paid, ending_balance))
            beginning_balance = ending_balance
            if (i % 12) == 0 and ending_balance >= 0.01:
                print("That was the end of year %d" % (i / 12))
                print("You still have $", format(ending_balance, ',.2f'), \
                      "to pay off.")
            sum_of_interest = sum_of_interest + interest
        
        # ask the user to run the program again
        print("Please enter InDebtMe if you want to run the program or No to quit.")
        run_program = input()

    print("The sum of interest for all loans calculated is $%.2f" % (sum_of_interest))
    print("At We <3 Autos, We <3 love and especially your money.")

# call the main method/function
main()