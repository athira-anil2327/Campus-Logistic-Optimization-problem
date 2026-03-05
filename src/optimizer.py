import pandas as pd
import pulp

# Load data
wh = pd.read_csv('../data/warehouses.csv').set_index('warehouse_id')
dm = pd.read_csv('../data/demands.csv').set_index('facility_id')
tr = pd.read_csv('../data/transportation_costs.csv')

# Setup constants
BUDGET = 1500000  # Annual budget limit
DAYS = 365
AMORT_YEARS = 10  # Construction amortized over 10 years

# Define Problem
model = pulp.LpProblem("Logistics_Optimization", pulp.LpMinimize)

# Decision Variables
# y: Is the warehouse open? (Binary)
y = pulp.LpVariable.dicts("Open", wh.index, cat='Binary')
# x: Quantity shipped (Continuous)
x = pulp.LpVariable.dicts("Flow", (wh.index, dm.index), lowBound=0)

# Goal: Minimize Total Annual Cost (Fixed + Variable)
fixed_costs = pulp.lpSum([
    ((wh.at[j, 'construction_cost'] / AMORT_YEARS) + (wh.at[j, 'daily_op_cost'] * DAYS)) * y[j]
    for j in wh.index
])
# Note: You'll need to map tr_costs to a dict for the shipping part
model += fixed_costs # + your_shipping_calculation

# Constraints
# 1. Exactly 2 warehouses must open
model += pulp.lpSum([y[j] for j in wh.index]) == 2

# 2. Capacity: Total daily flow <= Capacity * y
for j in wh.index:
    model += pulp.lpSum([x[j][i] for i in dm.index]) <= wh.at[j, 'capacity'] * y[j]

# Solve
model.solve()
print(f"Status: {pulp.LpStatus[model.status]}")