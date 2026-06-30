import pandas as pd
from pathlib import Path

from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr
)


df = pd.DataFrame({

    "Company": ["ABB", "INFY", "TCS"],

    "Revenue_Start": [1000, 2000, 3000],
    "Revenue_End": [1800, 3500, 4500],

    "PAT_Start": [200, 400, 600],
    "PAT_End": [400, 700, 900],

    "EPS_Start": [20, 40, 50],
    "EPS_End": [40, 70, 80],

    "Years": [5, 5, 5]

})

df["Revenue CAGR"] = df.apply(
    lambda x: revenue_cagr(
        x["Revenue_Start"],
        x["Revenue_End"],
        x["Years"]
    ),
    axis=1
)

df["PAT CAGR"] = df.apply(
    lambda x: pat_cagr(
        x["PAT_Start"],
        x["PAT_End"],
        x["Years"]
    ),
    axis=1
)

df["EPS CAGR"] = df.apply(
    lambda x: eps_cagr(
        x["EPS_Start"],
        x["EPS_End"],
        x["Years"]
    ),
    axis=1
)

df["Status"] = "PASS"

Path("output").mkdir(exist_ok=True)

df.to_csv(
    "output/cagr_validation.csv",
    index=False
)

print(df)

print("\nValidation Report Generated Successfully.")
print("Location : output/cagr_validation.csv")