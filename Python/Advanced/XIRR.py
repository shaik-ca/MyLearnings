import numpy as np
import numpy_financial as npf

# Define the cash flows and corresponding dates
cash_flows = [-1000, 300, 420, 680]  # Example cash flows
dates = ['2024-01-01', '2024-04-01', '2024-07-01', '2024-10-01']  # Corresponding dates

# Convert dates to ordinal format
dates = [np.datetime64(date).astype('O') for date in dates]
dates = np.array([(date - np.datetime64('1970-01-01')) / np.timedelta64(1, 'D') for date in dates])

# Define the function to compute XIRR
def xirr(cash_flows, dates):
    # Use Newton's method to find the IRR
    def irr_func(rate):
        return np.sum(cash_flows / (1 + rate) ** (dates - dates[0]))

    # Initial guess
    guess = 0.1
    
    # Solve for IRR
    irr = npf.irr(cash_flows)
    
    return irr

# Compute XIRR
irr_value = xirr(cash_flows, dates)
print(f'XIRR: {irr_value:.6f}')