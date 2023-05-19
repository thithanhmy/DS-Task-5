# DS-Task-5

# Capstone project I - variables and control structures
import math

# Display options
print('investstment - to calculate the amount of interest you\'ll earn on your investment')
print('bond         - to calculate the amount you\'ll have to pay on a home loan')
print() # add extra line space

# Get user input and convert to lower case to make it not case sensitive
user_input = input('Enter either \'investment\' or \'bond\' from the menu above to proceed: ')
user_input = user_input.lower()

# Check input validity and investment calculations
if user_input != 'investment' and user_input != 'bond':
    print('Entry not valid')

elif user_input == 'investment':
    P = int(input('Please enter the amount of money you want to deposit: '))
    r = int(input('Please provide the number for the interest rate as percentage: ')) / 100
    t = int(input('Please enter the number of years you plan on investing: '))
    interest = input('Please specify if you want \'simple\' or \'compound\' interest: ')
    interest = interest.lower()
    
    # simple interest calculation
    if interest != 'simple' and interest != 'compound':
        print('Entry not valid')

    elif interest == 'simple':
        A = P*(1 + r*t)
        print(f'Based on your input the total amount once the interest has been applied will be {A:.2f}.')
    
    # compound interest calculation
    elif interest == 'compound':
        A = P *  math.pow((1+r),t)
        print(f'Based on your input the total amount once the interest has been applied will be {A:.2f}.')

# Bond calculations
elif user_input == 'bond':
    P = int(input('Please enter the present value of your house: '))
    r = int(input('Please provide the number for the interest rate as percentage: ')) / 100
    i = r / 12
    n = int(input('Please enter the number of months you plan to take to repay the bond: '))

    # Repaymeny calculations
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f'You will have to repay an amount of {repayment:.2f} each month.')