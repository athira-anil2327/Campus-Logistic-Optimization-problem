# Campus Logistics Optimization using MILP

This project implements a **Mixed Integer Linear Programming (MILP)** model to design an optimized emergency supply distribution network for a university campus.
The goal is to minimize total annual logistics cost while satisfying facility demand, warehouse capacity constraints, and redundancy requirements.

The optimization model is implemented in **Python using the PuLP library**, while **Folium** is used to visualize the resulting supply routes and warehouse locations on an interactive geographic map.

---

## Problem Overview

Campus City requires a reliable emergency supply distribution network. The logistics system must determine:

* Which warehouses should be operational
* How supplies should be distributed to campus facilities
* The minimum annual cost while maintaining operational constraints

The system includes:

* **3 candidate warehouses**
* **6 campus facilities**
* Daily supply demands
* Warehouse capacity limitations
* Transportation costs

A **redundancy constraint** requires that **exactly two warehouses remain active** at all times to ensure reliability in case of a facility failure.

---

## Mathematical Model

The problem is formulated as a **Mixed Integer Linear Programming (MILP)** optimization.

### Decision Variables

* **yᵢ** : Binary variable representing whether warehouse *i* is active
* **xᵢⱼ** : Continuous variable representing annual supply shipped from warehouse *i* to facility *j*

### Objective Function

Minimize total annual cost:

* Amortized warehouse construction cost
* Annual operational cost
* Transportation cost per unit

[
\min Z =
\sum_{i \in W} \left(\frac{C_i}{10} + 365 \cdot O_i \right) y_i
+
\sum_{i \in W}\sum_{j \in F} (4.35 \cdot x_{ij})
]

---

## Constraints

1. **Demand Satisfaction**

Each facility must receive its required annual demand.

[
\sum_{i \in W} x_{ij} = D_j \times 365
]

2. **Warehouse Capacity**

Total shipments from a warehouse must not exceed its capacity.

[
\sum_{j \in F} x_{ij} \le S_i \times 365 \cdot y_i
]

3. **Redundancy Requirement**

Exactly **two warehouses must be active**.

[
\sum_{i \in W} y_i = 2
]

---


## Dataset Tables

### Facility Demand Dataset

| Facility | Daily Demand (Units) | Annual Demand (Units) |
|---------|----------------------|----------------------|
| MED_CENTER | 80 | 29,200 |
| ENG_BUILDING | 30 | 10,950 |
| SCIENCE_HALL | 35 | 12,775 |
| DORM_A | 55 | 20,075 |
| DORM_B | 45 | 16,425 |
| LIBRARY | 25 | 9,125 |

---

### Warehouse Dataset

| Warehouse | Daily Capacity | Construction Cost ($) | Daily Operating Cost ($) |
|-----------|---------------|----------------------|-------------------------|
| WH_NORTH | 400 | 300,000 | 800 |
| WH_SOUTH | 350 | 280,000 | 700 |
| WH_EAST | 450 | 320,000 | 900 |

---

### Warehouse Coordinate Dataset

| Warehouse | Latitude | Longitude |
|-----------|----------|-----------|
| WH_NORTH | 10.130 | 76.465 |
| WH_SOUTH | 10.120 | 76.450 |
| WH_EAST | 10.125 | 76.470 |

---

### Facility Coordinate Dataset

| Facility | Latitude | Longitude |
|----------|----------|-----------|
| MED_CENTER | 10.128 | 76.458 |
| ENG_BUILDING | 10.127 | 76.462 |
| SCIENCE_HALL | 10.124 | 76.463 |
| DORM_A | 10.121 | 76.456 |
| DORM_B | 10.119 | 76.459 |
| LIBRARY | 10.126 | 76.455 |

---

### Transportation Cost Parameter

| Parameter | Value |
|----------|------|
| Average Transportation Cost per Unit | \$4.35 |
| Planning Horizon | 365 Days |
| Construction Amortization Period | 10 Years |
| Annual Budget Limit | \$1,500,000 |


## Technologies Used

* Python
* PuLP (Linear Programming Solver)
* Folium (Geospatial Visualization)
* Jupyter / Google Colab

---

## Project Structure

```
Campus-Logistics-Optimization
│
├── optimization_model.py
├── campus_map.html
├── campus_map.png
├── report.tex
└── README.md
```

---

## Visualization

The optimized logistics network is visualized using **Folium**.

* 🟢 Green markers represent **active warehouses**
* 🔴 Red markers represent **inactive warehouses**
* 🔵 Blue markers represent **campus facilities**
* 🔵 Lines represent **supply routes**

Example map output:

![Distribution Map](campus_map.png)

---

## Results

The optimization recommends activating:

* **WH_NORTH**
* **WH_SOUTH**

while keeping **WH_EAST closed**.

Key results:

* **Total Annual Cost:** $1,034,192.50
* **Budget Limit:** $1,500,000
* **Budget Utilization:** 68.9%

This leaves a **31.1% budget surplus** for future capacity expansion or emergency reserves.

---

## How to Run the Project

1. Install required libraries

```
pip install pulp folium
```

2. Run the optimization script

```
python optimization_model.py
```

3. The map will be generated as

```
campus_map.html
```

Open this file in a browser to view the interactive distribution network.

---

## Author

**Athira Adiparambil Anil**
Computer Science Engineering Student
Specializing in Machine Learning and Optimization
