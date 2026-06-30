"""
cagr.py

Calculates Compound Annual Growth Rate (CAGR)
for Revenue, PAT and EPS.
"""


def calculate_cagr(beginning_value, ending_value, years):
    """
    Calculate CAGR.

    Formula:
    CAGR = ((Ending Value / Beginning Value) ** (1 / Years) - 1) * 100
    """

    if beginning_value is None or ending_value is None:
        return None

    if beginning_value <= 0:
        return None

    if ending_value <= 0:
        return None

    if years <= 0:
        return None

    cagr = ((ending_value / beginning_value) ** (1 / years) - 1) * 100

    return round(cagr, 2)


def revenue_cagr(beginning_revenue, ending_revenue, years):
    return calculate_cagr(beginning_revenue, ending_revenue, years)


def pat_cagr(beginning_pat, ending_pat, years):
    return calculate_cagr(beginning_pat, ending_pat, years)


def eps_cagr(beginning_eps, ending_eps, years):
    return calculate_cagr(beginning_eps, ending_eps, years)


if __name__ == "__main__":

    print("=" * 60)
    print("CAGR ENGINE")
    print("=" * 60)

    print("\nRevenue CAGR")
    print(revenue_cagr(1000, 1800, 5))

    print("\nPAT CAGR")
    print(pat_cagr(250, 500, 5))

    print("\nEPS CAGR")
    print(eps_cagr(20, 40, 5))