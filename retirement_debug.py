# This program uses a void function to calculate and then
# display the retirement amount that an employer should
# set aside for an emaployee's retirement given the
# gross_pay and match in percent. 
# Here is how the program should run with a test case of 100000 and 5 %
# Enter the gross pay: 100000
# Enter the employer retirement match as a % (ex 10 for 10%:) 5
# Contribution for gross pay: $5,000.00
# This program requires the use of the main() and 
# show_retirement_contrib(() functions and the
# calculation must take place in the 
# show_retirement_contrib() function
def main(): # Error: Add the colon
    gross_pay = float(input('Enter the gross pay: '))
    match = int(input('Enter the employer retirement match as a % (ex 10 for 10%:) '))
    gross_pay = show_retirement_contrib(match, gross_pay) # Error: Remove input and add match argument

# The show_retirement_contrib function accepts the
# gross_pay and match as arguments and displays the
# retirement contribution required by the employer.
# you must multiply the gross_pay by the match converted to a percent
# in order to calculate the contrib
def show_retirement_contrib(match, gross_pay): # Error add underscore and colon, edit spelling
    contrib = gross_pay * (match / 100)
    print('Contribution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='') # Error: float not integer and 2 decimals and comma formatting

# Call the main function.
main()
