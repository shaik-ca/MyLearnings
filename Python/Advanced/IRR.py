import numpy as np

# Example cash flows
cash_flows = [-1000, 300, 400, 500, 600]  # Initial investment followed by returns

# Calculate IRR
irr = np.irr(cash_flows)

# Print the IRR as a percentage
print(f"IRR: {irr:.4%}")