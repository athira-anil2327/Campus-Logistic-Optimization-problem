# Campus Logistics Network Optimization
**Prescriptive Analytics and Infrastructure Selection Model**

## Executive Summary
This project presents a mathematical optimization framework designed to transition Campus City Logistics from an ad-hoc distribution model to a centralized, two-hub network. By applying Mixed-Integer Linear Programming (MILP), the model identifies the most cost-effective infrastructure configuration that satisfies 100% of campus demand while adhering to a strict annual budgetary ceiling of $1,500,000.

## Strategic Objectives
The primary goal is to solve a Facility Location-Allocation problem with the following requirements:
* **Infrastructure Selection:** Evaluate and select exactly two out of three potential warehouse sites (North, South, and East).
* **Cost Minimization:** Reduce total annual expenditure, including capital investment and variable shipping costs.
* **Service Reliability:** Ensure 100% fulfillment of daily demand across six distinct campus facilities.

## Mathematical Formulation



### Objective Function
The model seeks to minimize the total annual cost ($Z$):
$$Z = \sum_{j \in W} (F_j \cdot y_j) + 365 \times \sum_{j \in W} \sum_{i \in F} (C_{ji} \cdot x_{ji})$$

### Constraints
1. **Demand Satisfaction:** All facilities must receive their total required units per day.
   $$\sum_{j \in W} x_{ji} = D_i, \quad \forall i \in F$$

2. **Capacity Limit:** Throughput at any node cannot exceed its rated physical capacity.
   $$\sum_{i \in F} x_{ji} \leq Cap_j \cdot y_j, \quad \forall j \in W$$

3. **Network Redundancy:** The system is constrained to operate exactly two warehouses.
   $$\sum_{j \in W} y_j = 2$$

4. **Financial Amortization:** Construction costs are amortized over a 10-year lifecycle to reflect accurate annual fiscal impact.

## System Architecture
The repository is organized to separate data assets from the optimization logic:
* **`/data`**: Contains CSV source files for warehouse parameters, facility demand profiles, and transportation cost matrices.
* **`/src`**: Contains the core Python implementation (`optimizer.py`) utilizing the PuLP library.
* **`.gitignore`**: Configured to prevent the tracking of Python bytecode and environment artifacts.

## Technology Stack
* **Language:** Python 3.x
* **Optimization Engine:** PuLP (COIN-OR CBC Solver)
* **Data Processing:** Pandas
* **Visualization:** Matplotlib

## Execution Instructions
1. Clone the repository to your local machine.
2. Ensure dependencies are installed via `pip install pulp pandas matplotlib`.
3. Navigate to the `src` directory and execute `python optimizer.py`.