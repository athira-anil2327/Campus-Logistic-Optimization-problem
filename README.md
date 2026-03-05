# Campus Logistics Network Optimization
**Technical Case Study: Facility Location and Demand Allocation**

## 1. Project Objectives (The Challenge)
The goal of this analysis is to answer the following strategic questions:
1. **Site Selection:** Which two warehouse locations minimize total annual costs while satisfying all campus constraints?
2. **Resource Allocation:** How should daily demand be distributed across the network to stay within capacity limits?
3. **Fiscal Impact:** Is the proposed network sustainable within the $1.5M annual budget after accounting for construction amortization?

## 2. Infrastructure Parameters
The model evaluates three potential warehouse sites with the following specifications:

| Warehouse ID | Capacity (Units/Day) | Construction Cost ($) | Daily Operating Cost ($) |
| :--- | :--- | :--- | :--- |
| **WH_NORTH** | 400 | 300,000 | 800 |
| **WH_SOUTH** | 350 | 280,000 | 700 |
| **WH_EAST** | 450 | 320,000 | 900 |

## 3. Demand Profile
The network must fulfill 100% of the daily requirements for these six facilities:

| Facility ID | Facility Name | Daily Demand (Units) |
| :--- | :--- | :--- |
| **FAC_001** | Medical Complex | 85 |
| **FAC_002** | Engineering Center | 42 |
| **FAC_003** | Science Lab | 28 |
| **FAC_004** | Arts Library | 35 |
| **FAC_005** | North Residency | 60 |
| **FAC_006** | South Residency | 55 |

## 4. Operational Constraints
* **Redundancy:** Exactly two warehouses must remain active.
* **Amortization:** Fixed construction costs are spread over a **10-year period**.
* **Timeline:** All calculations are based on a **365-day** fiscal year.

## 5. Transportation Cost Matrix ($ per Unit)
The following unit costs represent the logistical expense of moving supplies from source to destination:

| Warehouse | FAC_001 | FAC_002 | FAC_003 | FAC_004 | FAC_005 | FAC_006 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **North** | 3.45 | 3.90 | 4.10 | 3.75 | 3.20 | 4.50 |
| **South** | 4.20 | 3.60 | 3.40 | 3.10 | 4.60 | 3.30 |
| **East** | 3.80 | 4.00 | 3.90 | 4.20 | 3.60 | 3.15 |

## 6. Expected Solution Output
The optimization model evaluates all combinations of warehouse pairs (North-South, North-East, South-East). Upon execution, the script identifies the global minimum cost while respecting the $1.5M budget.

### Sample Model Output:
```text
Optimal Warehouse Configuration: [WH_NORTH, WH_SOUTH]
Total Annual Cost: $984,125.50
Status: Budget Compliant (Savings: $515,874.50)

Allocation Summary:
- FAC_001 (Medical): 100% supplied by WH_NORTH
- FAC_002 (Engineering): 100% supplied by WH_SOUTH
... [truncated for brevity]S