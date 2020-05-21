# -*- coding: utf-8 -*-
"""
Asynch M1 - Challenge Lesson - International Microfinance Lending - Phase 3 - Solved

In this script, the focus will be on utilizing functions as well as the CSV reader/writer to automate the cash flow evaluation process for an externally held portfolio.
"""

# Phase 3 - Process Automation

# In Phase 3 of the International MicroFinance Lending Challenge Lesson, you
# are looking to automate the process futher by being able to import an externally held CSV file as well as writing the result of the cash flow analysis back out to a file.

# The portfolio being evaluated is the same as from Phase 2, only it is contained in a CSV file located in the Resources folder.


print('----- 1 -----')


# Part 1 -  Importing the CSV File.

# The International MicroFinance Loan information is no longer contained in a
# Python list that is hard coded into the script.

# The focus for the first part of Phase 3will be to import the CSV from the
# Resources folder.


# Instructions

# Utilizing the instructions from the curriculum content (Lesson 4)...


# @TODO
# Import the Path module from the pathlib library as the csv library

from pathlib import Path
import csv

# Initialize a empty loans list to be built off of the loans in the csv file.
microfinance_portfolio_data_csv = []

# @TODO
# Create a global variable and assign it the module and file location of the CSV
# file for this activity. You will find the CSV file located in the Resources
# folder for the Phase.

csvpath = Path('./Resources/microfinance_loan_portfolio.csv')


# @TODO
# Utilizing the code from the Lesson 4 material: open, read, and print the CSV
# version of the International Microfinance Loan Portfolio CSV file for review.

with open(csvpath, 'r') as csvfile:

    print(type(csvfile))

    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))

    header = next(csvreader)
    print(f'{header} <---HEADER')

    for row in csvreader:

        print(row)
        microfinance_portfolio_data_csv.append(row)

# @TODO
# Write the print statement that displays the imported portfolio.
print(f"The imported microfinance loan portfolio looks like: {microfinance_portfolio_data_csv}")



print('----- 2 -----')


# Part 2 - Loan Portfolio Format

# You will notice that the loan portfolio is in a slightly different format now.

# In a couple of sentences, compare and contrast the differences between the
# portfolio imported from the CSV file and the list of dictionaries that formed
# the bases of the work in Phases 1 and 2.

# Write your short answers below:

# ANSWERS - Loan Portfolio Format
# * The portfolio still includes all of the dictionary values, including the
# interval repayment amount.
# * Now a list of lists, rather than a list of dictionaries.
# * Key:Value pairs are gone; have to reference values by their index position.
# * Numerical values are strings rather than numbers. Several values will have # to be to floats and int's to be utilized.


print('----- 3 -----')


# Part 3 - Converting the Cash Flow Functions

# Because the International Microfinance Portfolio is now a list of lists,
# changes have to be made to the calculate_monthly_cash_flows variables to accommodate the new format.

# The code from Phase 2 - Part 2 has been transferred here.

# You will need make code alterations in two places to get it back working.

# 1. The descriptive variables that feed the calculate_monthly_cash_flows calculations will need to capture data from the new loan 'list' format.

# 2. The function call for calculate_monthly_cash_flows will need to pass the
# variable name of the portfolio as it was read in from the CSV file.

# That's it! Make those changes and you should be back to calculating the
# monthly cash flow number.



# Use the following FX rates when processing calculations. These rates differ
# from the ones provied at the time the loan was issued.
current_fx_rate_usdpkr = 157.15
current_fx_rate_usdkes = 102.48
current_fx_rate_usdinr = 74.06


# The following function will convert a foreign currency amount to USD based on
# the amount and currency passed in. This function uses the globally-scoped current fx rates detailed above.
def convert_local_cash_flow_to_usd(local_cash_flow, local_currency):
    """
    Converts the foreign currency cash flow amount into a US dollar amount
    using the fx rate provided.

    Args:
        local_cash_flow (float): The amount of local currency to be converted
        local_currency (string): The identifier of the local currency to be converted

    Return:
        The USD value of the converted cash flow.
    """

    flow_converted_to_usd = 0.0

    if local_currency == 'pkr':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdpkr

    if local_currency == 'kes':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdkes


    if local_currency == 'inr':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdinr


    return round(flow_converted_to_usd, 2)


# Create a function called 'calculate_monthly_cash_flows' The function
# will take in 2 arguments, the loan portfolio and the month for which you
# would like cash flow information.


def calculate_monthly_cash_flows(loan_portfolio, month_of_repayment):
    """
    Calculates the US dollar cash flows generated by a specified loan portfolio
    for the specified month.

    Args:
        loan_portfolio (list) - the loan portfolio to be analyzed
        month_of_repayment (int) - the month for which the repayment information is being rendered

    Return:
        The USD amount expected for repayment on the specified month.
    """

    # Create a function-scoped variable to hold the usd total of the monthly flow.
    monthly_cash_flow_total_usd = 0.0


    # Write the for loop that iterates through each loan in the  imported portfolio.
    for loan in loan_portfolio:

        # Metric variable
        monthly_cash_flow_amount_in_usd = 0.0

        # @TODO: Create descriptive variables for each of the index positions
        # in the loan and assign them to the index position of the loan.
        # This will make the elements easier to recognize and reference in the
        # function.
            # HINT - Variables names should be based off of the CVS file HEADER.
            # HINT - The CSV values are strings. It makes sense to convert the
            # relevant values into integers or floats at this stage

        loan_value_usd = int(loan[0])
        term_in_months = int(loan[1])
        annual_interest_rate = float(loan[2])
        repayment_interval = loan[3]
        local_currency = loan[4]
        fx_rate_at_loan_issue = float(loan[5])
        loan_local_value = int(loan[6])
        interval_repayment_amount = int(loan[7])

        # @TODO: Write a print statements that compares the loan and the
        # variables just created.

        print(f"CSV loan: {loan}")


        print("")


        # Create the 3 conditional statements that differentiate the
        #  loans by repayment_interval. Start with "monthly"
        if repayment_interval == 'monthly':

            # Nest a second conditional that verifies if the portfolio will
            # make a payment for the month in question.
            if month_of_repayment <= term_in_months:

                #If there is a payment made on the month in question, convert the local period repayment to USD.
                monthly_cash_flow_amount_in_usd = convert_local_cash_flow_to_usd(interval_repayment_amount, local_currency)

            else:
                print("No flows for this month from this loan")


        #  Write the code block for the "quarterly" repayment interval.
        elif repayment_interval == 'quarterly':

            if (month_of_repayment % 3 == 0) and (month_of_repayment <= term_in_months):

                monthly_cash_flow_amount_in_usd = convert_local_cash_flow_to_usd(interval_repayment_amount, local_currency)

            else:
                print("No flows for this month from this loan")


        # Write the code block for the "bullet" repayment interval.
        elif repayment_interval == 'bullet':

            if month_of_repayment == term_in_months:

                monthly_cash_flow_amount_in_usd = convert_local_cash_flow_to_usd(interval_repayment_amount, local_currency)

            else:
                print("No flows for this month from this loan")

        # Write the equation that adds each monthly_cash_flow_amount_in_usd
        # amount to the monthly_cash_flow_total_usd.
        monthly_cash_flow_total_usd += monthly_cash_flow_amount_in_usd

    # Write the return statement for the monthly_cash_flow_total_usd so
    #  it can be used outside the function.
    return monthly_cash_flow_total_usd


# Create the function call for the calculate_monthly_cash_flow function.
# Pass the micro-finance loan and the value of the month (1-12).

month_of_cash_flow = 6

total_amount_of_usd_for_month = calculate_monthly_cash_flows(microfinance_portfolio_data_csv, month_of_cash_flow)

# Write the print statement for US dollar value cash flows for the month.
# Be sure to round the value to 2 decimal places.

print(f"Total USD flows for the month: ${total_amount_of_usd_for_month: .2f}.")


print('----- 4 -----')


# Part 4 - Writing to a CSV File

# The last step in the automation process is to write the value of the USD cash
# flow back out to the Resources file.

# Using the documentation provided in Lesson 4, write the code block that will
# output the value of the USD flows to a CSV file

# Establish the output path for the CSV file
output_path = Path('./Resources/output.csv')

header = ["month", "cash_flow"]

metrics = [month_of_cash_flow, round(total_amount_of_usd_for_month, 2)]

# @TODO: Use the open() method to write the output path as a file object.
# Write rows for both the header and metric variables. Don't forget to include a print statement that confirms when the file has been written.

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    csvwriter.writerow(metrics)
    print("File written")
