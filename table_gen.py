import pandas as pd
from datetime import datetime, timedelta
import calendar

# Function to generate the table
def generate_table(face_amount, spread, issue_date, maturity_date, yield_rate, benchmark_data):
    # Convert input values to the appropriate types
    face_amount = int(face_amount)  # Ensure face_amount is an integer (in dollars)
    spread = float(spread)  # Ensure spread is a float
    issue_date = datetime.strptime(issue_date, "%Y-%m-%d")  # Ensure issue_date is a datetime object
    maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")  # Ensure issue_date is a datetime object
    yield_rate = float(yield_rate)  # Ensure yield_rate is a float

    # Prepare the table
    table = []
    principal = 0  # Initial principal (will be 0 for all rows except the last)
    
    # Loop through benchmark data
    for i, (date_str, total_interest_rate) in enumerate(benchmark_data):
        # Parse the initial date
        initial_date = datetime.strptime(date_str, "%m/%d/%Y")
        
        # Calculate the last day of the next month
        # First, increment the month by 1
        next_month = initial_date.replace(day=28) + timedelta(days=4)  # Move to the next month
        pay_date = next_month - timedelta(days=next_month.day)  # Get the last day of the next month
        
        # If it's the first row, handle the issue date separately
        if i == 0:
            months_from_issue = 0
            # For the first row, the interest, discount factor, and present value should be None or zero
            interest = 0
            discount_factor = 1  # Present value at issue date
            present_value = 0  # No present value yet for the issue date
            principal = 0  # No principal yet at the issue date
        else:
            # Calculate months from the issue date for the subsequent rows
            months_from_issue = (pay_date.year - issue_date.year) * 12 + pay_date.month - issue_date.month
            
            total_interest_rate = (benchmark_data[i - 1][1] + spread)/100
            # print('tir', benchmark_data[i - 1][1], spread, total_interest_rate)
            # Calculate Interest (monthly interest based on annual interest rate)
            interest = face_amount * total_interest_rate / 12 if total_interest_rate != 0 else 0
            
            # Calculate Discount Factor based on yield_rate
            discount_factor = 1 / (1 + yield_rate / 1200) ** months_from_issue
            
            # Calculate Present Value (Principal + Interest) discounted to the present
            present_value = (principal + interest) * discount_factor
        
        is_last_month = pay_date.month == maturity_date.month and pay_date.year == maturity_date.year
        
        # If it's the last row (March 31, 2027), add the principal
        if is_last_month:  # 3/31/2027, 40th payment
            principal = face_amount  # Add Face Amount to the principal
            present_value = (principal + interest) * discount_factor

    
        
        # Append row data to the table
        table.append({
            "Pay Date": pay_date.strftime("%m/%d/%Y"),
            "Principal": principal if i == len(benchmark_data) - 1 else "-",  # Add principal only for the last row
            "Interest": round(interest, 2) if i != 0 else None,  # No interest for the first row
            "Discount Factor": round(discount_factor, 10) if i != 0 else None,  # No discount factor for the first row
            "Present Value": round(present_value, 0) if i != 0 else None  # No present value for the first row
        })
    
    return table
