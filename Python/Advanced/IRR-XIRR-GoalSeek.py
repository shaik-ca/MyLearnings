import numpy as np
from scipy.optimize import newton, root_scalar
from datetime import datetime

def calculate_irr(cash_flows):
    """
    Calculate the Internal Rate of Return (IRR) for a series of cash flows.

    :param cash_flows: List of cash flows (including initial investment).
    :return: The IRR value as a decimal.
    """
    return np.irr(cash_flows)

def npv(rate, cash_flows, dates=None):
    """
    Calculate the Net Present Value (NPV) for a series of cash flows and optional dates.

    :param rate: Discount rate as a decimal.
    :param cash_flows: List of cash flows.
    :param dates: List of corresponding dates (used for XIRR).
    :return: The NPV value.
    """
    if dates is None:
        # Standard NPV calculation for IRR
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
    else:
        # XIRR calculation with dates
        return sum(cf / (1 + rate)**((date - dates[0]).days / 365.0) for cf, date in zip(cash_flows, dates))

def calculate_xirr(cash_flows, dates):
    """
    Calculate the Extended Internal Rate of Return (XIRR) for cash flows with specific dates.

    :param cash_flows: List of cash flows.
    :param dates: List of corresponding dates.
    :return: The XIRR value as a decimal.
    """
    return newton(lambda r: npv(r, cash_flows, dates), 0.1)  # Initial guess of 10%

def goal_seek(target_value, cash_flows, dates=None):
    """
    Perform Goal Seek to find the rate that makes the NPV equal to the target value.

    :param target_value: Desired NPV value (e.g., 0 for IRR).
    :param cash_flows: List of cash flows.
    :param dates: List of corresponding dates (used for XIRR).
    :return: The rate that achieves the target NPV.
    """
    def npv_function(rate):
        return npv(rate, cash_flows, dates) - target_value

    # Use bracket method to find the root of npv_function
    result = root_scalar(npv_function, bracket=[-1, 1], method='brentq')
    return result.root

# Example usage

# IRR
cash_flows = [-1000, 300, 400, 500, 600]
irr_value = calculate_irr(cash_flows)
print(f"IRR: {irr_value:.4%}")

# XIRR
dates = [
    datetime(2023, 1, 1),
    datetime(2023, 6, 1),
    datetime(2023, 12, 1),
    datetime(2024, 6, 1),
    datetime(2024, 12, 1)
]
xirr_value = calculate_xirr(cash_flows, dates)
print(f"XIRR: {xirr_value:.4%}")

# Goal Seek
target_value = 0  # For IRR, we use a target NPV of 0
goal_seek_rate = goal_seek(target_value, cash_flows, dates)
print(f"Goal Seek Rate: {goal_seek_rate:.4%}")